Source: https://openrouter.ai/docs/api/api-reference/models/list-models-count

Get total count of available models | OpenRouter | Documentation

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

[API Reference](/docs/api/api-reference/responses/create-responses)[Models](/docs/api/api-reference/models/list-models-count)

Get total count of available models
===================================

Copy page

GET

https://openrouter.ai/api/v1/models/count

GET

/api/v1/models/count

cURL

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/models/count \ |
| 2 | -H "Authorization: Bearer <token>" |
```

Try it

200Retrieved

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "count": 150 |
| 4 | } |
| 5 | } |
```

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Response

Returns the total count of available models

dataobject

Model count data

Show 1 properties

### Errors

500

Internal Server Error

Was this page helpful?

YesNo

[Previous](/docs/api/api-reference/generations/get-generation)[#### List all models and their properties

Next](/docs/api/api-reference/models/get-models)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)