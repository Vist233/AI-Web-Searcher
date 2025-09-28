MCP 搜索编排（Python）

本仓库提供一个 Python 版的 Model Context Protocol (MCP) 服务端脚手架，用于“搜索 → 三个小模型并行抽取 → 大模型排序过滤”的编排场景。核心逻辑留空，便于按你的方案实现。

目录结构

- `python_mcp/mcp_app/server.py`：MCP 入口，暴露 `search_orchestrator` 工具
- `python_mcp/mcp_app/schemas.py`：Pydantic 入参/出参模型（`SearchInput`、`Candidate`、`SearchResponse`）
- `python_mcp/mcp_app/orchestrator/pipeline.py`：编排层占位（待实现：搜索→抓取→3小模型→大模型排序）
- `python_mcp/mcp_app/search/providers/base.py`：搜索 Provider 接口
- `python_mcp/mcp_app/search/providers/google.py`：搜索 Provider 占位（你来实现，不在此适配示例文件）
- `python_mcp/mcp_app/workers/small_model_worker.py`：小模型 Worker 占位
- `python_mcp/mcp_app/workers/ranker.py`：大模型排序器占位
- `mcp.python.example.json`：MCP 客户端示例配置
- `GoogleSearchToolExample.py`：你的 Google 搜索工具

使用方式

- 在 MCP 客户端中配置：参考 `mcp.python.example.json`（`command: python`，`args: -m mcp_app`，`workingDirectory: python_mcp`）
- 本地启动（便于烟测）：在仓库根目录执行 `python -m mcp_app`（工作目录为 `python_mcp`）
- 依赖（按需安装）：`pip install mcp pydantic googlesearch-python pycountry`

工作流程（待你实现的核心）

- 搜索：通过 `search.providers` 选择 Provider（`google.py` 为占位，需要你实现）
- 抓取/解析：当 `with_content=true` 时由 `server.py` 中的 `fetch_page()` 进行抓取，并发可自行扩展
- 小模型分发：三个小模型并行抽取结构化候选（统一 `Candidate` Schema）
- 大模型排序：聚合候选，调用大模型过滤去重、排序，得到最终列表
- 返回：`SearchResponse`（含 `results`、`used_providers`、`latency_ms`）

开发提示

- 在 `orchestrator/pipeline.py` 串起 provider → 抓取 → 小模型 → ranker（保留推理实现为 TODO）
- 在 `workers/` 中实现三个小模型抽取逻辑；在 `ranker.py` 实现大模型排序
- 如需合规稳定的搜索源，可并行实现 CSE/Bing/Brave/Tavily provider 并通过配置切换

注意

- 本仓库已移除 TypeScript 版示例，专注于 Python MCP。
