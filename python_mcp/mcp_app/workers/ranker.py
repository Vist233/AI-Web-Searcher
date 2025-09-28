from __future__ import annotations

from typing import List

from ..schemas import Candidate


class Ranker:
    """Stub for a large-model ranker that merges and scores candidates."""

    def __init__(self, model_name: str | None = None):
        self.model_name = model_name or "llm-ranker"

    def rerank(self, candidates: List[Candidate], query: str, top_k: int) -> List[Candidate]:
        """
        TODO: Implement ranking/aggregation logic using a large model.
        """
        return candidates[:top_k]

