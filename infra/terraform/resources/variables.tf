variable "branch" {}
variable "environment" {}

variable "gcp_project" {}
variable "gcp_region" {}
variable "gcp_service_name" {}
variable "gcp_suffix" {}

variable "min_instances" {}
variable "max_instances" {}

# GCP: Roles
variable "gcp_roles" {
  type = set(string)
  default = [
    "roles/pubsub.admin",
    "roles/run.admin",
    "roles/iam.serviceAccountUser",
    "roles/cloudbuild.serviceAgent",
    "roles/secretmanager.secretAccessor",
  ]
}
