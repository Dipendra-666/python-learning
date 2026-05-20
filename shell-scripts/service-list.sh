#!/bin/bash

###############################################################################
# Author: Dipendra Rayamajhi
# Version: v0.0.1
#
# Script Name: azure_resource_list.sh
#
# Description:
# This script automates the process of listing Azure resources using
# Azure CLI. It helps DevOps engineers and cloud administrators quickly
# view cloud resources directly from the terminal without opening the
# Azure Portal.
#
# Supported Azure Resources:
# 1. Virtual Machines (vm)
# 2. Storage Accounts (storage)
# 3. Virtual Networks (vnet)
# 4. Network Security Groups (nsg)
# 5. AKS Clusters (aks)
# 6. Azure SQL Servers (sql)
# 7. Function Apps (function)
# 8. Cosmos DB Accounts (cosmosdb)
# 9. All Resources (all)
#
# Requirements:
# - Azure CLI must be installed
# - User must be authenticated using:
#       az login
#
# Usage:
# ./azure_resource_list.sh <resource_type>
#
# Examples:
# ./azure_resource_list.sh vm
# ./azure_resource_list.sh storage
# ./azure_resource_list.sh all
#
# Output Format:
# Resources are displayed in table format for better readability.
#
# Exit Codes:
# 0 -> Success
# 1 -> Invalid arguments / authentication failure / unsupported resource
#
###############################################################################

# ==========================
# Argument Validation
# ==========================

if [ $# -ne 1 ]; then
    echo "ERROR: Invalid number of arguments."
    echo ""
    echo "Usage:"
    echo "./azure_resource_list.sh <resource_type>"
    echo ""
    echo "Example:"
    echo "./azure_resource_list.sh vm"
    exit 1
fi

# ==========================
# Variables
# ==========================

resource_type=$(echo "$1" | tr '[:upper:]' '[:lower:]')

# ==========================
# Check Azure CLI
# ==========================

if ! command -v az &> /dev/null; then
    echo "ERROR: Azure CLI is not installed."
    echo "Install Azure CLI and try again."
    exit 1
fi

# ==========================
# Check Azure Authentication
# ==========================

if ! az account show &> /dev/null; then
    echo "ERROR: You are not logged into Azure."
    echo "Run the following command first:"
    echo "az login"
    exit 1
fi

# ==========================
# Resource Listing Section
# ==========================

case $resource_type in

    vm)
        echo "Listing Azure Virtual Machines..."
        az vm list --output table
        ;;

    storage)
        echo "Listing Azure Storage Accounts..."
        az storage account list --output table
        ;;

    vnet)
        echo "Listing Azure Virtual Networks..."
        az network vnet list --output table
        ;;

    nsg)
        echo "Listing Azure Network Security Groups..."
        az network nsg list --output table
        ;;

    aks)
        echo "Listing Azure Kubernetes Service (AKS) Clusters..."
        az aks list --output table
        ;;

    sql)
        echo "Listing Azure SQL Servers..."
        az sql server list --output table
        ;;

    function)
        echo "Listing Azure Function Apps..."
        az functionapp list --output table
        ;;

    cosmosdb)
        echo "Listing Azure Cosmos DB Accounts..."
        az cosmosdb list --output table
        ;;

    all)
        echo "========================================="
        echo "Listing All Azure Resources"
        echo "========================================="

        echo ""
        echo "Virtual Machines:"
        az vm list --output table

        echo ""
        echo "Storage Accounts:"
        az storage account list --output table

        echo ""
        echo "Virtual Networks:"
        az network vnet list --output table

        echo ""
        echo "Network Security Groups:"
        az network nsg list --output table

        echo ""
        echo "AKS Clusters:"
        az aks list --output table

        echo ""
        echo "Azure SQL Servers:"
        az sql server list --output table

        echo ""
        echo "Function Apps:"
        az functionapp list --output table

        echo ""
        echo "Cosmos DB Accounts:"
        az cosmosdb list --output table
        ;;

    *)
        echo "ERROR: Unsupported resource type."
        echo ""
        echo "Supported resource types:"
        echo "vm"
        echo "storage"
        echo "vnet"
        echo "nsg"
        echo "aks"
        echo "sql"
        echo "function"
        echo "cosmosdb"
        echo "all"
        exit 1
        ;;
esac

# ==========================
# Script Completion Message
# ==========================

echo ""
echo "Script execution completed successfully."