Source: https://openrouter.ai/docs/guides/features/broadcast/langfuse

Broadcast to Langfuse | OpenRouter Observability | OpenRouter | Documentation

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

* [Step 1: Create a Langfuse API key](#step-1-create-a-langfuse-api-key)
* [Step 2: Enable Broadcast in OpenRouter](#step-2-enable-broadcast-in-openrouter)
* [Step 3: Configure Langfuse](#step-3-configure-langfuse)
* [Step 4: Test and save](#step-4-test-and-save)
* [Step 5: Send a test trace](#step-5-send-a-test-trace)
* [Custom Metadata](#custom-metadata)
* [Supported Metadata Keys](#supported-metadata-keys)
* [Example](#example)
* [Additional Context](#additional-context)
* [Privacy Mode](#privacy-mode)

[Features](/docs/guides/features/presets)[Broadcast](/docs/guides/features/broadcast/overview)

Langfuse
========

Copy page

Send traces to Langfuse

[Langfuse](https://langfuse.com/) is an open-source LLM engineering platform for tracing, evaluating, and debugging LLM applications.

Step 1: Create a Langfuse API key
---------------------------------

In Langfuse, go to your project’s **Settings > API Keys** and create a new key pair. Copy both the Secret Key and Public Key.

![Langfuse API Keys](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/2fda0df2def9f2d969130c4704f72937461f4cbb8bb9435aa2245bb07391a35e/content/pages/features/broadcast/broadcast-langfuse-keys.png)

Step 2: Enable Broadcast in OpenRouter
--------------------------------------

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

Step 3: Configure Langfuse
--------------------------

Click the edit icon next to **Langfuse** and enter:

* **Secret Key**: Your Langfuse Secret Key
* **Public Key**: Your Langfuse Public Key
* **Base URL** (optional): Default is `https://us.cloud.langfuse.com`. Change for other regions or self-hosted instances

![Langfuse Configuration](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/10178cb9915dae07364910b865f4dbdbfc18936d91ca39ab0a9f9f1d9892ad79/content/pages/features/broadcast/broadcast-langfuse-config.png)

Step 4: Test and save
---------------------

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

![Langfuse Configured](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/77277ddb0cd573d0efe91338a32735d6b710c4c7ecfdcd610f0750d0262b4202/content/pages/features/broadcast/broadcast-langfuse-configured.png)

Step 5: Send a test trace
-------------------------

Make an API request through OpenRouter and view the trace in Langfuse.

![Langfuse Trace](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/cbd93fc215244ec3906102bdfb3a46c4938c7dd92b076c6a3f3510cc701a9487/content/pages/features/broadcast/broadcast-langfuse-trace.png)

Custom Metadata
---------------

Langfuse supports rich trace hierarchies and metadata. Use the `trace` field to customize how your traces appear in Langfuse.

### Supported Metadata Keys

| Key | Langfuse Mapping | Description |
| --- | --- | --- |
| `trace_id` | Trace ID | Group multiple requests into a single trace |
| `trace_name` | Trace Name | Custom name displayed in the Langfuse trace list |
| `span_name` | Span Name | Name for intermediate spans in the hierarchy |
| `generation_name` | Generation Name | Name for the LLM generation observation |
| `parent_span_id` | Parent Observation ID | Link to an existing span in your trace hierarchy |

### Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Summarize this document..." }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_id": "workflow_12345", |
| 8 | "trace_name": "Document Processing Pipeline", |
| 9 | "span_name": "Summarization Step", |
| 10 | "generation_name": "Generate Summary", |
| 11 | "environment": "production", |
| 12 | "pipeline_version": "2.1.0" |
| 13 | } |
| 14 | } |
```

This creates a hierarchical trace structure in Langfuse:

```
|  |
| --- |
| Document Processing Pipeline (trace) |
| └── Summarization Step (span) |
| └── Generate Summary (generation) |
```

### Additional Context

* The `user` field maps to Langfuse’s User ID for user-level analytics
* The `session_id` field maps to Langfuse’s Session ID for grouping conversations
* Any additional keys in `trace` are passed as trace metadata and can be used for filtering and analysis in Langfuse

Privacy Mode
------------

When [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) for details.

Was this page helpful?

YesNo

[Previous](/docs/guides/features/broadcast/grafana)[#### LangSmith

Send traces to LangSmith

Next](/docs/guides/features/broadcast/langsmith)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)