import httpx

from app.models import Job


async def fetch_arbeitnow_jobs() -> list[Job]:
    # Call API
    url = 'https://www.arbeitnow.com/api/job-board-api'
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        res.raise_for_status()

    # get json
    data = res.json()

    # conv each dict into a Job
    jobs = []

    for job_data in data["data"]:
        job = Job(**job_data)
        jobs.append(job)
    
        # Return jobs
    return jobs
