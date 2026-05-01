resource "azurerm_virtual_network" "vnets" {
  for_each = var.vnets

  name                = each.key
  address_space       = [each.value.address_space]
  location            = each.value.location
  resource_group_name = local.resource_groups[each.value.resource_group].name
}