import asyncio

from app.jobs import fetch_all_jobs, filter_jobs


async def main() -> None:

    print("========================================")
    print("          JOB HUNTER V2             ")
    print("========================================")

    jobs = await fetch_all_jobs()
    print(f"Found {len(jobs)} jobs")

    matched_jobs = filter_jobs(jobs)
    print("Matching Jobs: ")

    for i, job in enumerate(matched_jobs, start=1):
        print(f"{i}. {job.title}")
        print(f"   Company: {job.company_name}")
        print(f"   created_at: {job.created_at}")
        print(f"   Location: {job.location}")
        print(f"   Job Type: {', '.join(job.job_types)}")
        print(f"   URL: {job.url}")
        print()


if __name__ == "__main__":
    asyncio.run(main())