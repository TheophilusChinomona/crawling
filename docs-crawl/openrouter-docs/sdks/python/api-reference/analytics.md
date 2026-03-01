Source: https://openrouter.ai/docs/sdks/python/api-reference/analytics

Analytics | OpenRouter Python SDK | OpenRouter | Documentation

Search

`/`

Ask AI

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

* + [Agentic Usage](/docs/sdks/agentic-usage)
* DevTools

  + [Overview](/docs/sdks/dev-tools/devtools)
* TypeScript SDK

  + [Overview](/docs/sdks/typescript/overview)
  + Call Model
  + API Reference
* Python SDK

  + [Overview](/docs/sdks/python/overview)
  + API Reference

Light

On this page

* [Overview](#overview)
* [Available Operations](#available-operations)
* [get\_user\_activity](#get_user_activity)
* [Example Usage](#example-usage)
* [Parameters](#parameters)
* [Response](#response)
* [Errors](#errors)

[Python SDK](/docs/sdks/python/overview)[API Reference](/docs/sdks/python/api-reference/analytics)

Analytics - Python SDK

Copy page

Analytics method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

(*analytics*)

Overview
--------

Analytics and usage endpoints

### Available Operations

* [get\_user\_activity](/docs/sdks/python/api-reference/analytics#get_user_activity) - Get user activity grouped by endpoint

get\_user\_activity
-------------------

Returns user activity data grouped by endpoint for the last 30 (completed) UTC days. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

```
|  |  |
| --- | --- |
| 1 | from openrouter import OpenRouter |
| 2 | import os |
| 3 |  |
| 4 | with OpenRouter( |
| 5 | api_key=os.getenv("OPENROUTER_API_KEY", ""), |
| 6 | ) as open_router: |
| 7 |  |
| 8 | res = open_router.analytics.get_user_activity(date_="2025-08-24") |
| 9 |  |
| 10 | # Handle response |
| 11 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `date_` | *Optional[str]* | ➖ | Filter by a single UTC date in the last 30 days (YYYY-MM-DD format). | 2025-08-24 |
| `retries` | [Optional[utils.RetryConfig]](/docs/sdks/models/utils/retryconfig.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.GetUserActivityResponse](/docs/sdks/python/api-reference/operations/getuseractivityresponse)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.ForbiddenResponseError | 403 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

Was this page helpful?

YesNo

[Previous](/docs/sdks/python/overview)[#### 

APIKeys - Python SDK

APIKeys method reference

Next](/docs/sdks/python/api-reference/apikeys)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)