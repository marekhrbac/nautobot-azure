resource "azurerm_resource_group" "rg_germany" {
  location = "germanywestcentral"
  name     = "rg-germany"
}

resource "azurerm_resource_group" "rg_spain" {
  location = "spaincentral"
  name     = "rg-spain"
}