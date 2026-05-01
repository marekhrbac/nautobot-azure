variable "vnets" {
  type = map(object({
    address_space       = string
    location            = string
    resource_group = string
  }))
}


