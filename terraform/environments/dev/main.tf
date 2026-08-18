
resource "proxmox_virtual_environment_vm" "vm" {

  for_each = {
    for index, vm in var.vms : index => vm
  }

  name      = "${each.value.project}_${each.key + 1}"
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