from __future__ import annotations

from typing import List

from ...schemas import Candidate
from .base import SearchProvider


class GoogleProvider(SearchProvider):
    """
    Placeholder Google search provider.

    Implement this using your preferred approach (e.g., code adapted
    from your GoogleSearchToolExample, Google CSE API, or a SERP API).

    The provider should return a list of Candidates with title/url/snippet.
    Do NOT fetch page content here; the server layer will optionally fetch
    content (with_content mode) via its own fetch function.
    """

    name = "google"

    def search(self, query: str, max_results: int, language: str = "en") -> List[Candidate]:
        # TODO: Implement actual search, returning metadata-only candidates.
        # Example structure:
        # return [Candidate(title="...", url="https://...", snippet="...", source=self.name)]
        return []

