# TF Import Demo
This repo contains an example of how to import resources in Terraform with the [vSphere](https://registry.terraform.io/providers/hashicorp/vsphere/latest/docs) provider. 

The goal is to automatically generate a file with the required `import` blocks for Terraform to import resources. The [`import.py`](./python/import.py) is a Python script that communicates with the vCenter API and returns a list of VMs according to a specified filter string.

## How to use this

### 1. Prerequisites
- Python: version 3.13.3 was used for this demo.
- Terraform: version used: 1.11.3

### 2. Clone this repo
```bash
git clone 
```

### Create a virtual environment:
```bash
cd 
```
### Install the requirements:
