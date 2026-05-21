#!/bin/bash

# CPU, Disk, Memory monitoring script
# Author: Dipendra Rayamajhi / DevOps team
# Version: 0.0.1

set -x
set -e
set -o pipefail

echo "===== Disk Usage ====="
df -h

echo "===== Memory Usage ====="
free -h

echo "===== CPU Cores ====="
nproc

echo "===== Azure Processes (PIDs) ====="
ps -ef | grep azure | grep -v grep | awk '{print $2}'