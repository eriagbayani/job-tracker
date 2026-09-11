from datetime import datetime

import httpx

from app.models import Job


async def fetch_jobicy_jobs() -> list[Job]:
    # call api
    url = 'https://jobicy.com/api/v2/remote-jobs'
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        res.raise_for_status()
    # get json
    data = res.json()
    # conv each dict into a Job
    jobs = []

    # loop through jobicy jobs
    for job_data in data["jobs"]:
        mapped_job = {
            "slug": job_data["jobSlug"],
            "company_name": job_data["companyName"],
            "title": job_data["jobTitle"],
            "description": job_data["jobDescription"],
            "remote": True,
            "url": job_data["url"],
            "tags": job_data["jobIndustry"],
            "job_types": job_data["jobType"],
            "location": job_data["jobGeo"],
            "created_at": int(
                datetime.fromisoformat(job_data["pubDate"]).timestamp()
            )
        }

        job = Job(**mapped_job)
        jobs.append(job)
    return jobs