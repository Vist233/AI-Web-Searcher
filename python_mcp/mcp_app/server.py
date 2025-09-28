from __future__ import annotations

from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from .schemas import SearchInput, SearchResponse, Candidate
# Orchestrator stub (no core logic implemented)
from .orchestrator.pipeline import orchestrate
from .search.providers.google import GoogleProvider


mcp = FastMCP("searcher", version="0.1.0", description="Modular Search with LLMs")


def fetch_page(url: str, timeout_s: int | None = 10) -> str:
    """Fetch a single web page and return raw text content.

    NOTE: This is a simple implementation. You can replace with httpx + better HTML-to-text.
    """
    try:
        import requests
        from bs4 import BeautifulSoup

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            )
        }
        resp = requests.get(url, headers=headers, timeout=timeout_s)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, "html.parser")
        return soup.get_text(" ", strip=True)
    except Exception:
        return ""


@mcp.tool()
def search(
    query: str,
    top_k: int = 5,
    pages: int = 3,
    lang: str = "en",
    region: Optional[str] = None,
    timeout_s: Optional[int] = 10,
    with_content: bool = False,
) -> Dict[str, Any]:
    """
    Search orchestration entrypoint.
    - Dispatch to multiple small-model workers per page
    - Aggregate and send to a large-model ranker
    - Return structured, ranked results

    Note: This is a scaffold; core logic lives in orchestrator.orchestrate and is intentionally not implemented here.
    """
    params = SearchInput(
        query=query,
        top_k=top_k,
        pages=pages,
        lang=lang,
        region=region,
        timeout_s=timeout_s,
        with_content=with_content,
    )
    # 1) Provider search (metadata only)
    provider = GoogleProvider()
    base_candidates: list[Candidate] = provider.search(
        query=query, max_results=pages, language=lang
    )

    # 2) Optional: fetch page content here
    if with_content:
        enriched: list[Candidate] = []
        for c in base_candidates:
            content = fetch_page(c.url, timeout_s=timeout_s)
            enriched.append(Candidate(**c.model_dump(), content=content))
        base_candidates = enriched

    # 3) Delegate to pipeline orchestrator (workers + ranker are TODOs)
    result: SearchResponse = orchestrate(params, initial_candidates=base_candidates)
    return result.model_dump()

def main() -> None:
    mcp.run()
