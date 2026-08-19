output "vms" {
  value = {
    for key, vm in proxmox_virtual_environment_vm.vm :
    key => {
      vm_id = vm.vm_id
      name  = vm.name
      ip    = vm.ipv4_addresses
    }
  }
}