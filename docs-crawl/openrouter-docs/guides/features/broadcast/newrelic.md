Source: https://openrouter.ai/docs/guides/features/broadcast/newrelic

Broadcast to New Relic | OpenRouter Observability | OpenRouter | Documentation

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

* [Step 1: Get your New Relic license key](#step-1-get-your-new-relic-license-key)
* [Step 2: Enable Broadcast in OpenRouter](#step-2-enable-broadcast-in-openrouter)
* [Step 3: Configure New Relic](#step-3-configure-new-relic)
* [Step 4: Test and save](#step-4-test-and-save)
* [Step 5: Send a test trace](#step-5-send-a-test-trace)
* [Custom Metadata](#custom-metadata)
* [Supported Metadata Keys](#supported-metadata-keys)
* [Example](#example)
* [Viewing in New Relic](#viewing-in-new-relic)
* [Additional Context](#additional-context)
* [Privacy Mode](#privacy-mode)

[Features](/docs/guides/features/presets)[Broadcast](/docs/guides/features/broadcast/overview)

New Relic
=========

Copy page

Send traces to New Relic

[New Relic](https://newrelic.com/) is a full-stack observability platform for monitoring applications, infrastructure, and digital experiences.

Step 1: Get your New Relic license key
--------------------------------------

In New Relic, navigate to your API keys:

1. Log in to your New Relic account
2. Go to **API Keys** in your account settings
3. Create a new Ingest - License key or copy an existing one

Step 2: Enable Broadcast in OpenRouter
--------------------------------------

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

Step 3: Configure New Relic
---------------------------

Click the edit icon next to **New Relic** and enter:

* **License Key**: Your New Relic ingest license key
* **Region**: Select your New Relic region (`us` or `eu`)

Step 4: Test and save
---------------------

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

Step 5: Send a test trace
-------------------------

Make an API request through OpenRouter and view the trace in New Relic’s
distributed tracing view.

![New Relic Trace View](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/2adbb2978a900052552bdbf3d13e6a1a58f5205f4439ae5a57b0d7d4d2b07939/content/pages/features/broadcast/broadcast-newrelic-trace.png)

Custom Metadata
---------------

New Relic receives traces via the OTLP protocol. Custom metadata from the `trace` field is sent as span attributes.

### Supported Metadata Keys

| Key | New Relic Mapping | Description |
| --- | --- | --- |
| `trace_id` | Trace ID | Group multiple requests into a single trace |
| `trace_name` | Span Name | Custom name for the root span |
| `span_name` | Span Name | Name for intermediate spans in the hierarchy |
| `generation_name` | Span Name | Name for the LLM generation span |
| `parent_span_id` | Parent Span ID | Link to an existing span in your trace hierarchy |

### Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Summarize this report..." }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_id": "workflow_789", |
| 8 | "trace_name": "Report Processing", |
| 9 | "generation_name": "Summarize Report", |
| 10 | "environment": "production", |
| 11 | "service": "report-api" |
| 12 | } |
| 13 | } |
```

### Viewing in New Relic

In New Relic’s distributed tracing view, you can:

* Filter traces by custom attributes using NRQL queries
* View custom metadata in the span attributes panel
* Create alerts and dashboards based on metadata fields

### Additional Context

* Custom metadata keys from `trace` are included as span attributes under the `trace.metadata.*` namespace
* The `user` field maps to `user.id` in span attributes
* The `session_id` field maps to `session.id` in span attributes
* GenAI semantic conventions (`gen_ai.*` attributes) are used for model, token, and cost data

Privacy Mode
------------

When [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) for details.

Was this page helpful?

YesNo

[Previous](/docs/guides/features/broadcast/langsmith)[#### OpenTelemetry Collector

Send traces to any OpenTelemetry-compatible backend

Next](/docs/guides/features/broadcast/otel-collector)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)