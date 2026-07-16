
resource "proxmox_virtual_environment_vm" "vm" {

  name      = var.project
  node_name = "pve"

  clone {
    vm_id = var.vm_id
  }

  cpu {
    cores = var.cpu
  }

  memory {
    dedicated = var.memory
  }
}
