#!/usr/bin/env bash
set -euo pipefail

# Delete the demo resource group used in samples
: "${AZ_RG:=rg-database-demo}"
az group delete --name "$AZ_RG" --yes --no-wait
