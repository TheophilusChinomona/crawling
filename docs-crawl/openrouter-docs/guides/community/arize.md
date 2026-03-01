Source: https://openrouter.ai/docs/guides/community/arize

Arize Integration | OpenRouter SDK Support | OpenRouter | Documentation

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

* [Using Arize](#using-arize)
* [Installation](#installation)
* [Prerequisites](#prerequisites)
* [Why OpenRouter Works with Arize](#why-openrouter-works-with-arize)
* [Configuration](#configuration)
* [Simple LLM Call](#simple-llm-call)
* [What Gets Traced](#what-gets-traced)
* [JavaScript/TypeScript Support](#javascripttypescript-support)
* [Common Issues](#common-issues)
* [Learn More](#learn-more)

[Community](/docs/guides/community/frameworks-and-integrations-overview)

Arize
=====

Copy page

Using OpenRouter with Arize

Using Arize
-----------

[Arize](https://arize.com/) provides observability and tracing for LLM applications. Since OpenRouter uses the OpenAI API schema, you can utilize Arize’s OpenInference auto-instrumentation with the OpenAI SDK to automatically trace and monitor your OpenRouter API calls.

### Installation

```
|  |  |
| --- | --- |
| $ | pip install openinference-instrumentation-openai openai arize-otel |
```

### Prerequisites

* OpenRouter account and API key
* Arize account with Space ID and API Key

### Why OpenRouter Works with Arize

Arize’s OpenInference auto-instrumentation works with OpenRouter because:

1. **OpenRouter provides a fully OpenAI-API-compatible endpoint** - The `/v1` endpoint mirrors OpenAI’s schema
2. **Reuse official OpenAI SDKs** - Point the OpenAI client’s `base_url` to OpenRouter
3. **Automatic instrumentation** - OpenInference hooks into OpenAI SDK calls seamlessly

### Configuration

Set up your environment variables:

Environment Setup

```
|  |  |
| --- | --- |
| 1 | import os |
| 2 |  |
| 3 | # Set your OpenRouter API key |
| 4 | os.environ["OPENAI_API_KEY"] = "${API_KEY_REF}" |
```

### Simple LLM Call

Initialize Arize and instrument your OpenAI client to automatically trace OpenRouter calls:

Basic Integration

```
|  |  |
| --- | --- |
| 1 | from arize.otel import register |
| 2 | from openinference.instrumentation.openai import OpenAIInstrumentor |
| 3 | import openai |
| 4 |  |
| 5 | # Initialize Arize and register the tracer provider |
| 6 | tracer_provider = register( |
| 7 | space_id="your-space-id", |
| 8 | api_key="your-arize-api-key", |
| 9 | project_name="your-project-name", |
| 10 | ) |
| 11 |  |
| 12 | # Instrument OpenAI SDK |
| 13 | OpenAIInstrumentor().instrument(tracer_provider=tracer_provider) |
| 14 |  |
| 15 | # Configure OpenAI client for OpenRouter |
| 16 | client = openai.OpenAI( |
| 17 | base_url="https://openrouter.ai/api/v1", |
| 18 | api_key="your_openrouter_api_key", |
| 19 | default_headers={ |
| 20 | "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional: Your site URL |
| 21 | "X-OpenRouter-Title": "<YOUR_SITE_NAME>",      # Optional: Your site name |
| 22 | } |
| 23 | ) |
| 24 |  |
| 25 | # Make a traced chat completion request |
| 26 | response = client.chat.completions.create( |
| 27 | model="meta-llama/llama-3.1-8b-instruct:free", |
| 28 | messages=[ |
| 29 | {"role": "user", "content": "Write a haiku about observability."} |
| 30 | ], |
| 31 | ) |
| 32 |  |
| 33 | # Print the assistant's reply |
| 34 | print(response.choices[0].message.content) |
```

### What Gets Traced

All OpenRouter model calls are automatically traced and include:

* Request/response data and timing
* Model name and provider information
* Token usage and cost data (when supported)
* Error handling and debugging information

### JavaScript/TypeScript Support

OpenInference also provides instrumentation for the OpenAI JavaScript/TypeScript SDK, which works with OpenRouter. For setup and examples, please refer to the [OpenInference JavaScript examples for OpenAI](https://github.com/Arize-ai/openinference/tree/main/js).

### Common Issues

* **API Key**: Use your OpenRouter API key, not OpenAI’s
* **Model Names**: Use exact model names from [OpenRouter’s model list](https://openrouter.ai/models)
* **Rate Limits**: Check your OpenRouter dashboard for usage limits

### Learn More

* **Arize OpenRouter Integration**: <https://arize.com/docs/ax/integrations/llm-providers/openrouter/openrouter-tracing>
* **OpenRouter Quick Start Guide**: <https://openrouter.ai/docs/quickstart>
* **OpenInference OpenAI Instrumentation**: <https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-openai>

Was this page helpful?

YesNo

[Previous](/docs/guides/community/effect-ai-sdk)[#### LangChain

Using OpenRouter with LangChain

Next](/docs/guides/community/langchain)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)