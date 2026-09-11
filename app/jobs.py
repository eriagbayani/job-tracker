import asyncio

from app.models import Job
from app.sources.arbeitnow import fetch_arbeitnow_jobs
from app.sources.jobicy import fetch_jobicy_jobs


async def fetch_all_jobs() -> list[Job]:
    # call Arbeitnow for jobs
    arbeitnow_jobs = fetch_arbeitnow_jobs()

    # call Jobicy  for jobs
    jobicy_jobs = fetch_jobicy_jobs()

    # gather both
    results = await asyncio.gather(arbeitnow_jobs, jobicy_jobs)

    # return combined list
    all_jobs = []

    for job_list in results:
        for job in job_list:
            all_jobs.append(job)
    return all_jobs


def filter_jobs(jobs: list[Job]) -> list[Job]:
    # Filter jobs based on your criteria
    filtered_jobs = []
    job_keywords = ["developer", "engineer", "dev", "python", "backend"]
    
    for job in jobs:
        if any(keyword in job.title.lower() for keyword in job_keywords):
            filtered_jobs.append(job)

    return filtered_jobs