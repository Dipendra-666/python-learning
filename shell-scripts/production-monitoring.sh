#!/bin/bash

###############################################################################
# Author      : Dipendra Rayamajhi
# Version     : v1.0.0
# Script Name : production_monitoring_tool.sh
#
# Description:
# This production-grade DevOps monitoring script performs:
#   - System health checks
#   - CPU monitoring
#   - Memory monitoring
#   - Disk usage monitoring
#   - Top process monitoring
#   - Service health checks
#   - Network connectivity checks
#   - Log generation
#   - Alerting for threshold breaches
#
# This script demonstrates:
#   - Bash best practices
#   - Error handling
#   - Logging
#   - Functions
#   - Modular scripting
#   - Automation mindset
#   - Production-ready structure
#
# Usage:
#   chmod +x production_monitoring_tool.sh
#   ./production_monitoring_tool.sh
#
###############################################################################

set -Eeuo pipefail

#############################################
# Global Variables
#############################################

LOG_FILE="/tmp/system_monitor.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')
HOSTNAME=$(hostname)
CPU_THRESHOLD=80
MEM_THRESHOLD=80
DISK_THRESHOLD=80

#############################################
# Logging Function
#############################################

log_info() {
    echo "[$DATE] [INFO] $1" | tee -a "$LOG_FILE"
}

log_warn() {
    echo "[$DATE] [WARNING] $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo "[$DATE] [ERROR] $1" | tee -a "$LOG_FILE"
}

#############################################
# Error Handler
#############################################

handle_error() {
    log_error "Script failed at line number $1"
    exit 1
}

trap 'handle_error $LINENO' ERR

#############################################
# Banner
#############################################

show_banner() {
    echo "========================================================="
    echo "        Production Grade DevOps Monitoring Tool          "
    echo "========================================================="
    echo "Hostname : $HOSTNAME"
    echo "Executed : $DATE"
    echo "Log File : $LOG_FILE"
    echo "========================================================="
}

#############################################
# Check Required Commands
#############################################

check_dependencies() {
    log_info "Checking required dependencies"

    REQUIRED_COMMANDS=(df free awk grep top systemctl curl)

    for cmd in "${REQUIRED_COMMANDS[@]}"; do
        if ! command -v "$cmd" &>/dev/null; then
            log_error "$cmd is not installed"
            exit 1
        fi
    done

    log_info "All dependencies are installed"
}

#############################################
# CPU Monitoring
#############################################

check_cpu_usage() {
    log_info "Checking CPU usage"

    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')
    CPU_INT=${CPU_USAGE%.*}

    echo "CPU Usage : ${CPU_USAGE}%"

    if [ "$CPU_INT" -gt "$CPU_THRESHOLD" ]; then
        log_warn "CPU usage exceeded threshold: ${CPU_USAGE}%"
    else
        log_info "CPU usage is normal: ${CPU_USAGE}%"
    fi
}

#############################################
# Memory Monitoring
#############################################

check_memory_usage() {
    log_info "Checking memory usage"

    MEMORY_USAGE=$(free | awk '/Mem:/ {printf("%.2f", $3/$2 * 100)}')
    MEMORY_INT=${MEMORY_USAGE%.*}

    echo "Memory Usage : ${MEMORY_USAGE}%"

    if [ "$MEMORY_INT" -gt "$MEM_THRESHOLD" ]; then
        log_warn "Memory usage exceeded threshold: ${MEMORY_USAGE}%"
    else
        log_info "Memory usage is normal: ${MEMORY_USAGE}%"
    fi
}

#############################################
# Disk Monitoring
#############################################

check_disk_usage() {
    log_info "Checking disk usage"

    df -h --output=source,pcent,target | tail -n +2 | while read -r line
    do
        USAGE=$(echo "$line" | awk '{print $2}' | tr -d '%')
        PARTITION=$(echo "$line" | awk '{print $3}')

        echo "$line"

        if [ "$USAGE" -gt "$DISK_THRESHOLD" ]; then
            log_warn "Disk usage exceeded threshold on $PARTITION : ${USAGE}%"
        fi
    done
}

#############################################
# Top Processes
#############################################

show_top_processes() {
    log_info "Displaying top memory consuming processes"

    ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -10
}

#############################################
# Service Monitoring
#############################################

check_services() {
    log_info "Checking important services"

    SERVICES=(ssh cron)

    for service in "${SERVICES[@]}"; do
        if systemctl is-active --quiet "$service"; then
            log_info "$service service is running"
        else
            log_warn "$service service is NOT running"
        fi
    done
}

#############################################
# Internet Connectivity Check
#############################################

check_network() {
    log_info "Checking internet connectivity"

    if curl -s https://www.google.com &>/dev/null; then
        log_info "Internet connectivity is working"
    else
        log_error "No internet connectivity"
    fi
}

#############################################
# System Information
#############################################

show_system_info() {
    log_info "Displaying system information"

    echo ""
    echo "========== SYSTEM INFORMATION =========="
    uname -a

    echo ""
    echo "========== UPTIME =========="
    uptime

    echo ""
    echo "========== CPU CORES =========="
    nproc

    echo ""
    echo "========== MEMORY =========="
    free -h

    echo ""
    echo "========== DISK =========="
    df -h
}

#############################################
# Main Function
#############################################

main() {
    show_banner
    check_dependencies
    show_system_info
    check_cpu_usage
    check_memory_usage
    check_disk_usage
    show_top_processes
    check_services
    check_network

    echo ""
    echo "========================================================="
    echo "Monitoring completed successfully"
    echo "========================================================="

    log_info "Monitoring script executed successfully"
}

#############################################
# Execute Main Function
#############################################

main
