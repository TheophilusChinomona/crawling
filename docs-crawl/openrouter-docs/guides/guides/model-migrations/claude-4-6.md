Source: https://openrouter.ai/docs/guides/guides/model-migrations/claude-4-6

Claude 4.6 Migration Guide | OpenRouter | OpenRouter | Documentation

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

* [What’s New](#whats-new)
* [Adaptive Thinking](#adaptive-thinking)
* [How it works](#how-it-works)
* [When budget-based thinking is still used](#when-budget-based-thinking-is-still-used)
* [Max Effort Level](#max-effort-level)
* [Verbosity vs Reasoning Effort](#verbosity-vs-reasoning-effort)
* [Breaking Changes](#breaking-changes)

[Guides](/docs/guides/guides/free-models-router-playground)[Model Migrations](/docs/guides/guides/model-migrations/claude-4-6)

Claude 4.6 Migration Guide
==========================

Copy page

Migrate to Claude 4.6 with adaptive thinking and max effort level

What’s New
----------

See Anthropic’s [What’s new in Claude 4.6](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6) for a full overview of new features.

Claude 4.6 Opus and 4.6 Sonnet introduce two major changes to reasoning:

1. **Adaptive Thinking** — Claude decides how much to think based on task complexity, replacing budget-based extended thinking
2. **Max Effort Level** — A new `'max'` effort level above `'high'` (Opus 4.6 and Sonnet 4.6 only)

Adaptive Thinking
-----------------

For Claude 4.6 Opus and 4.6 Sonnet, OpenRouter now uses adaptive thinking (`thinking.type: 'adaptive'`) by default instead of budget-based thinking (`thinking.type: 'enabled'` with `budget_tokens`).

### How it works

* When you enable reasoning without specifying `reasoning.max_tokens`, Claude 4.6 Opus and 4.6 Sonnet use adaptive thinking
* Claude automatically determines the appropriate amount of reasoning based on task complexity
* You don’t need to estimate or tune token budgets

### When budget-based thinking is still used

* If you explicitly set `reasoning.max_tokens`, budget-based thinking is used
* If you pass the raw Anthropic `thinking` parameter directly

```
|  |  |
| --- | --- |
| 1 | // Adaptive thinking (recommended for 4.6) |
| 2 | { |
| 3 | "model": "anthropic/claude-4.6-opus",  // or "anthropic/claude-4.6-sonnet" |
| 4 | "reasoning": { "enabled": true } |
| 5 | } |
```

```
|  |  |
| --- | --- |
| 1 | // Budget-based thinking (still supported) |
| 2 | { |
| 3 | "model": "anthropic/claude-4.6-opus",  // or "anthropic/claude-4.6-sonnet" |
| 4 | "reasoning": { "enabled": true, "max_tokens": 10000 } |
| 5 | } |
```

Max Effort Level
----------------

A new `'max'` effort level is available for Claude 4.6 Opus and 4.6 Sonnet via the `verbosity` parameter. See Anthropic’s [effort documentation](https://platform.claude.com/docs/en/build-with-claude/effort) for details on how effort controls response thoroughness and token usage.

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "anthropic/claude-4.6-opus",  // or "anthropic/claude-4.6-sonnet" |
| 3 | "verbosity": "max" |
| 4 | } |
```

##### 

`'max'` is only supported on Claude 4.6 Opus and 4.6 Sonnet. For other models, it automatically falls back to `'high'`.

Verbosity vs Reasoning Effort
-----------------------------

These are separate parameters:

| Parameter | Controls | 4.6 Behavior |
| --- | --- | --- |
| `verbosity` | Response detail (`output_config.effort`) | Works normally, supports `'max'` |
| `reasoning.effort` | Thinking token budget | Ignored (adaptive thinking used instead) |

```
|  |  |
| --- | --- |
| 1 | // verbosity works - controls response detail |
| 2 | { "model": "anthropic/claude-4.6-opus", "verbosity": "max" }  // also works with anthropic/claude-4.6-sonnet |
```

```
|  |  |
| --- | --- |
| 1 | // reasoning.effort ignored - still uses adaptive |
| 2 | { "model": "anthropic/claude-4.6-opus", "reasoning": { "enabled": true, "effort": "low" } }  // also applies to anthropic/claude-4.6-sonnet |
```

Breaking Changes
----------------

None. Existing requests continue to work:

* Budget-based thinking still works when `reasoning.max_tokens` is set
* `reasoning.effort` values (low, medium, high) are still supported for older models, but will be ignored for Opus 4.6 and Sonnet 4.6. Use `reasoning.max_tokens` to control Anthropic’s `thinking.budget_tokens`, and `verbosity` to control Anthropic’s `output_config.effort`.
* Older models (4.5 Opus, 3.7 Sonnet, etc.) behave exactly as before

| Feature | Opus 4.5 | Opus 4.6 / Sonnet 4.6 |
| --- | --- | --- |
| Default Thinking Mode | Budget-based | Adaptive |
| `reasoning.max_tokens` | Budget-based | Budget-based |
| `verbosity: 'max'` | Falls back to `high` | Supported |

Was this page helpful?

YesNo

[Previous](/docs/guides/guides/distillation)[#### Frameworks and Integrations Overview

Using OpenRouter with Popular Frameworks and Integrations

Next](/docs/guides/community/frameworks-and-integrations-overview)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)