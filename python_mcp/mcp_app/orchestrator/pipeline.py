from __future__ import annotations

import time
from typing import List

from ..schemas import Candidate, SearchInput, SearchResponse


def orchestrate(params: SearchInput, initial_candidates: list[Candidate] | None = None) -> SearchResponse:
    """
    Orchestration stub.

    Intended flow (to be implemented):
    1) Receive initial candidates from server layer (already searched; may include content)
    2) Distribute to small-model workers (parallel)
    3) Aggregate candidates and send to large-model ranker
    4) Return ranked, filtered list
    """
    t0 = time.time()

    # Placeholder: pass-through initial candidates (if any) and return
    candidates: List[Candidate] = list(initial_candidates or [])
    used_providers: List[str] = []
    
    

    latency_ms = int((time.time() - t0) * 1000)
    return SearchResponse(
        query=params.query,
        results=candidates,
        used_providers=used_providers,
        latency_ms=latency_ms,
        note=(
            "This is a scaffold. Implement provider calls, small-model workers, and ranker in orchestrator."
        ),
    )


from agno.agent import Agent
from agno.models.dashscope import DashScope
from pydantic import BaseModel


class searchResult(BaseModel):
    OrderNum: int
    title: str
    url: str
    abstract: str
    content: str

class searchResult(BaseModel):
    OrderNum: int
    title: str
    url: str
    abstract: str
    content: str


littleAgent = Agent(
    model=DashScope(id="qwen-flash"),
    markdown=False,
)

biggerAgent = Agent(
    model=DashScope(id="qwen-plus"),
    markdown=False,
)

if __name__ == "__main__":
    littleAgent.print_response("Share a 2 sentence horror story.")