Source: https://openrouter.ai/docs/api/reference/responses/overview

OpenRouter Responses API Beta | OpenRouter | Documentation

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

On this page

* [Base URL](#base-url)
* [Authentication](#authentication)
* [Core Features](#core-features)
* [Basic Usage](#basic-usage)
* [Reasoning](#reasoning)
* [Tool Calling](#tool-calling)
* [Web Search](#web-search)
* [Error Handling](#error-handling)
* [Rate Limits](#rate-limits)

[API Guides](/docs/api/reference/overview)[Responses API](/docs/api/reference/responses/overview)

Responses API Beta
==================

Copy page

OpenAI-compatible Responses API (Beta)

##### Beta API

This API is in **beta stage** and may have breaking changes. Use with caution in production environments.

##### Stateless Only

This API is **stateless** - each request is independent and no conversation state is persisted between requests. You must include the full conversation history in each request.

OpenRouter’s Responses API Beta provides OpenAI-compatible access to multiple AI models through a unified interface, designed to be a drop-in replacement for OpenAI’s Responses API. This stateless API offers enhanced capabilities including reasoning, tool calling, and web search integration, with each request being independent and no server-side state persisted.

Base URL
--------

```
|  |
| --- |
| https://openrouter.ai/api/v1/responses |
```

Authentication
--------------

All requests require authentication using your OpenRouter API key:

TypeScriptPythoncURL

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini', |
| 9 | input: 'Hello, world!', |
| 10 | }), |
| 11 | }); |
```

Core Features
-------------

### [Basic Usage](/docs/api/reference/responses/basic-usage)

Learn the fundamentals of making requests with simple text input and handling responses.

### [Reasoning](/docs/api/reference/responses/reasoning)

Access advanced reasoning capabilities with configurable effort levels and encrypted reasoning chains.

### [Tool Calling](/docs/api/reference/responses/tool-calling)

Integrate function calling with support for parallel execution and complex tool interactions.

### [Web Search](/docs/api/reference/responses/web-search)

Enable web search capabilities with real-time information retrieval and citation annotations.

Error Handling
--------------

The API returns structured error responses:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "error": { |
| 3 | "code": "invalid_prompt", |
| 4 | "message": "Missing required parameter: 'model'." |
| 5 | }, |
| 6 | "metadata": null |
| 7 | } |
```

For comprehensive error handling guidance, see [Error Handling](/docs/api/reference/responses/error-handling).

Rate Limits
-----------

Standard OpenRouter rate limits apply. See [API Limits](/docs/api-reference/limits) for details.

Was this page helpful?

YesNo

[Previous](/docs/api/reference/errors-and-debugging)[#### Basic Usage

Getting started with the Responses API Beta

Next](/docs/api/reference/responses/basic-usage)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)