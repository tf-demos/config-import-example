module "single-virtual-machine" {
  source  = "app.terraform.io/tfo-apj-demos/single-virtual-machine/vsphere"
  version = "1.2.0"

  for_each         = var.vm_config
  hostname         = each.value.hostname
  ad_domain        = each.value.ad_domain
  backup_policy    = each.value.backup_policy
  environment      = each.value.environment
  os_type          = each.value.os_type
  security_profile = each.value.security_profile
  site             = each.value.site
  size             = each.value.size
  storage_profile  = each.value.storage_profile
  tier             = each.value.tier
}