resource "google_service_account" "service_account" {
  project      = var.gcp_project
  account_id   = var.gcp_service_name
  display_name = "Service Account for ${var.gcp_service_name}"
}

resource "google_project_iam_member" "member" {
  for_each = var.gcp_roles

  project = var.gcp_project
  role    = each.key

  member = "serviceAccount:${google_service_account.service_account.email}"
}
