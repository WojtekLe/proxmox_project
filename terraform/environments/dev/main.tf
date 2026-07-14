
terraform {
  required_providers {
    proxmox = {
      source = "bpg/proxmox"
      version = "~> 0.84"
    }
  }
}


provider "proxmox" {
  endpoint = "https://pve:8006/api2/json"

  api_token = "${var.proxmox_token_id}=${var.proxmox_token_secret}"

  insecure = true
}

data "proxmox_virtual_environment_nodes" "nodes" {}

output "nodes" {
  value = data.proxmox_virtual_environment_nodes.nodes.names
}


# resource "proxmox_virtual_environment_vm" "vm" {

#   name = var.project

#   cpu {
#     cores = var.cpu
#   }

#   memory {
#     dedicated = var.memory
#   }

#   disk {
#     size = var.disk
#   }
# }