terraform {
  cloud {
    organization = "tfo-apj-demos"
    workspaces {
      name    = "import-demo-create-vms"
      project = "Demo Better Together Project"
    }
  }
  required_providers {
    vsphere = {
      source  = "hashicorp/vsphere"
      version = "~> 2.0"
    }
  }
}