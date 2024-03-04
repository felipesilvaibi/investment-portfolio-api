resource "google_cloudbuild_trigger" "trigger" {
  project  = var.gcp_project
  location = "global"

  name        = "${var.gcp_service_name}-trigger${var.gcp_suffix}"
  description = "Deploy ${var.gcp_service_name}${var.gcp_suffix}"

  service_account = google_service_account.service_account.id

  source_to_build {
    uri       = "https://github.com/felipesilvaibi/${var.gcp_service_name}"
    ref       = "refs/heads/${var.branch}"
    repo_type = "GITHUB"
  }

  git_file_source {
    path      = "infra/cloudbuild.yaml"
    uri       = "https://github.com/felipesilvaibi/${var.gcp_service_name}"
    revision  = "refs/heads/${var.branch}"
    repo_type = "GITHUB"
  }

  substitutions = {
    _SUFFIX        = var.gcp_suffix
    _SERVICE_NAME  = var.gcp_service_name
    _REGION        = var.gcp_region
    _ENVIRONMENT   = var.branch
    _MIN_INSTANCES = var.min_instances
    _MAX_INSTANCES = var.max_instances
    _SERVICE_URL   = google_cloud_run_service.service.status[0].url
  }

  depends_on = [
    google_project_iam_member.member,
    google_cloud_run_service.service
  ]
}
