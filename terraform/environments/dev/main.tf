
resource "proxmox_virtual_environment_vm" "vm" {

  for_each = {
    for vm in var.vms : vm.vm_id => vm
  }

  name      = each.value.project
  node_name = "pve"

  clone {
    vm_id = each.value.vm_id
  }

  agent {
    enabled = true
  }

  cpu {
    cores = each.value.cpu
    type = "host"
  }

  memory {
    dedicated = each.value.memory
  }
}