import httpx
import requests
from app.models import Job

def fetch_jobs() -> list[Job]:
    # Call API
    url = 'https://www.arbeitnow.com/api/job-board-api'
    response = httpx.get(url)
    response.raise_for_status()

    # Get JSON
    data = response.json()

    # convert each dictionary into a Job
    jobs = []

    for job_data in data["data"]:
        job = Job(**job_data)
        jobs.append(job)

    # Return jobs
    return jobs


def filter_jobs(jobs: list[Job]) -> list[Job]:
    # Filter jobs based on your criteria
    filtered_jobs = []
    job_keywords = ["developer", "engineer", "dev", "python", "backend"]
    
    for job in jobs:
        if any(keyword in job.title.lower() for keyword in job_keywords):
            filtered_jobs.append(job)

    return filtered_jobs