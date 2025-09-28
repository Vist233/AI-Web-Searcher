from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


class SearchInput(BaseModel):
    query: str
    top_k: int = Field(default=5, ge=1, le=20)
    pages: int = Field(default=3, ge=1, le=10)
    lang: str = Field(default="en")
    region: Optional[str] = None
    timeout_s: Optional[int] = 30
    with_content: bool = False


class Candidate(BaseModel):
    title: str
    url: HttpUrl
    snippet: Optional[str] = None
    source: Optional[str] = None  # provider/worker name
    score: Optional[float] = None
    reason: Optional[str] = None
    content: Optional[str] = None  # optional raw page content when with_content=True


class SearchResponse(BaseModel):
    query: str
    results: List[Candidate] = Field(default_factory=list)
    used_providers: List[str] = Field(default_factory=list)
    latency_ms: Optional[int] = None
    note: Optional[str] = None


class FetchResponse(BaseModel):
    query: str
    results: List[Candidate] = Field(default_factory=list)
    latency_ms: Optional[int] = None
    note: Optional[str] = None
