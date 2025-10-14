from agno.agent import Agent
from agno.models.dashscope import DashScope

agent = Agent(
    model=DashScope(id="qwen-plus", api_key="sk-b5ee4168837640b1af2695fa72ab41c5"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")

# Output:
# ERROR    API status error from OpenAI API: Error code: 401 - {'error': {'message': 'Incorrect API key provided. ', 'type':                
#          'invalid_request_error', 'param': None, 'code': 'invalid_api_key'}, 'request_id': 'cfa9183e-8836-999d-9aaf-c668c31fc1dc'}        
# WARNING  Attempt 1/1 failed: Incorrect API key provided.                                                                                  
# ERROR    Failed after 1 attempts. Last error using Qwen(qwen-plus)                                                                        
# ▰▰▰▱▱▱▱ Thinking...
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                        ┃
# ┃ Share a 2 sentence horror story.                                                                                                       ┃
# ┃                                                                                                                                        ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# Traceback (most recent call last):
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/agno/models/openai/chat.py", line 370, in invoke
#     provider_response = self.get_client().chat.completions.create(
#         model=self.id,
#         messages=[self._format_message(m) for m in messages],  # type: ignore
#         **self.get_request_params(response_format=response_format, tools=tools, tool_choice=tool_choice),
#     )
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/openai/_utils/_utils.py", line 286, in wrapper
#     return func(*args, **kwargs)
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/openai/resources/chat/completions/completions.py", line 1147, in create
#     return self._post(
#            ~~~~~~~~~~^
#         "/chat/completions",
#         ^^^^^^^^^^^^^^^^^^^^
#     ...<46 lines>...
#         stream_cls=Stream[ChatCompletionChunk],
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/openai/_base_client.py", line 1259, in post
#     return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
#                            ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/openai/_base_client.py", line 1047, in request
#     raise self._make_status_error_from_response(err.response) from None
# openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Incorrect API key provided. ', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_api_key'}, 'request_id': 'cfa9183e-8836-999d-9aaf-c668c31fc1dc'}

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/dashsp.py", line 10, in <module>
#     agent.print_response("Share a 2 sentence horror story.")
#     ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/agno/agent/agent.py", line 6988, in print_response
#     print_response(
#     ~~~~~~~~~~~~~~^
#         agent=self,
#         ^^^^^^^^^^^
#     ...<22 lines>...
#         **kwargs,
#         ^^^^^^^^^
#     )
#     ^
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/agno/utils/print_response/agent.py", line 526, in print_response
#     run_response = agent.run(
#         input=input,
#     ...<16 lines>...
#         **kwargs,
#     )
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/agno/agent/agent.py", line 1298, in run
#     raise last_exception
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/agno/agent/agent.py", line 1247, in run
#     response = self._run(
#         run_response=run_response,
#     ...<3 lines>...
#         response_format=response_format,
#     )
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/agno/agent/agent.py", line 775, in _run
#     model_response: ModelResponse = self.model.response(
#                                     ~~~~~~~~~~~~~~~~~~~^
#         messages=run_messages.messages,
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     ...<6 lines>...
#         send_media_to_model=self.send_media_to_model,
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/agno/models/base.py", line 216, in response
#     self._process_model_response(
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
#         messages=messages,
#         ^^^^^^^^^^^^^^^^^^
#     ...<5 lines>...
#         run_response=run_response,
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/agno/models/base.py", line 501, in _process_model_response
#     provider_response = self.invoke(
#         assistant_message=assistant_message,
#     ...<4 lines>...
#         run_response=run_response,
#     )
#   File "/Users/zhangyvjing/Library/CloudStorage/OneDrive-Personal/Code/search-mcp/.venv/lib/python3.13/site-packages/agno/models/openai/chat.py", line 410, in invoke
#     raise ModelProviderError(
#     ...<4 lines>...
#     ) from e
# agno.exceptions.ModelProviderError: Incorrect API key provided. 

# 由此可以发现
# https://docs.agno.com/concepts/models/dashscope
# DashScope

# Copy page

# Learn how to use DashScope models in Agno.

# Leverage DashScope’s powerful command models and more.
# DashScope supports a wide range of models
# We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:
# qwen-plus model is good for most use-cases.
# ​
# Authentication
# Set your DASHSCOPE_API_KEY environment variable. Get your key from here.

# Mac

# Windows

# Copy

# Ask AI
# export DASHSCOPE_API_KEY=***
# ​
# Example
# Use DashScope with your Agent:

# agent.py

# Copy

# Ask AI
# from agno.agent import Agent
# from agno.models.dashscope import DashScope

# agent = Agent(
#     model=DashScope(id="qwen-plus"),
#     markdown=True
# )

# # Print the response in the terminal
# agent.print_response("Share a 2 sentence horror story.")

# View more examples here.
# ​
# Parameters
# Parameter	Type	Default	Description
# id	str	"qwen-plus"	The id of the Qwen model to use
# name	str	"Qwen"	The name of the model
# provider	str	"Dashscope"	The provider of the model
# api_key	Optional[str]	None	The API key for DashScope (defaults to DASHSCOPE_API_KEY env var)
# base_url	str	"https://dashscope-intl.aliyuncs.com/compatible-mode/v1"	The base URL for the DashScope API
# enable_thinking	bool	False	Enable thinking process for reasoning models
# include_thoughts	Optional[bool]	None	Include thinking process in response (alternative parameter)
# thinking_budget	Optional[int]	None	Budget for thinking tokens in reasoning models
# DashScope extends the OpenAI-compatible interface and supports most parameters from the OpenAI model.
# ​
# Thinking Models
# DashScope supports reasoning models with thinking capabilities:

# Copy

# Ask AI
# from agno.agent import Agent
# from agno.models.dashscope import DashScope

# agent = Agent(
#     model=DashScope(
#         id="qwen-plus",
#         enable_thinking=True,
#         thinking_budget=5000
#     ),
#     markdown=True
# )
# 这个DashScope已经被弃用了，现在更新成为了阿里云百炼。请你写一个ISSUE来告诉Ango官方这个问题，并且最后提出我可以完成这个转换工作