Source: https://openrouter.ai/docs/api-reference/embeddings/create-embeddings

Submit an embedding request | OpenRouter | Documentation

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

[API Reference](/docs/api/api-reference/responses/create-responses)[Embeddings](/docs/api/api-reference/embeddings/create-embeddings)

Submit an embedding request
===========================

Copy page

POST

https://openrouter.ai/api/v1/embeddings

POST

/api/v1/embeddings

Python

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 |  |
| 3 | url = "https://openrouter.ai/api/v1/embeddings" |
| 4 |  |
| 5 | payload = { |
| 6 | "input": "The quick brown fox jumps over the lazy dog", |
| 7 | "model": "text-embedding-ada-002" |
| 8 | } |
| 9 | headers = { |
| 10 | "Authorization": "Bearer <token>", |
| 11 | "Content-Type": "application/json" |
| 12 | } |
| 13 |  |
| 14 | response = requests.post(url, json=payload, headers=headers) |
| 15 |  |
| 16 | print(response.json()) |
```

Try it

200Successful

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "object": "list", |
| 3 | "data": [ |
| 4 | { |
| 5 | "object": "embedding", |
| 6 | "embedding": [ |
| 7 | 0.0123, |
| 8 | -0.0456, |
| 9 | 0.0789, |
| 10 | -0.0345, |
| 11 | 0.0678, |
| 12 | -0.0234, |
| 13 | 0.0567, |
| 14 | -0.089, |
| 15 | 0.0345, |
| 16 | -0.0123 |
| 17 | ], |
| 18 | "index": 0 |
| 19 | } |
| 20 | ], |
| 21 | "model": "text-embedding-ada-002", |
| 22 | "id": "embeddings-1234567890abcdef", |
| 23 | "usage": { |
| 24 | "prompt_tokens": 9, |
| 25 | "total_tokens": 9, |
| 26 | "cost": 0.00015 |
| 27 | } |
| 28 | } |
```

Submits an embedding request to the embeddings router

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

inputstring or list of strings or list of doubles or list of lists of doubles or list of objectsRequired

Show 5 variants

modelstringRequired

encoding\_formatenumOptional

Allowed values:floatbase64

dimensionsintegerOptional`>=0`

userstringOptional

providerobjectOptional

Provider routing preferences for the request.

Show 13 properties

input\_typestringOptional

### Response

Embedding response

objectenum

Allowed values:list

datalist of objects

Show 3 properties

modelstring

idstring or null

usageobject or null

Show 3 properties

### Errors

400

Bad Request Error

401

Unauthorized Error

402

Payment Required Error

404

Not Found Error

429

Too Many Requests Error

500

Internal Server Error

502

Bad Gateway Error

503

Service Unavailable Error

Was this page helpful?

YesNo

[Previous](/docs/api/api-reference/credits/create-coinbase-charge)[#### List all embeddings models

Next](/docs/api/api-reference/embeddings/list-embeddings-models)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)