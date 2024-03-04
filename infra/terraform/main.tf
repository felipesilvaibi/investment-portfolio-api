provider "google" {
  project = var.gcp_project
  region  = var.gcp_region
  zone    = var.gcp_zone
}

module "resources" {
  source = "./resources"

  environment = var.environment
  branch      = var.branch

  gcp_project = var.gcp_project
  gcp_region  = var.gcp_region
  gcp_suffix  = var.gcp_suffix

  gcp_service_name = var.gcp_service_name
  min_instances    = var.min_instances
  max_instances    = var.max_instances
}
