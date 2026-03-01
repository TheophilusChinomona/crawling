Source: https://openrouter.ai/docs/guides/guides/openclaw-integration

Integration with OpenClaw | OpenRouter | OpenRouter | Documentation

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

* [What is OpenClaw?](#what-is-openclaw)
* [Setup](#setup)
* [Recommended: Use the OpenClaw Setup Wizard](#recommended-use-the-openclaw-setup-wizard)
* [Quick Start (CLI)](#quick-start-cli)
* [Manual Configuration](#manual-configuration)
* [Step 1: Get Your OpenRouter API Key](#step-1-get-your-openrouter-api-key)
* [Step 2: Set Your API Key](#step-2-set-your-api-key)
* [Step 3: Choose Your Model](#step-3-choose-your-model)
* [Step 4: Start OpenClaw](#step-4-start-openclaw)
* [Model Format](#model-format)
* [Multiple Models with Fallbacks](#multiple-models-with-fallbacks)
* [Using Auto Model for Cost Optimization](#using-auto-model-for-cost-optimization)
* [Using Auth Profiles](#using-auth-profiles)
* [Monitoring Usage](#monitoring-usage)
* [Common Errors](#common-errors)
* [”No API key found for provider ‘openrouter’”](#no-api-key-found-for-provider-openrouter)
* [Authentication errors (401/403)](#authentication-errors-401403)
* [Model not working](#model-not-working)
* [Advanced Configuration](#advanced-configuration)
* [Per-Channel Models](#per-channel-models)
* [Resources](#resources)

[Guides](/docs/guides/guides/free-models-router-playground)

OpenClaw 🦞

Copy page

Use OpenClaw (formerly Moltbot, formerly Clawdbot) with OpenRouter

What is OpenClaw?
-----------------

[OpenClaw](https://github.com/openclaw/openclaw) (formerly Moltbot, formerly Clawdbot) is an open-source AI agent platform that brings conversational AI to multiple messaging channels including Telegram, Discord, Slack, Signal, iMessage, and WhatsApp. It supports multiple LLM providers and allows you to run AI agents that can interact across all these platforms.

Setup
-----

### Recommended: Use the OpenClaw Setup Wizard

The easiest way to configure OpenClaw with OpenRouter is using the built-in setup wizard:

```
|  |  |
| --- | --- |
| $ | openclaw onboard |
```

The wizard will guide you through:

1. Choosing OpenRouter as your provider
2. Entering your API key
3. Selecting your preferred model
4. Configuring messaging channels

This is the recommended approach for new users and ensures everything is configured correctly.

### Quick Start (CLI)

If you already have your OpenRouter API key and want to skip the wizard, use this one-line command:

```
|  |  |
| --- | --- |
| $ | openclaw onboard --auth-choice apiKey --token-provider openrouter --token "$OPENROUTER_API_KEY" |
```

This automatically configures OpenClaw to use OpenRouter with the recommended model (`openrouter/auto`).

Manual Configuration
--------------------

##### 

**Advanced users only:** The following manual configuration is for users who need to edit their config file directly. For most users, we recommend using the setup wizard above.

If you need to manually edit your OpenClaw configuration file, follow these steps:

### Step 1: Get Your OpenRouter API Key

1. Sign up or log in at [OpenRouter](https://openrouter.ai/)
2. Navigate to your [API Keys page](https://openrouter.ai/keys)
3. Create a new API key
4. Copy your key (starts with `sk-or-...`)

### Step 2: Set Your API Key

Add your OpenRouter API key to your `~/.openclaw/openclaw.json`:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "env": { |
| 3 | "OPENROUTER_API_KEY": "sk-or-..." |
| 4 | }, |
| 5 | "agents": { |
| 6 | "defaults": { |
| 7 | "model": { |
| 8 | "primary": "openrouter/anthropic/claude-sonnet-4.5" |
| 9 | }, |
| 10 | "models": { |
| 11 | "openrouter/anthropic/claude-sonnet-4.5": {} |
| 12 | } |
| 13 | } |
| 14 | } |
| 15 | } |
```

Or set it as an environment variable in your shell profile:

```
|  |  |
| --- | --- |
| $ | export OPENROUTER_API_KEY="sk-or-..." |
```

##### 

That’s it! OpenClaw has built-in support for OpenRouter. You don’t need to configure `models.providers` - just set your API key and reference models with the `openrouter/<author>/<slug>` format.

### Step 3: Choose Your Model

Update the `primary` model and add it to the `models` list. Here are some popular options:

**Anthropic Claude:**

```
|  |  |
| --- | --- |
| 1 | "model": { |
| 2 | "primary": "openrouter/anthropic/claude-sonnet-4.5" |
| 3 | }, |
| 4 | "models": { |
| 5 | "openrouter/anthropic/claude-sonnet-4.5": {} |
| 6 | } |
```

**Google Gemini:**

```
|  |  |
| --- | --- |
| 1 | "model": { |
| 2 | "primary": "openrouter/google/gemini-pro-1.5" |
| 3 | }, |
| 4 | "models": { |
| 5 | "openrouter/google/gemini-pro-1.5": {} |
| 6 | } |
```

**DeepSeek:**

```
|  |  |
| --- | --- |
| 1 | "model": { |
| 2 | "primary": "openrouter/deepseek/deepseek-chat" |
| 3 | }, |
| 4 | "models": { |
| 5 | "openrouter/deepseek/deepseek-chat": {} |
| 6 | } |
```

**Moonshot Kimi:**

```
|  |  |
| --- | --- |
| 1 | "model": { |
| 2 | "primary": "openrouter/moonshotai/kimi-k2.5" |
| 3 | }, |
| 4 | "models": { |
| 5 | "openrouter/moonshotai/kimi-k2.5": {} |
| 6 | } |
```

Browse all available models at [openrouter.ai/models](https://openrouter.ai/models).

### Step 4: Start OpenClaw

After updating your configuration, start or restart OpenClaw:

```
|  |  |
| --- | --- |
| $ | openclaw gateway run |
```

Your agents will now use OpenRouter to route requests to your chosen model.

Model Format
------------

OpenClaw uses the format `openrouter/<author>/<slug>` for OpenRouter models. For example:

* `openrouter/anthropic/claude-sonnet-4.5`
* `openrouter/google/gemini-pro-1.5`
* `openrouter/moonshotai/kimi-k2.5`
* `openrouter/openrouter/auto` (Auto router that picks the most cost effective model for your prompt)

You can find the exact format for each model on the [OpenRouter models page](https://openrouter.ai/models).

Multiple Models with Fallbacks
------------------------------

OpenClaw supports model fallbacks. If the primary model is unavailable, it will try the fallback models in order:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "agents": { |
| 3 | "defaults": { |
| 4 | "model": { |
| 5 | "primary": "openrouter/anthropic/claude-sonnet-4.5", |
| 6 | "fallbacks": [ |
| 7 | "openrouter/anthropic/claude-haiku-3.5" |
| 8 | ] |
| 9 | }, |
| 10 | "models": { |
| 11 | "openrouter/anthropic/claude-sonnet-4.5": {}, |
| 12 | "openrouter/anthropic/claude-haiku-3.5": {} |
| 13 | } |
| 14 | } |
| 15 | } |
| 16 | } |
```

This provides an additional layer of reliability on top of OpenRouter’s provider-level failover.

Using Auto Model for Cost Optimization
--------------------------------------

OpenClaw agents perform many different types of actions, from simple heartbeat processing to complex reasoning tasks. Using a powerful model for every action wastes money on tasks that don’t require advanced capabilities.

The OpenRouter Auto Model (`openrouter/openrouter/auto`) automatically selects the most cost-effective model based on your prompt. This is ideal for OpenClaw because it routes simple tasks like heartbeats and status checks to cheaper models while using more capable models only when needed for complex interactions.

To configure Auto Model as your primary model:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "agents": { |
| 3 | "defaults": { |
| 4 | "model": { |
| 5 | "primary": "openrouter/openrouter/auto" |
| 6 | }, |
| 7 | "models": { |
| 8 | "openrouter/openrouter/auto": {} |
| 9 | } |
| 10 | } |
| 11 | } |
| 12 | } |
```

You can also combine Auto Model with fallbacks for maximum reliability:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "agents": { |
| 3 | "defaults": { |
| 4 | "model": { |
| 5 | "primary": "openrouter/openrouter/auto", |
| 6 | "fallbacks": [ |
| 7 | "openrouter/anthropic/claude-haiku-3.5" |
| 8 | ] |
| 9 | }, |
| 10 | "models": { |
| 11 | "openrouter/openrouter/auto": {}, |
| 12 | "openrouter/anthropic/claude-haiku-3.5": {} |
| 13 | } |
| 14 | } |
| 15 | } |
| 16 | } |
```

Learn more about how Auto Model works at [openrouter.ai/models/openrouter/auto](https://openrouter.ai/models/openrouter/auto).

Using Auth Profiles
-------------------

For more secure credential management, you can use OpenClaw’s auth profiles instead of environment variables. This is automatically configured when you use the `openclaw onboard` command.

To manually create an auth profile, add this to your `openclaw.json`:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "auth": { |
| 3 | "profiles": { |
| 4 | "openrouter:default": { |
| 5 | "provider": "openrouter", |
| 6 | "mode": "api_key" |
| 7 | } |
| 8 | } |
| 9 | } |
| 10 | } |
```

Then use the OpenClaw CLI to set the key in your system keychain:

```
|  |  |
| --- | --- |
| $ | openclaw auth set openrouter:default --key "$OPENROUTER_API_KEY" |
```

This keeps your API key out of your config file and stores it securely in your system keychain.

Monitoring Usage
----------------

Track your OpenClaw usage in real-time:

1. Visit the [OpenRouter Activity Dashboard](https://openrouter.ai/activity)
2. See requests, costs, and token usage across all your OpenClaw agents
3. Filter by model, time range, or other criteria
4. Export usage data for billing or analysis

Common Errors
-------------

### ”No API key found for provider ‘openrouter’”

OpenClaw can’t find your OpenRouter API key.

**Fix:**

1. Ensure the `OPENROUTER_API_KEY` environment variable is set: `echo $OPENROUTER_API_KEY`
2. Or verify your auth profile exists: `openclaw auth list`
3. Run the onboard command: `openclaw onboard --auth-choice apiKey --token-provider openrouter --token "$OPENROUTER_API_KEY"`

### Authentication errors (401/403)

If you see authentication errors:

**Fix:**

1. Verify your API key is valid at [openrouter.ai/keys](https://openrouter.ai/keys)
2. Check that you have sufficient credits in your account
3. Ensure your key hasn’t expired or been revoked

### Model not working

If a specific model isn’t working:

**Fix:**

1. Verify the model ID is correct on the [OpenRouter models page](https://openrouter.ai/models)
2. Use the format `openrouter/<author>/<slug>` (e.g., `openrouter/anthropic/claude-sonnet-4.5`)
3. Add the model to `agents.defaults.models` in your config

Advanced Configuration
----------------------

### Per-Channel Models

Configure different models for different messaging channels:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "telegram": { |
| 3 | "agents": { |
| 4 | "defaults": { |
| 5 | "model": { |
| 6 | "primary": "openrouter/anthropic/claude-haiku-3.5" |
| 7 | } |
| 8 | } |
| 9 | } |
| 10 | }, |
| 11 | "discord": { |
| 12 | "agents": { |
| 13 | "defaults": { |
| 14 | "model": { |
| 15 | "primary": "openrouter/anthropic/claude-sonnet-4.5" |
| 16 | } |
| 17 | } |
| 18 | } |
| 19 | } |
| 20 | } |
```

Resources
---------

* [OpenClaw Documentation](https://docs.openclaw.ai/)
* [OpenClaw OpenRouter Provider Guide](https://docs.openclaw.ai/providers/openrouter)
* [OpenClaw GitHub](https://github.com/openclaw/openclaw)
* [OpenRouter Models](https://openrouter.ai/models)
* [OpenRouter Activity Dashboard](https://openrouter.ai/activity)
* [OpenRouter API Documentation](https://openrouter.ai/docs/api)

Was this page helpful?

YesNo

[Previous](/docs/guides/guides/claude-code-integration)[#### Organization Management

Manage teams and shared resources with OpenRouter organizations

Next](/docs/use-cases/organization-management)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)