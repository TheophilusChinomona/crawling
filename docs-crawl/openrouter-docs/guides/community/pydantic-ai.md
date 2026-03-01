Source: https://openrouter.ai/docs/guides/community/pydantic-ai#using-pydanticai

PydanticAI Integration | OpenRouter SDK Support | OpenRouter | Documentation

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

* [Using PydanticAI](#using-pydanticai)
* [Installation](#installation)
* [Configuration](#configuration)

[Community](/docs/guides/community/frameworks-and-integrations-overview)

PydanticAI
==========

Copy page

Using OpenRouter with PydanticAI

Using PydanticAI
----------------

[PydanticAI](https://github.com/pydantic/pydantic-ai) provides a high-level interface for working with various LLM providers, including OpenRouter.

### Installation

```
|  |  |
| --- | --- |
| $ | pip install 'pydantic-ai-slim[openai]' |
```

### Configuration

You can use OpenRouter with PydanticAI through its OpenAI-compatible interface:

```
|  |  |
| --- | --- |
| 1 | from pydantic_ai import Agent |
| 2 | from pydantic_ai.models.openai import OpenAIModel |
| 3 |  |
| 4 | model = OpenAIModel( |
| 5 | "anthropic/claude-3.5-sonnet",  # or any other OpenRouter model |
| 6 | base_url="https://openrouter.ai/api/v1", |
| 7 | api_key="sk-or-...", |
| 8 | ) |
| 9 |  |
| 10 | agent = Agent(model) |
| 11 | result = await agent.run("What is the meaning of life?") |
| 12 | print(result) |
```

For more details about using PydanticAI with OpenRouter, see the [PydanticAI documentation](https://ai.pydantic.dev/models/#api_key-argument).

Was this page helpful?

YesNo

[Previous](/docs/guides/community/anthropic-agent-sdk)[#### TanStack AI

Using OpenRouter with TanStack AI

Next](/docs/guides/community/tanstack-ai)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)