from fastmcp import FastMCP
from FetchPage.fetchWeb import filter_extracted_text
from typing import Optional
from WebSearch.baiduSearchTool import BaiduSearchTools

mcp = FastMCP("Search Tools")

# @mcp.tool
# def add(a: int, b: int) -> int:
#     """Add two numbers"""
#     return a + b

@mcp.tool
def search_baidu(query: str, max_results: int = 5, language: str = "zh") -> str:
    """Execute Baidu search and return results

    Args:
        query (str): Search keyword
        max_results (int, optional): Maximum number of results to return, default 5
        language (str, optional): Search language, default Chinese

    Returns:
        str: A JSON formatted string containing the search results (Title, URL, abstract).
    """
    tool = BaiduSearchTools()
    return tool.baidu_search(query, max_results=max_results, language=language)

@mcp.tool
def extractTextFromUrl(
    url: str,
    *,
    follow_pagination: bool = True,
    pagination_limit: int = 3,
    timeout: float = 10.0,
    user_agent: Optional[str] = None,
    regular_expressions: Optional[list[str]] = None,
) -> str:
    """
    提取并过滤指定网址的整页可读文本（可选跟随 rel=\"next\" 分页），实现方式与项目一致：
    - 使用 requests 抓取 HTML
    - 使用 trafilatura.extract 提取纯文本，失败时回退到原始 HTML 文本
    - 使用正则表达式过滤文本

    参数:
      - url: 目标网页
      - follow_pagination: 是否跟随 rel=\"next\" 的分页链接
      - pagination_limit: 最多跟随的分页深度（至少 1）
      - timeout: 每次 HTTP 请求超时时间（秒）
      - user_agent: 自定义 UA；不提供则使用常见浏览器 UA
      - regular_expressions: 用于过滤文本的正则表达式列表；如果为 None 或空列表，则不进行过滤
      """
    return filter_extracted_text(
        url,
        follow_pagination=follow_pagination,
        pagination_limit=pagination_limit,
        timeout=timeout,
        user_agent=user_agent,
        regular_expressions=regular_expressions,
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")

