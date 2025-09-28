from __future__ import annotations

from typing import List

from ..schemas import Candidate


class SmallModelWorker:
    """Stub for a small model worker that extracts structured candidates from page content."""

    def __init__(self, name: str):
        self.name = name

    def infer(self, page_text: str) -> List[Candidate]:
        """
        TODO: Implement small model inference that extracts top entities/answers from a page.
        Return a list of Candidate objects with reason/score if applicable.
        """
        return []

