# Deprecation Notice: DashScope → Alibaba Cloud Bailian API Migration


## Description
The current implementation of `agno.models.dashscope.DashScope` depends on the legacy DashScope API (`https://dashscope-intl.aliyuncs.com/compatible-mode/v1`), which is no longer active.  
Alibaba Cloud has migrated all DashScope services to **Bailian (Alibaba Cloud Bailian / Model Studio - Bailian)**.  
As a result, any existing code using DashScope fails authentication and cannot access Qwen models.

Example error:

```bash
401 Unauthorized: Incorrect API key provided
```

the API key is rejected because DashScope has been deprecated.

## Expected Behavior

Agno should:

1. Support the new **Bailian** API endpoint and authentication mechanism.

2. Accept a new environment variable such as `BAILIAN_API_KEY`, while optionally supporting `DASHSCOPE_API_KEY` for backward compatibility.

3. Provide a transparent migration path for users currently using the `DashScope` model.

## Actual Behavior

- The `DashScope` client still calls the old DashScope endpoint.

- All requests return `401 Invalid API key`.

- The `qwen-plus` and other Qwen models cannot be accessed.

## Environment

- OS: macOS

- Python: 3.13

- Agno version: latest

- Model: `qwen-plus`

## Suggested Fix

1. Implement a new adapter class, e.g. `agno.models.bailian`, for the Alibaba Cloud Bailian API.

2. Update `DashScope` to detect if Bailian configuration is present, and automatically route requests to the new endpoint.

3. Update environment variable naming and documentation:
   
   - From: `export DASHSCOPE_API_KEY=***`
   
   - To: `export BAILIAN_API_KEY=***`

4. Update the official documentation and examples to use Bailian.

5. Add backward compatibility and basic integration tests.

Reference:

- [Alibaba Cloud Bailian Documentation](https://www.alibabacloud.com/help/en/model-studio/use-qwen-by-calling-api)

- [Bailian API Reference on Alibaba Cloud](https://api.aliyun.com/api-tools/sdk/bailian?version=2023-12-29)

## Contribution

I am willing to submit a pull request to:

- Implement `agno.models.bailian`

- Update `DashScope` for compatibility

- Revise documentation and examples accordingly

Please confirm whether this migration direction aligns with Agno’s roadmap before I begin.
