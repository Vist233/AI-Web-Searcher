from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from ...schemas import Candidate


class SearchProvider(ABC):
    name: str = "provider"

    @abstractmethod
    def search(self, query: str, max_results: int, language: str = "en") -> List[Candidate]:
        """Return a list of candidates from a SERP provider."""
        raise NotImplementedError

