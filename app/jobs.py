import httpx
import requests

def fetch_jobs() -> list[dict]:
    # Call API
    url = 'https://www.arbeitnow.com/api/job-board-api'
    response = httpx.get(url)
    response.raise_for_status()

    # Get JSON
    data = response.json()

    # Return jobs
    return data["data"]


def filter_jobs(jobs: list[dict]) -> list[dict]:
    # Filter jobs based on your criteria
    filtered_jobs = []

    for job in jobs:
        job_keywords = ["developer", "engineer", "dev", "python", "backend"]
        if any(keyword in job["title"].lower()for keyword in job_keywords):
            filtered_jobs.append(job)

    return filtered_jobs