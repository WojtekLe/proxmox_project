# Developer Provisioning Platform

Infrastructure as Code platform for automated provisioning of developer environments on Proxmox using Terraform and Ansible.

## Goals

- Infrastructure as Code
- Reproducible environments
- Zero manual configuration
- GitOps workflow
- Fast disaster recovery

## Stack

- Proxmox
- Terraform
- Ansible
- GitHub Actions
- Ubuntu


## proxmox_project
Simple virtual machine in proxmox

### Cel biznesowy
1. Deweloper zgłasza potrzebę nowej maszyny.

2. W repozytorium pojawia się opis tej maszyny.

3. Pipeline uruchamia Terraform.

4. Proxmox tworzy VM z Cloud-Init.

5. Ansible konfiguruje system.

6. Po kilku minutach deweloper dostaje gotowy adres IP i może zaczynać pracę.

### Workflow

GitHub

↓

Terraform

↓

Ubuntu Template

↓

Cloud-Init

↓

VM

↓

Ansible

↓

Docker

↓

Developer

### Etap 0 – Architektura repozytorium

├── .github/
│   └── workflows/
│
├── docs/
│   ├── architecture.md
│   ├── decisions.md
│   └── roadmap.md
│
├── terraform/
│   ├── environments/
│   │   └── dev/
│   │       ├── main.tf
│   │       ├── variables.tf
│   │       ├── outputs.tf
│   │       └── terraform.tfvars.example
│   │
│   ├── modules/
│   │   └── proxmox-vm/
│   │
│   └── providers.tf
│
├── ansible/
│   ├── inventories/
│   │   └── dev/
│   │
│   ├── playbooks/
│   │   └── bootstrap.yml
│   │
│   └── roles/
│       ├── common/
│       ├── docker/
│       └── developer/
│
├── scripts/
│
├── .gitignore
├── README.md
└── LICENSE