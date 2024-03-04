# GCP: General
variable "gcp_project" {
  type        = string
  description = "The project ID to create the application under"
  default     = "angular-box-415904"
}

variable "gcp_region" {
  type        = string
  description = "The location region to serve the app from"
  default     = "us-central1"
}

variable "gcp_zone" {
  type        = string
  description = "The location zone to serve the app from"
  default     = "us-central1-c"
}

variable "gcp_suffix" {
  type        = string
  description = "Resource suffix"
  default     = "-dev"
}

## Environment
variable "environment" {
  type        = string
  description = "Environment"
  default     = "development"
}

variable "branch" {
  type        = string
  description = "Branch"
  default     = "dev"
}

## Project
variable "gcp_service_name" {
  type        = string
  description = "Service name"
  default     = "example-api"
}

variable "min_instances" {
  type        = number
  description = "Min instances"
  default     = 0
}

variable "max_instances" {
  type        = number
  description = "Max instances"
  default     = 2
}
