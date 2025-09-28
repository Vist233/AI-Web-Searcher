Python MCP Server Scaffold

This folder contains a minimal Python-based MCP server scaffold designed for a search-orchestration tool. It avoids core logic and focuses on clear interfaces and placeholders.

Structure
- mcp_app/__main__.py: Entrypoint to run as module
- mcp_app/server.py: MCP server using FastMCP; exposes `search` tool and calls `fetch_page` when with_content=True
- mcp_app/schemas.py: Pydantic models for inputs/outputs
- mcp_app/orchestrator/pipeline.py: Orchestration stub (dispatch small models → rank by large model)
- mcp_app/search/providers/base.py: Provider interface for search
- mcp_app/search/providers/google.py: Placeholder provider (implement your own search; no content fetching here)
- mcp_app/workers/small_model_worker.py: Small model worker stubs
- mcp_app/workers/ranker.py: Ranking (large model) stub
- mcp_app/utils/config.py: Config/env helpers

Run (in MCP client)
- Command: `python`
- Args: `-m mcp_app`

Local quick test (no client)
- `python -m mcp_app` (this starts the MCP server over stdio)

Modes
- without content: provider returns metadata-only results (title/url/snippet)
- with content: server calls `fetch_page(url)` to enrich candidates with `content`

Notes
- Core logic is intentionally left as TODOs.
- Implement the Google provider yourself (do not rely on sample file import).
