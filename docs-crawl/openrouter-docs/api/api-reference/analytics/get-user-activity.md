Source: https://openrouter.ai/docs/api/api-reference/analytics/get-user-activity

Get user activity grouped by endpoint | OpenRouter | Documentation

Search

`/`

Ask AI

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

* API Guides

  + [Overview](/docs/api/reference/overview)
  + [Streaming](/docs/api/reference/streaming)
  + [Embeddings](/docs/api/reference/embeddings)
  + [Limits](/docs/api/reference/limits)
  + [Authentication](/docs/api/reference/authentication)
  + [Parameters](/docs/api/reference/parameters)
  + [Errors and Debugging](/docs/api/reference/errors-and-debugging)
  + Responses API
* API Reference

  + Responses
  + OAuth
  + Anthropic Messages
  + Analytics
  + Chat
  + Credits
  + Embeddings
  + Generations
  + Models
  + Endpoints
  + Providers
  + API Keys
  + Guardrails

Light

[API Reference](/docs/api/api-reference/responses/create-responses)[Analytics](/docs/api/api-reference/analytics/get-user-activity)

Get user activity grouped by endpoint
=====================================

Copy page

GET

https://openrouter.ai/api/v1/activity

GET

/api/v1/activity

cURL

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/activity \ |
| 2 | -H "Authorization: Bearer <token>" |
```

Try it

200Retrieved

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "date": "2025-08-24", |
| 5 | "model": "openai/gpt-4.1", |
| 6 | "model_permaslug": "openai/gpt-4.1-2025-04-14", |
| 7 | "endpoint_id": "550e8400-e29b-41d4-a716-446655440000", |
| 8 | "provider_name": "OpenAI", |
| 9 | "usage": 0.015, |
| 10 | "byok_usage_inference": 0.012, |
| 11 | "requests": 5, |
| 12 | "prompt_tokens": 50, |
| 13 | "completion_tokens": 125, |
| 14 | "reasoning_tokens": 25 |
| 15 | } |
| 16 | ] |
| 17 | } |
```

Returns user activity data grouped by endpoint for the last 30 (completed) UTC days. [Management key](/docs/guides/overview/auth/management-api-keys) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

datestringOptional

Filter by a single UTC date in the last 30 days (YYYY-MM-DD format).

### Response

Returns user activity data grouped by endpoint

datalist of objects

List of activity items

Show 11 properties

### Errors

400

Bad Request Error

401

Unauthorized Error

403

Forbidden Error

500

Internal Server Error

Was this page helpful?

YesNo

[Previous](/docs/api/api-reference/anthropic-messages/create-messages)[#### Create a chat completion

Next](/docs/api/api-reference/chat/send-chat-completion-request)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)