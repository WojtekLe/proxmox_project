
resource "proxmox_virtual_environment_vm" "vm" {

  for_each = {
    for index, vm in var.vms : index => vm
  }

  name      = "${each.value.project}-${each.key + 1}"
  node_name = "pve"

  description = "Project ${each.value.project} with template ${each.value.template}"

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