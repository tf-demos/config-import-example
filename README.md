# TF Import Demo
This repo contains an example of how to import resources in Terraform with the [vSphere](https://registry.terraform.io/providers/hashicorp/vsphere/latest/docs) provider. 

The goal is to automatically generate a file with the required `import` blocks for Terraform to import resources. The [`import.py`](./python/import.py) is a Python script that communicates with the vCenter API and returns a list of VMs according to a specified filter string.

## How to use this

### 1. Prerequisites
- Python: version 3.13.3 was used for this demo.
- Terraform: version used: 1.11.3

### 2. Clone this repo
```bash
git clone https://github.com/tf-demos/config-import-example.git import-example
```

### 3. Update your vCenter API credentials
Update the `.env` file with the corresponding host, username and password to authenticate to vCenter. Once done, remove the `.example` from the file name:
```bash
cd import-example/python
# Update the .env file accordingly
mv .env.example .env
```

### 4. Create a virtual environment and install requirements:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### 5. Run the script
This script generates an `imported.tf` file with the necessary import blocks for Terraform. It retrieves a list of VMs for a specified resource pool in vCenter called "Demo Workloads", you can change that directly in the python code.

And additionally uses a "filter string" that filters the VMs to import according to the name. This parameter must be passed as a command line argument. For example, in this case the filter is `database`:

```bash
python import.py database
```

Upon successfully running the script, this will generate an `imported.tf` file inside [import-resource](./import-resource).

### 6. Check the imported resources:
```
cd ../import-resources
terraform plan
```

### 7. Use wisely
Once you have imported resources in Terraform you can manage them, modify them, and _destroy them_.

### 8. Cleanup
```
deactivate
```
