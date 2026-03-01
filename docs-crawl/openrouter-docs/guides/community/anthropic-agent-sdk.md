Source: https://openrouter.ai/docs/guides/community/anthropic-agent-sdk

Anthropic Agent SDK Integration | OpenRouter SDK Support | OpenRouter | Documentation

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

* [Configuration](#configuration)
* [TypeScript Example](#typescript-example)
* [Python Example](#python-example)

[Community](/docs/guides/community/frameworks-and-integrations-overview)

Anthropic Agent SDK
===================

Copy page

Using OpenRouter with the Anthropic Agent SDK

The [Anthropic Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) lets you build AI agents programmatically using Python or TypeScript. Since the Agent SDK uses Claude Code as its runtime, you can connect it to OpenRouter using the same environment variables.

Configuration
-------------

Set the following environment variables before running your agent:

```
|  |  |
| --- | --- |
| $ | export ANTHROPIC_BASE_URL="https://openrouter.ai/api" |
| $ | export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY" |
| $ | export ANTHROPIC_API_KEY="" # Important: Must be explicitly empty |
```

TypeScript Example
------------------

Install the SDK:

```
|  |  |
| --- | --- |
| $ | npm install @anthropic-ai/claude-agent-sdk |
```

Create an agent that uses OpenRouter:

```
|  |  |
| --- | --- |
| 1 | import { query } from "@anthropic-ai/claude-agent-sdk"; |
| 2 |  |
| 3 | // Environment variables should be set before running: |
| 4 | // ANTHROPIC_BASE_URL=https://openrouter.ai/api |
| 5 | // ANTHROPIC_AUTH_TOKEN=your_openrouter_api_key |
| 6 | // ANTHROPIC_API_KEY="" |
| 7 |  |
| 8 | async function main() { |
| 9 | for await (const message of query({ |
| 10 | prompt: "Find and fix the bug in auth.py", |
| 11 | options: { |
| 12 | allowedTools: ["Read", "Edit", "Bash"], |
| 13 | }, |
| 14 | })) { |
| 15 | if (message.type === "assistant") { |
| 16 | console.log(message.message.content); |
| 17 | } |
| 18 | } |
| 19 | } |
| 20 |  |
| 21 | main(); |
```

Python Example
--------------

Install the SDK:

```
|  |  |
| --- | --- |
| $ | pip install claude-agent-sdk |
```

Create an agent that uses OpenRouter:

```
|  |  |
| --- | --- |
| 1 | import asyncio |
| 2 | from claude_agent_sdk import query, ClaudeAgentOptions |
| 3 |  |
| 4 | # Environment variables should be set before running: |
| 5 | # ANTHROPIC_BASE_URL=https://openrouter.ai/api |
| 6 | # ANTHROPIC_AUTH_TOKEN=your_openrouter_api_key |
| 7 | # ANTHROPIC_API_KEY="" |
| 8 |  |
| 9 | async def main(): |
| 10 | async for message in query( |
| 11 | prompt="Find and fix the bug in auth.py", |
| 12 | options=ClaudeAgentOptions( |
| 13 | allowed_tools=["Read", "Edit", "Bash"] |
| 14 | ) |
| 15 | ): |
| 16 | print(message) |
| 17 |  |
| 18 | asyncio.run(main()) |
```

##### 

**Tip:** The Agent SDK inherits all the same model override capabilities as Claude Code. You can use `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_OPUS_MODEL`, and other environment variables to route your agent to different models on OpenRouter. See the [Claude Code integration guide](/docs/guides/guides/claude-code-integration) for more details.

Was this page helpful?

YesNo

[Previous](/docs/guides/community/openai-sdk)[#### PydanticAI

Using OpenRouter with PydanticAI

Next](/docs/guides/community/pydantic-ai)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)