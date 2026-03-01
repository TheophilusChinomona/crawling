Source: https://openrouter.ai/docs/api/api-reference/generations/get-generation

Get request & usage metadata for a generation | OpenRouter | Documentation

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

[API Reference](/docs/api/api-reference/responses/create-responses)[Generations](/docs/api/api-reference/generations/get-generation)

Get request & usage metadata for a generation

Copy page

GET

https://openrouter.ai/api/v1/generation

GET

/api/v1/generation

cURL

```
|  |  |
| --- | --- |
| 1 | curl -G https://openrouter.ai/api/v1/generation \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -d id=id |
```

Try it

200Retrieved

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "id": "gen-3bhGkxlo4XFrqiabUM7NDtwDzWwG", |
| 4 | "upstream_id": "chatcmpl-791bcf62-080e-4568-87d0-94c72e3b4946", |
| 5 | "total_cost": 0.0015, |
| 6 | "cache_discount": 0.0002, |
| 7 | "upstream_inference_cost": 0.0012, |
| 8 | "created_at": "2024-07-15T23:33:19.433273+00:00", |
| 9 | "model": "sao10k/l3-stheno-8b", |
| 10 | "app_id": 12345, |
| 11 | "streamed": true, |
| 12 | "cancelled": false, |
| 13 | "provider_name": "Infermatic", |
| 14 | "latency": 1250, |
| 15 | "moderation_latency": 50, |
| 16 | "generation_time": 1200, |
| 17 | "finish_reason": "stop", |
| 18 | "tokens_prompt": 10, |
| 19 | "tokens_completion": 25, |
| 20 | "native_tokens_prompt": 10, |
| 21 | "native_tokens_completion": 25, |
| 22 | "native_tokens_completion_images": 0, |
| 23 | "native_tokens_reasoning": 5, |
| 24 | "native_tokens_cached": 3, |
| 25 | "num_media_prompt": 1, |
| 26 | "num_input_audio_prompt": 0, |
| 27 | "num_media_completion": 0, |
| 28 | "num_search_results": 5, |
| 29 | "origin": "https://openrouter.ai/", |
| 30 | "usage": 0.0015, |
| 31 | "is_byok": false, |
| 32 | "native_finish_reason": "stop", |
| 33 | "external_user": "user-123", |
| 34 | "api_type": "completions", |
| 35 | "router": "openrouter/auto", |
| 36 | "provider_responses": [ |
| 37 | { |
| 38 | "status": 1.1, |
| 39 | "id": "string", |
| 40 | "endpoint_id": "string", |
| 41 | "model_permaslug": "string", |
| 42 | "provider_name": "AnyScale", |
| 43 | "latency": 1.1, |
| 44 | "is_byok": true |
| 45 | } |
| 46 | ] |
| 47 | } |
| 48 | } |
```

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

idstringRequired`>=1 character`

### Response

Returns the request metadata for this generation

dataobject

Generation data

Show 34 properties

### Errors

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

Was this page helpful?

YesNo

[Previous](/docs/api/api-reference/embeddings/list-embeddings-models)[#### Get total count of available models

Next](/docs/api/api-reference/models/list-models-count)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)