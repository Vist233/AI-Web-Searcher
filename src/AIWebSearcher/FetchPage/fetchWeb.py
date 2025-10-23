import requests
from html.parser import HTMLParser
from urllib.parse import urljoin
from typing import Optional

try:
    import trafilatura
except ImportError as e:
    raise ImportError(
        "This function requires 'trafilatura'. Install with: pip install trafilatura requests"
    ) from e


def extract_text_from_url(
    url: str,
    *,
    follow_pagination: bool = True,
    pagination_limit: int = 3,
    timeout: float = 10.0,
    user_agent: Optional[str] = None,
) -> str:
    """
    Extract readable text from a webpage (optionally following rel="next" pagination).

    Implementation details:
    - Fetch HTML using requests.
    - Use trafilatura.extract to extract clean text; fall back to raw HTML if extraction fails.

    Parameters:
      - url: Target webpage URL.
      - follow_pagination: Whether to follow rel="next" pagination links.
      - pagination_limit: Maximum pagination depth (minimum 1).
      - timeout: HTTP request timeout in seconds.
      - user_agent: Custom User-Agent string; if not provided a common browser UA is used.

    Returns:
      - The concatenated plain text with blank lines between paginated pages; returns an
        empty string if no usable text is found.
    """

    class _RelLinkParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.href: Optional[str] = None

        def handle_starttag(self, tag, attrs):
            if self.href:
                return
            attr = {k.lower(): v for k, v in attrs}
            rel_attr = (attr.get("rel") or "").lower().split()
            if "next" in rel_attr:
                self.href = attr.get("href")

    def _find_rel_next(html: str) -> Optional[str]:
        try:
            parser = _RelLinkParser()
            parser.feed(html)
            return parser.href
        except Exception:
            return None

    headers = {
        "User-Agent": user_agent
        or (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        )
    }

    texts: list[str] = []
    visited = set()
    current = url

    for _ in range(max(1, int(pagination_limit))):
        if current in visited:
            break
        visited.add(current)

        resp = requests.get(current, headers=headers, timeout=timeout)
        resp.raise_for_status()
        raw_html = resp.text

        extracted = trafilatura.extract(
            raw_html,
            include_comments=False,
            include_tables=False,
        )
        clean_text = extracted.strip() if extracted else raw_html.strip()
        if clean_text:
            texts.append(clean_text)

        if not follow_pagination:
            break

        next_href = _find_rel_next(raw_html)
        if not next_href:
            break
        current = urljoin(current, next_href)

    return ("\n\n".join(texts)).strip()

def filter_extracted_text(   
    url: str,
    *,
    follow_pagination: bool = True,
    pagination_limit: int = 3,
    timeout: float = 10.0,
    user_agent: Optional[str] = None,
    regular_expressions: Optional[list[str]] = None,
) -> str:
    """
    Extract and filter readable text from a webpage (optionally following rel="next" pagination).

    Implementation details:
    - Fetch HTML using requests.
    - Use trafilatura.extract to extract clean text; fall back to raw HTML if extraction fails.
    - Use regular expressions to filter the extracted text.

    Parameters:
      - url: Target webpage URL.
      - follow_pagination: Whether to follow rel="next" pagination links.
      - pagination_limit: Maximum pagination depth (minimum 1).
      - timeout: HTTP request timeout in seconds.
      - user_agent: Custom User-Agent string; if not provided a common browser UA is used.
      - regular_expressions: List of regex patterns used to filter text; if None or empty,
        no filtering is performed.
    """
    import re

    text = extract_text_from_url(
        url,
        follow_pagination=follow_pagination,
        pagination_limit=pagination_limit,
        timeout=timeout,
        user_agent=user_agent,
    )

    if not regular_expressions:
        return text

    patterns = [re.compile(pattern) for pattern in regular_expressions]
    filtered_lines = [
        line for line in text.splitlines()
        if any(pattern.search(line) for pattern in patterns)
    ]

    return "\n".join(filtered_lines).strip()

