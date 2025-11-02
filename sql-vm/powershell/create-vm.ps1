New-AzVM -ResourceGroupName rg-database-demo -Name sqlvm-demo `
  -Location eastus -Image 'MicrosoftSQLServer:SQL2019-WS2019:Enterprise:latest' `
  -AdminUsername azureuser -AdminPassword 'ChangeMe123!'
