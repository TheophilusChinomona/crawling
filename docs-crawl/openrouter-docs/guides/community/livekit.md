Source: https://openrouter.ai/docs/guides/community/livekit

LiveKit Integration | OpenRouter SDK Support | OpenRouter | Documentation

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

* [Using LiveKit Agents](#using-livekit-agents)
* [Installation](#installation)
* [Authentication](#authentication)
* [Basic Usage](#basic-usage)
* [Advanced Features](#advanced-features)
* [Fallback Models](#fallback-models)
* [Provider Routing](#provider-routing)
* [Web Search Plugin](#web-search-plugin)
* [Analytics Integration](#analytics-integration)
* [Resources](#resources)

[Community](/docs/guides/community/frameworks-and-integrations-overview)

LiveKit
=======

Copy page

Using OpenRouter with LiveKit Agents

Using LiveKit Agents
--------------------

[LiveKit Agents](https://docs.livekit.io/agents/) is an open-source framework for building voice AI agents. The OpenRouter plugin allows you to access 300+ AI models from multiple providers through a unified API, with automatic fallback support and intelligent routing.

### Installation

Install the OpenAI plugin to add OpenRouter support:

```
|  |  |
| --- | --- |
| $ | uv add "livekit-agents[openai]~=1.2" |
```

### Authentication

The OpenRouter plugin requires an [OpenRouter API key](https://openrouter.ai/settings/keys). Set `OPENROUTER_API_KEY` in your `.env` file.

### Basic Usage

Create an OpenRouter LLM using the `with_openrouter` method:

Python

```
|  |  |
| --- | --- |
| 1 | from livekit.plugins import openai |
| 2 |  |
| 3 | session = AgentSession( |
| 4 | llm=openai.LLM.with_openrouter(model="anthropic/claude-sonnet-4.5"), |
| 5 | # ... tts, stt, vad, turn_detection, etc. |
| 6 | ) |
```

### Advanced Features

#### Fallback Models

Configure multiple fallback models to use if the primary model is unavailable:

Python

```
|  |  |
| --- | --- |
| 1 | from livekit.plugins import openai |
| 2 |  |
| 3 | llm = openai.LLM.with_openrouter( |
| 4 | model="openai/gpt-4o", |
| 5 | fallback_models=[ |
| 6 | "anthropic/claude-sonnet-4", |
| 7 | "openai/gpt-5-mini", |
| 8 | ], |
| 9 | ) |
```

#### Provider Routing

Control which providers are used for model inference:

Python

```
|  |  |
| --- | --- |
| 1 | from livekit.plugins import openai |
| 2 |  |
| 3 | llm = openai.LLM.with_openrouter( |
| 4 | model="deepseek/deepseek-chat-v3.1", |
| 5 | provider={ |
| 6 | "order": ["novita/fp8", "gmicloud/fp8", "google-vertex"], |
| 7 | "allow_fallbacks": True, |
| 8 | "sort": "latency", |
| 9 | }, |
| 10 | ) |
```

#### Web Search Plugin

Enable OpenRouter’s web search capabilities:

Python

```
|  |  |
| --- | --- |
| 1 | from livekit.plugins import openai |
| 2 |  |
| 3 | llm = openai.LLM.with_openrouter( |
| 4 | model="google/gemini-2.5-flash-preview-09-2025", |
| 5 | plugins=[ |
| 6 | openai.OpenRouterWebPlugin( |
| 7 | max_results=5, |
| 8 | search_prompt="Search for relevant information", |
| 9 | ) |
| 10 | ], |
| 11 | ) |
```

#### Analytics Integration

Include site and app information for OpenRouter analytics:

Python

```
|  |  |
| --- | --- |
| 1 | from livekit.plugins import openai |
| 2 |  |
| 3 | llm = openai.LLM.with_openrouter( |
| 4 | model="openrouter/auto", |
| 5 | site_url="https://myapp.com", |
| 6 | app_name="My Voice Agent", |
| 7 | ) |
```

### Resources

* [LiveKit OpenRouter Plugin Documentation](https://docs.livekit.io/agents/models/llm/plugins/openrouter/)
* [LiveKit Agents GitHub](https://github.com/livekit/agents)
* [OpenRouter Models](https://openrouter.ai/models)

Was this page helpful?

YesNo

[Previous](/docs/guides/community/langchain)[#### Langfuse

Using OpenRouter with Langfuse

Next](/docs/guides/community/langfuse)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)