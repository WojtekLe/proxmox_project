variable "proxmox_token_id" {
  sensitive = true
}

variable "proxmox_token_secret" {
  sensitive = true
}

variable "proxmox_url" {
  type = string
}

variable "vms" {
  type = list(object({
    project  = string
    owner    = string
    template = string
    cpu      = number
    memory   = number
    disk     = number
    vm_id    = number
  }))
}
