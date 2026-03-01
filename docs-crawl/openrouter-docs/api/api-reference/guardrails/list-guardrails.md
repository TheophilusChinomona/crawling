Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails

List guardrails | OpenRouter | Documentation

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

[API Reference](/docs/api/api-reference/responses/create-responses)[Guardrails](/docs/api/api-reference/guardrails/list-guardrails)

List guardrails
===============

Copy page

GET

https://openrouter.ai/api/v1/guardrails

GET

/api/v1/guardrails

TypeScript

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/guardrails \ |
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
| 4 | "id": "550e8400-e29b-41d4-a716-446655440000", |
| 5 | "name": "Production Guardrail", |
| 6 | "created_at": "2025-08-24T10:30:00Z", |
| 7 | "description": "Guardrail for production environment", |
| 8 | "limit_usd": 100, |
| 9 | "reset_interval": "monthly", |
| 10 | "allowed_providers": [ |
| 11 | "openai", |
| 12 | "anthropic", |
| 13 | "google" |
| 14 | ], |
| 15 | "enforce_zdr": false, |
| 16 | "updated_at": "2025-08-24T15:45:00Z" |
| 17 | } |
| 18 | ], |
| 19 | "total_count": 1 |
| 20 | } |
```

List all guardrails for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

offsetstringOptional

Number of records to skip for pagination

limitstringOptional

Maximum number of records to return (max 100)

### Response

List of guardrails

datalist of objects

List of guardrails

Show 10 properties

total\_countdouble

Total number of guardrails

### Errors

401

Unauthorized Error

500

Internal Server Error

Was this page helpful?

YesNo

[Previous](/docs/api/api-reference/api-keys/get-current-key)[#### Create a guardrail

Next](/docs/api/api-reference/guardrails/create-guardrail)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)