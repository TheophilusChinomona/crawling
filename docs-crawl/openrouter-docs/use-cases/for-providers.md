Source: https://openrouter.ai/docs/use-cases/for-providers

Provider Integration | Add Your AI Models to OpenRouter | OpenRouter | Documentation

Search

`/`

Ask AI

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

* Overview

  + [Quickstart](/docs/quickstart)
  + [Principles](/docs/guides/overview/principles)
  + [Models](/docs/guides/overview/models)
  + Multimodal
  + Authentication
  + [FAQ](/docs/faq)
  + [Report Feedback](/docs/guides/overview/report-feedback)
  + [Enterprise](https://openrouter.ai/enterprise)
* Models & Routing

  + [Model Fallbacks](/docs/guides/routing/model-fallbacks)
  + [Provider Selection](/docs/guides/routing/provider-selection)
  + Model Variants
  + Routers
* Features

  + [Presets](/docs/guides/features/presets)
  + [Tool Calling](/docs/guides/features/tool-calling)
  + Plugins
  + [Structured Outputs](/docs/guides/features/structured-outputs)
  + [Message Transforms](/docs/guides/features/message-transforms)
  + [Zero Completion Insurance](/docs/guides/features/zero-completion-insurance)
  + [ZDR](/docs/guides/features/zdr)
  + [App Attribution](/docs/app-attribution)
  + [Guardrails](/docs/guides/features/guardrails)
  + Broadcast
* + Privacy
  + Best Practices
  + Guides
  + Community

Light

On this page

* [For Providers](#for-providers)
* [1. List Models Endpoint](#1-list-models-endpoint)
* [Tiered Pricing](#tiered-pricing)
* [Deprecation Date](#deprecation-date)
* [2. Auto Top Up or Invoicing](#2-auto-top-up-or-invoicing)
* [3. Uptime Monitoring & Traffic Routing](#3-uptime-monitoring--traffic-routing)
* [4. Performance Metrics](#4-performance-metrics)

[Guides](/docs/guides/guides/free-models-router-playground)

Provider Integration
====================

Copy page

For Providers
-------------

If you’d like to be a model provider and sell inference on OpenRouter, [fill out our form](https://openrouter.ai/how-to-list) to get started.

To be eligible to provide inference on OpenRouter you must have the following:

### 1. List Models Endpoint

You must implement an endpoint that returns all models that should be served by OpenRouter. At this endpoint, please return a list of all available models on your platform. Below is an example of the response format:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | // Required |
| 5 | "id": "anthropic/claude-sonnet-4", |
| 6 | "hugging_face_id": "", // required if the model is on Hugging Face |
| 7 | "name": "Anthropic: Claude Sonnet 4", |
| 8 | "created": 1690502400, |
| 9 | "input_modalities": ["text", "image", "file"], |
| 10 | "output_modalities": ["text", "image", "file"], |
| 11 | "quantization": "fp8", |
| 12 | "context_length": 1000000, |
| 13 | "max_output_length": 128000, |
| 14 | "pricing": { |
| 15 | "prompt": "0.000008", // pricing per 1 token |
| 16 | "completion": "0.000024", // pricing per 1 token |
| 17 | "image": "0", // pricing per 1 image |
| 18 | "request": "0", // pricing per 1 request |
| 19 | "input_cache_read": "0" // pricing per 1 token |
| 20 | }, |
| 21 | "supported_sampling_parameters": ["temperature", "stop"], |
| 22 | "supported_features": [ |
| 23 | "tools", |
| 24 | "json_mode", |
| 25 | "structured_outputs", |
| 26 | "web_search", |
| 27 | "reasoning" |
| 28 | ], |
| 29 | // Optional |
| 30 | "description": "Anthropic's flagship model...", |
| 31 | "deprecation_date": "2025-06-01", // ISO 8601 date (YYYY-MM-DD) |
| 32 | "openrouter": { |
| 33 | "slug": "anthropic/claude-sonnet-4" |
| 34 | }, |
| 35 | "datacenters": [ |
| 36 | { |
| 37 | "country_code": "US" // `Iso3166Alpha2Code` |
| 38 | } |
| 39 | ] |
| 40 | } |
| 41 | ] |
| 42 | } |
```

The `id` field should be the exact model identifier that OpenRouter will use when calling your API.

The `pricing` fields are in string format to avoid floating point precision issues, and must be in USD.

Valid quantization values are: `int4`, `int8`, `fp4`, `fp6`, `fp8`, `fp16`, `bf16`, `fp32`.

Valid sampling parameters are: `temperature`, `top_p`, `top_k`, `min_p`, `top_a`, `frequency_penalty`, `presence_penalty`, `repetition_penalty`, `stop`, `seed`, `max_tokens`, `logit_bias`, `logprobs`, `top_logprobs`.

Valid features are: `tools`, `json_mode`, `structured_outputs`, `logprobs`, `web_search`, `reasoning`.

#### Tiered Pricing

For models with different pricing based on context length (e.g., long context pricing), you can provide `pricing` as an array of tiers instead of a single object:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "pricing": [ |
| 3 | { |
| 4 | "prompt": "0.000002", // base tier pricing per 1 token |
| 5 | "completion": "0.000012", // base tier pricing per 1 token |
| 6 | "image": "0.01", // pricing per 1 image (base tier only) |
| 7 | "request": "0", // pricing per 1 request (base tier only) |
| 8 | "input_cache_read": "0.000001" // base tier pricing per 1 token |
| 9 | }, |
| 10 | { |
| 11 | "prompt": "0.000004", // long context tier pricing per 1 token |
| 12 | "completion": "0.000018", // long context tier pricing per 1 token |
| 13 | "input_cache_read": "0.000002", // long context tier pricing per 1 token |
| 14 | "min_context": 200000 // minimum input tokens for this tier to apply |
| 15 | } |
| 16 | ] |
| 17 | } |
```

When using tiered pricing, the first tier (index 0) is the base pricing that applies when input tokens are below the `min_context` threshold. The second tier applies when input tokens meet or exceed the `min_context` value.

Limitations:

* Currently, OpenRouter supports up to 2 pricing tiers.
* The `image` and `request` fields are only supported in the base tier (index 0) and will be ignored if included in other tiers.

#### Deprecation Date

If a model is scheduled for deprecation, include the `deprecation_date` field in ISO 8601 format (YYYY-MM-DD):

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "id": "anthropic/claude-2.1", |
| 3 | "deprecation_date": "2025-06-01" |
| 4 | } |
```

When OpenRouter’s provider monitor detects a deprecation date, it will automatically update the endpoint to display deprecation warnings to users. Models past their deprecation date may be automatically hidden from the marketplace.

### 2. Auto Top Up or Invoicing

For OpenRouter to use the provider we must be able to pay for inference automatically. This can be done via auto top up or invoicing.

### 3. Uptime Monitoring & Traffic Routing

OpenRouter automatically monitors provider reliability and adjusts traffic routing based on uptime metrics. Your endpoint’s uptime is calculated as: **successful requests ÷ total requests** (excluding user errors).

**Errors that affect your uptime:**

* Authentication issues (401)
* Payment failures (402)
* Model not found (404)
* All server errors (500+)
* Mid-stream errors
* Successful requests with error finish reasons

**Errors that DON’T affect uptime:**

* Bad requests (400) - user input errors
* Oversized payloads (413) - user input errors
* Rate limiting (429) - tracked separately
* Geographic restrictions (403) - tracked separately

**Traffic routing thresholds:**

* **Minimum data**: 100+ requests required before uptime calculation begins
* **Normal routing**: 95%+ uptime
* **Degraded status**: 80-94% uptime → receives lower priority
* **Down status**: <80% uptime → only used as fallback

This system ensures traffic automatically flows to the most reliable providers while giving temporary issues time to resolve.

### 4. Performance Metrics

OpenRouter publicly tracks TTFT (time to first token) and throughput (tokens/second) for all providers on each model page.

Throughput is calculated as: **output tokens ÷ generation time**, where generation time includes fetch latency (time from request to first server response), TTFT, and streaming time. This means any queueing on your end will show up in your throughput metrics.

To keep your metrics competitive:

* Return early 429s if under load, rather than queueing requests
* Stream tokens as soon as they’re available
* If processing takes time (e.g. reasoning models), send SSE comments as keep-alives so we know you’re still working on the request. Otherwise we may cancel with a fetch timeout and fallback to another provider

Was this page helpful?

YesNo

[Previous](/docs/use-cases/organization-management)[#### Usage Accounting

Next](/docs/guides/guides/usage-accounting)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)