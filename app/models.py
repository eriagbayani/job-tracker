from pydantic import BaseModel, HttpUrl


class Job(BaseModel):
    slug: str
    company_name: str
    title: str
    description: str
    remote: bool
    url: HttpUrl
    tags: list[str]
    job_types: list[str]
    location: str
    created_at: int