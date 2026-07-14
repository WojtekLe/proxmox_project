variable "project" {
  type = string
}

variable "owner" {
  type = string
}

variable "template" {
  type = string
}

variable "cpu" {
  type = number
}

variable "memory" {
  type = number
}

variable "disk" {
  type = number
}

variable "proxmox_token_id" {
  sensitive = true
}

variable "proxmox_token_secret" {
  sensitive = true
}
