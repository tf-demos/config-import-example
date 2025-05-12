import requests
import json
from dotenv import load_dotenv
import os
import urllib3

# Disable some warnings (not recommended but just for demo)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Import vcenter variables
load_dotenv()  # Loads from .env by default

vcenter_host = os.getenv("VCENTER_HOST")
vcenter_user = os.getenv("VCENTER_USERNAME")
vcenter_password = os.getenv("VCENTER_PASSWORD")

# The name of the resource pool:
resource_pool_name = "Demo Workloads"

# get session token
def get_vcenter_session(host, user, password) -> str:
    url = f"https://{host}/api/session"
    response = requests.post(url, auth=(user, password), verify=False)
    if response.status_code == 201: #201 means created. The session token gets created
        return response.json() # keep in mind this is a single string value
    else:
        raise Exception("Failed to get session token from vCenter")

# get resource pool id, just as an example filter. Could be anything else
def get_resource_pool_id(host, session_id, resource_pool_name) -> str:
    url = f"https://{host}/api/vcenter/resource-pool"
    headers = {'vmware-api-session-id': session_id}
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        resource_pools = response.json()
        for pool in resource_pools:
            if pool['name'] == resource_pool_name:
                return pool['resource_pool']
        raise Exception(f"Resource pool '{resource_pool_name}' not found")
    else:
        raise Exception("Failed to retrieve resource pools")
    
# get vms:
def get_vms_for_resource_pool(host, session_id, resource_pool_name) -> list:
    url = f"https://{host}/api/vcenter/vm"
    headers = {'vmware-api-session-id': session_id}
    respool_id = get_resource_pool_id(host, session_id, resource_pool_name)
    params = {'resource_pools' : respool_id}
    response = requests.get(url, headers=headers, params=params, verify=False)
    if response.status_code == 200:
        return response.json() 
    else:
        raise Exception("Failed to retrieve VM list")

# generate import blocks
def generate_import(vm_list, filter_string) -> str:
    """
    Generate import blocks for Terraform from a list of VMs.
    Applies a string filter for VM names.
    """
    #Optional for demo, apply filter:
    vm_list = [vm for vm in vm_list if filter_string in vm['name']]
    import_file = "# File genertated automatically by script\n"
    import_file += "# Always check the generated file or plan before running 'terraform apply'\n\n"

    try:
        for vm in vm_list:
            import_block = f"""import {{
  to = vsphere_virtual_machine.{vm['name']}
  id = {vm['vm']}
}}

"""
            import_file += import_block
        import_file += "# End of generated file\n"
        # create file for contents
        create_file(import_file, "../import-resources/imported.tf")
        return {"status": "success", "message": "File generated successfully", "file": import_file}
    
    except Exception as e:
        print("Error generating import file:", e)
        return {"status": "error", "message": "Error generating import file", "error": str(e)}

def create_file(contents, filename):
    """
    Create a file with the given contents.
    """
    try:
        with open(filename, 'w') as file:
            file.write(contents)
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating file '{filename}':", e)


if __name__ == "__main__":
    # Example usage
    try:
        session_token = get_vcenter_session(vcenter_host, vcenter_user, vcenter_password)
        vms = get_vms_for_resource_pool(vcenter_host, session_token, resource_pool_name)
        # generate import file:
        filter_string = "database"
        generate_import(vms, filter_string)
    except Exception as e:
        print("Error:", e)
