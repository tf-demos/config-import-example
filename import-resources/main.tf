terraform {
  cloud {
    organization = "tfo-apj-demos"
    workspaces {
      project = "Demo Better Together Project"
      name    = "imported-resources"
    }
  }

  required_providers {
    vsphere = {
      source  = "hashicorp/vsphere"
      version = "~> 2.0"
    }
  }
}

# If running locally, fill out the required credentials to authenticate to vSphere:

# provider "vsphere" {
#   user           = var.vsphere_user
#   password       = var.vsphere_password
#   vsphere_server = var.vsphere_server
# }