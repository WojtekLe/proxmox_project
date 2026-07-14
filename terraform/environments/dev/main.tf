
resource "proxmox_virtual_environment_vm" "vm" {

  name = var.project

  cpu {
    cores = var.cpu
  }

  memory {
    dedicated = var.memory
  }

  disk {
    size = var.disk
  }
}