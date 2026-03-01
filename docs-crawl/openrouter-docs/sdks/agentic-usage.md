Source: https://openrouter.ai/docs/sdks/agentic-usage

Agentic Usage | OpenRouter SDK | OpenRouter | Documentation

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

* [Quick Start](#quick-start)
* [Supported AI Coding Assistants](#supported-ai-coding-assistants)
* [What the Skill Provides](#what-the-skill-provides)
* [Example Usage](#example-usage)
* [Updating the Skill](#updating-the-skill)
* [Manual Installation](#manual-installation)
* [Repository](#repository)

Agentic Usage
=============

Copy page

Add OpenRouter SDK skills to your AI coding assistant

Give your AI coding assistant the knowledge to work with the OpenRouter SDK
by installing our official skill. This enables AI agents to understand the
SDK’s APIs, patterns, and best practices when helping you write code.

Quick Start
-----------

Run this command in your project directory:

```
|  |  |
| --- | --- |
| $ | npx add-skill OpenRouterTeam/agent-skills |
```

This installs the OpenRouter SDK skill, which teaches your AI assistant how
to use the SDK effectively.

Supported AI Coding Assistants
------------------------------

The skill works with any AI coding assistant that supports the skills format:

| Assistant | Status |
| --- | --- |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Supported |
| [OpenCode](https://opencode.ai/) | Supported |
| [Cursor](https://cursor.com/) | Supported |
| [GitHub Copilot](https://github.com/features/copilot) | Supported |
| [Codex](https://openai.com/index/openai-codex) | Supported |
| [Amp](https://amp.dev/) | Supported |
| [Roo Code](https://roo.dev/) | Supported |
| [Antigravity](https://antigravity.dev/) | Supported |

What the Skill Provides
-----------------------

Once installed, your AI coding assistant will have knowledge of:

* **SDK Installation & Setup** - How to install and configure the OpenRouter
  SDK in TypeScript projects
* **callModel API** - The recommended approach for making AI model calls with
  full type safety and streaming support
* **Chat Completions** - Working with the chat API for conversations
* **Embeddings** - Generating embeddings for semantic search and RAG
* **Error Handling** - Proper error handling patterns and Result types
* **Streaming** - Real-time streaming responses
* **Tool Use** - Implementing function calling and tools

Example Usage
-------------

After installing the skill, your AI assistant can help you with tasks like:

**“Help me set up OpenRouter in my project”**

The assistant will know to use:

```
|  |  |
| --- | --- |
| 1 | import { callModel } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const response = await callModel({ |
| 4 | model: 'anthropic/claude-sonnet-4', |
| 5 | messages: [ |
| 6 | { role: 'user', content: 'Hello!' } |
| 7 | ] |
| 8 | }); |
```

**“Add streaming to my OpenRouter call”**

The assistant understands the streaming API:

```
|  |  |
| --- | --- |
| 1 | import { callModel } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const stream = await callModel({ |
| 4 | model: 'anthropic/claude-sonnet-4', |
| 5 | messages: [{ role: 'user', content: 'Tell me a story' }], |
| 6 | stream: true |
| 7 | }); |
| 8 |  |
| 9 | for await (const chunk of stream) { |
| 10 | process.stdout.write(chunk.choices[0]?.delta?.content ?? ''); |
| 11 | } |
```

Updating the Skill
------------------

To get the latest SDK documentation, re-run the install command:

```
|  |  |
| --- | --- |
| $ | npx add-skill OpenRouterTeam/agent-skills |
```

The skill is automatically updated when new SDK versions are released.

Manual Installation
-------------------

If you prefer to install manually, add the skill file to your project’s
`.skills/` directory:

```
|  |  |
| --- | --- |
| $ | mkdir -p .skills |
| $ | curl -o .skills/openrouter-sdk.md \ |
| > | https://raw.githubusercontent.com/OpenRouterTeam/agent-skills/main/skills/typescript-sdk/SKILL.md |
```

Repository
----------

The skill source is available at:
[github.com/OpenRouterTeam/agent-skills](https://github.com/OpenRouterTeam/agent-skills)

Contributions and feedback are welcome.

Was this page helpful?

YesNo

[#### DevTools

SDK Development Tools for telemetry capture and visualization

Next](/docs/sdks/dev-tools/devtools)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)