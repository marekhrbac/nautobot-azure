locals {
  resource_groups = {
    "rg-germany" = azurerm_resource_group.rg_germany
    "rg-spain"   = azurerm_resource_group.rg_spain
  }
}