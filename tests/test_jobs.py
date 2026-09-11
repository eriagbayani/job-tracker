from unittest.mock import AsyncMock, patch

import pytest
from pydantic import ValidationError

from app.jobs import fetch_all_jobs, filter_jobs
from app.models import Job


def make_job(title: str) -> Job:
    return Job(
        slug="test-job-123",
        company_name="Test Company",
        title=title,
        description="Test description",
        remote=True,
        url="https://example.com/test-job",
        tags=["python"],
        job_types=["Full time"],
        location="Remote",
        created_at=1788776408,
    )


def test_filter_jobs_matches_keywords():
    jobs = [
        make_job("Python Developer"),
        make_job("Marketing Manager"),
        make_job("Backend Engineer"),
    ]

    result = filter_jobs(jobs)

    assert len(result) == 2
    assert result[0].title == "Python Developer"
    assert result[1].title == "Backend Engineer"


def test_filter_jobs_is_case_insensitive():
    jobs = [
        make_job("PYTHON DEVELOPER"),
    ]

    result = filter_jobs(jobs)

    assert len(result) == 1


def test_filter_jobs_excludes_non_matching_jobs():
    jobs = [
        make_job("Marketing Manager"),
        make_job("Data Analyst"),
    ]

    result = filter_jobs(jobs)

    assert len(result) == 0


def test_job_model_validates_data():
    job = make_job("Python Developer")

    assert job.title == "Python Developer"
    assert job.remote is True


def test_job_model_rejects_invalid_url():
    with pytest.raises(ValidationError):
        Job(
            slug="test-job-123",
            company_name="Test Company",
            title="Python Developer",
            description="Test description",
            remote=True,
            url="not-a-valid-url",
            tags=["python"],
            job_types=["Full time"],
            location="Remote",
            created_at=1788776408,
        )


@pytest.mark.asyncio
async def test_fetch_all_jobs_combines_sources():
    arbeitnow_jobs = [
        make_job("Python Developer"),
        make_job("Backend Engineer"),
    ]

    jobicy_jobs = [
        make_job("Software Engineer"),
    ]

    with (
        patch(
            "app.jobs.fetch_arbeitnow_jobs",
            new=AsyncMock(return_value=arbeitnow_jobs),
        ),
        patch(
            "app.jobs.fetch_jobicy_jobs",
            new=AsyncMock(return_value=jobicy_jobs),
        ),
    ):
        result = await fetch_all_jobs()

    assert len(result) == 3
    assert result[0].title == "Python Developer"
    assert result[1].title == "Backend Engineer"
    assert result[2].title == "Software Engineer"