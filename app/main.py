from app.jobs import fetch_jobs, filter_jobs


def main() -> None:

    print("========================================")
    print("          JOB HUNTER V0             ")
    print("========================================")

    jobs = fetch_jobs()
    print(f"Found {len(jobs)} jobs")

    matched_jobs = filter_jobs(jobs)
    print("Matching Jobs: ")

    for i, job in enumerate(matched_jobs, start=1):
        print(f"{i}. {job['title']}")
        print(f"   Company: {job['company_name']}")
        print(f"   Location: {job['location']}")
        print(f"   Job Type: {', '.join(job['job_types'])}")
        print(f"   URL: {job['url']}")
        print()


if __name__ == "__main__":
    main()