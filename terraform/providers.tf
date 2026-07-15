terraform {
  required_providers {
    proxmox = {
      source  = "bpg/proxmox"
      version = "~> 0.84"
    }
  }
}

provider "proxmox" {
  endpoint = var.proxmox_url

  api_token = "${var.proxmox_token_id}=${var.proxmox_token_secret}"

  insecure = true
}
