Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key

Get current API key | OpenRouter | Documentation

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

[API Reference](/docs/api/api-reference/responses/create-responses)[API Keys](/docs/api/api-reference/api-keys/list)

Get current API key
===================

Copy page

GET

https://openrouter.ai/api/v1/key

GET

/api/v1/key

cURL

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/key \ |
| 2 | -H "Authorization: Bearer <token>" |
```

Try it

200Retrieved

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "label": "sk-or-v1-au7...890", |
| 4 | "limit": 100, |
| 5 | "usage": 25.5, |
| 6 | "usage_daily": 25.5, |
| 7 | "usage_weekly": 25.5, |
| 8 | "usage_monthly": 25.5, |
| 9 | "byok_usage": 17.38, |
| 10 | "byok_usage_daily": 17.38, |
| 11 | "byok_usage_weekly": 17.38, |
| 12 | "byok_usage_monthly": 17.38, |
| 13 | "is_free_tier": false, |
| 14 | "is_management_key": false, |
| 15 | "limit_remaining": 74.5, |
| 16 | "limit_reset": "monthly", |
| 17 | "include_byok_in_limit": false, |
| 18 | "is_provisioning_key": false, |
| 19 | "rate_limit": { |
| 20 | "requests": 1000, |
| 21 | "interval": "1h", |
| 22 | "note": "This field is deprecated and safe to ignore." |
| 23 | }, |
| 24 | "expires_at": "2027-12-31T23:59:59Z" |
| 25 | } |
| 26 | } |
```

Get information on the API key associated with the current authentication session

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Response

API key details

dataobject

Current API key information

Show 18 properties

### Errors

401

Unauthorized Error

500

Internal Server Error

Was this page helpful?

YesNo

[Previous](/docs/api/api-reference/api-keys/update-keys)[#### List guardrails

Next](/docs/api/api-reference/guardrails/list-guardrails)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)