import requests
import os
from pprint import pprint
import json

api_key = os.getenv("API_KEY")

url = "http://nautobot.msync.cz:8001"
prefix_path = "/api/ipam/prefixes/" 
location_path = "/api/ipam/prefix-location-assignments/"

full_prefix_path = url + prefix_path
full_location_path = url + location_path

get_prefix = requests.get(full_prefix_path, headers={"Authorization": f"Token {api_key}"})
get_location = requests.get(full_location_path, headers={"Authorization": f"Token {api_key}"})

vnet_dict = {}

for azure_prefix in get_prefix.json()["results"]:
    pprint(azure_prefix)
    if azure_prefix["custom_fields"]["is_vnet"]:
        vnet_name = azure_prefix["custom_fields"]["vnet"]
        vnet_rg = azure_prefix["custom_fields"]["resource_group"]
        vnet_prefix = azure_prefix["prefix"]
        
        for azure_location in get_location.json()["results"]:
            if vnet_prefix in azure_location["display"]:
                vnet_location = azure_location["display"].split(": ")[1]
                
        vnet_dict[vnet_name] = {
             "address_space": vnet_prefix,
             "location": vnet_location,
             "resource_group": vnet_rg
            }

data = {
    "vnets": vnet_dict
}

with open("nautobot_vnets.json", "w") as f:
    json.dump(data, f, indent=2)


