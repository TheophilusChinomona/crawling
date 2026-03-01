Source: https://openrouter.ai/docs/sdks/python/overview

OpenRouter Python SDK | Complete Documentation | OpenRouter | Documentation

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

* [Why use the OpenRouter SDK?](#why-use-the-openrouter-sdk)
* [Auto-generated from API specifications](#auto-generated-from-api-specifications)
* [Type-safe by default](#type-safe-by-default)
* [Installation](#installation)
* [Quick start](#quick-start)

[Python SDK](/docs/sdks/python/overview)

Python SDK
==========

Copy page

Official OpenRouter Python SDK documentation

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

The OpenRouter Python SDK is a type-safe toolkit for building AI applications with access to 300+ language models through a unified API.

Why use the OpenRouter SDK?
---------------------------

Integrating AI models into applications involves handling different provider APIs, managing model-specific requirements, and avoiding common implementation mistakes. The OpenRouter SDK standardizes these integrations and protects you from footguns.

```
|  |  |
| --- | --- |
| 1 | from openrouter import OpenRouter |
| 2 | import os |
| 3 |  |
| 4 | with OpenRouter( |
| 5 | api_key=os.getenv("OPENROUTER_API_KEY") |
| 6 | ) as client: |
| 7 | response = client.chat.send( |
| 8 | model="minimax/minimax-m2", |
| 9 | messages=[ |
| 10 | {"role": "user", "content": "Explain quantum computing"} |
| 11 | ] |
| 12 | ) |
```

The SDK provides three core benefits:

### Auto-generated from API specifications

The SDK is automatically generated from OpenRouter’s OpenAPI specs and updated with every API change. New models, parameters, and features appear in your IDE autocomplete immediately. No manual updates. No version drift.

```
|  |  |
| --- | --- |
| 1 | # When new models launch, they're available instantly |
| 2 | response = client.chat.send( |
| 3 | model="minimax/minimax-m2" |
| 4 | ) |
```

### Type-safe by default

Every parameter, response field, and configuration option is fully typed with Python type hints and validated with Pydantic. Invalid configurations are caught at runtime with clear error messages.

```
|  |  |
| --- | --- |
| 1 | response = client.chat.send( |
| 2 | model="minimax/minimax-m2", |
| 3 | messages=[ |
| 4 | {"role": "user", "content": "Hello"} |
| 5 | # ← Pydantic validates message structure |
| 6 | ], |
| 7 | temperature=0.7,  # ← Type-checked and validated |
| 8 | stream=True       # ← Response type changes based on this |
| 9 | ) |
```

**Actionable error messages:**

```
|  |  |
| --- | --- |
| 1 | # Instead of generic errors, get specific guidance: |
| 2 | # "Model 'openai/o1-preview' requires at least 2 messages. |
| 3 | #  You provided 1 message. Add a system or user message." |
```

**Type-safe streaming:**

```
|  |  |
| --- | --- |
| 1 | stream = client.chat.send( |
| 2 | model="minimax/minimax-m2", |
| 3 | messages=[{"role": "user", "content": "Write a story"}], |
| 4 | stream=True |
| 5 | ) |
| 6 |  |
| 7 | for event in stream: |
| 8 | # Full type information for streaming responses |
| 9 | content = event.choices[0].delta.content if event.choices else None |
```

**Async support:**

```
|  |  |
| --- | --- |
| 1 | import asyncio |
| 2 |  |
| 3 | async def main(): |
| 4 | async with OpenRouter( |
| 5 | api_key=os.getenv("OPENROUTER_API_KEY") |
| 6 | ) as client: |
| 7 | response = await client.chat.send_async( |
| 8 | model="minimax/minimax-m2", |
| 9 | messages=[{"role": "user", "content": "Hello"}] |
| 10 | ) |
| 11 | print(response.choices[0].message.content) |
| 12 |  |
| 13 | asyncio.run(main()) |
```

Installation
------------

```
|  |  |
| --- | --- |
| $ | # Using uv (recommended) |
| $ | uv add openrouter |
| $ |  |
| $ | # Using pip |
| $ | pip install openrouter |
| $ |  |
| $ | # Using poetry |
| $ | poetry add openrouter |
```

**Requirements:** Python 3.9 or higher

Get your API key from [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys).

Quick start
-----------

```
|  |  |
| --- | --- |
| 1 | from openrouter import OpenRouter |
| 2 | import os |
| 3 |  |
| 4 | with OpenRouter( |
| 5 | api_key=os.getenv("OPENROUTER_API_KEY") |
| 6 | ) as client: |
| 7 | response = client.chat.send( |
| 8 | model="minimax/minimax-m2", |
| 9 | messages=[ |
| 10 | {"role": "user", "content": "Hello!"} |
| 11 | ] |
| 12 | ) |
| 13 |  |
| 14 | print(response.choices[0].message.content) |
```

Was this page helpful?

YesNo

[Previous](/docs/sdks/typescript/api-reference/responses)[#### 

Analytics - Python SDK

Analytics method reference

Next](/docs/sdks/python/api-reference/analytics)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)