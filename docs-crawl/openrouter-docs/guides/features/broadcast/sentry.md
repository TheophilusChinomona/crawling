Source: https://openrouter.ai/docs/guides/features/broadcast/sentry

Broadcast to Sentry | OpenRouter Observability | OpenRouter | Documentation

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

* [Step 1: Get your Sentry OTLP endpoint and DSN](#step-1-get-your-sentry-otlp-endpoint-and-dsn)
* [Step 2: Enable Broadcast in OpenRouter](#step-2-enable-broadcast-in-openrouter)
* [Step 3: Configure Sentry](#step-3-configure-sentry)
* [Step 4: Test and save](#step-4-test-and-save)
* [Step 5: Send a test trace](#step-5-send-a-test-trace)
* [Custom Metadata](#custom-metadata)
* [Supported Metadata Keys](#supported-metadata-keys)
* [Example](#example)
* [Additional Context](#additional-context)
* [Privacy Mode](#privacy-mode)

[Features](/docs/guides/features/presets)[Broadcast](/docs/guides/features/broadcast/overview)

Sentry
======

Copy page

Send traces to Sentry

[Sentry](https://sentry.io/) is an application monitoring platform that helps developers identify and fix issues in real-time. With Sentry’s AI monitoring capabilities, you can track LLM performance and errors.

Step 1: Get your Sentry OTLP endpoint and DSN
---------------------------------------------

In Sentry, navigate to your project’s SDK setup:

1. Log in to your Sentry account
2. Go to **Settings > Projects > [Your Project] > SDK Setup > Client Keys (DSN)**
3. Click on the **OpenTelemetry** tab
4. Copy the **OTLP Traces Endpoint** URL (ends with `/v1/traces`)
5. Copy your **DSN** from the same page

Step 2: Enable Broadcast in OpenRouter
--------------------------------------

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

Step 3: Configure Sentry
------------------------

Click the edit icon next to **Sentry** and enter:

* **OTLP Traces Endpoint**: The OTLP endpoint URL from Sentry (e.g., `https://o123.ingest.us.sentry.io/api/456/integration/otlp/v1/traces`)
* **Sentry DSN**: Your Sentry DSN (e.g., `https://abc123@o123.ingest.us.sentry.io/456`)

Step 4: Test and save
---------------------

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

Step 5: Send a test trace
-------------------------

Make an API request through OpenRouter and view the trace in Sentry’s
Performance or Traces view.

![Sentry Trace View](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/56b7ddbbef77c96471b25b6e468e6327816ffacd355d4671ec2d20a5b0564a8e/content/pages/features/broadcast/broadcast-sentry-trace.png)

##### 

Sentry uses OpenTelemetry for trace ingestion. The OTLP endpoint and DSN
are both required for proper authentication and trace routing.

Custom Metadata
---------------

Sentry receives traces via the OTLP protocol. Custom metadata from the `trace` field is sent as span attributes and can be used for filtering and analysis in Sentry’s Performance view.

### Supported Metadata Keys

| Key | Sentry Mapping | Description |
| --- | --- | --- |
| `trace_id` | Trace ID | Group multiple requests into a single trace |
| `trace_name` | Transaction Name | Custom name for the root span |
| `span_name` | Span Description | Name for intermediate spans in the hierarchy |
| `generation_name` | Span Description | Name for the LLM generation span |
| `parent_span_id` | Parent Span ID | Link to an existing span in your trace hierarchy |

### Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Debug this error..." }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_id": "incident_investigation_001", |
| 8 | "trace_name": "Error Analysis Agent", |
| 9 | "generation_name": "Analyze Stack Trace", |
| 10 | "environment": "production", |
| 11 | "release": "v2.1.0" |
| 12 | } |
| 13 | } |
```

### Additional Context

* Custom metadata keys from `trace` are included as span attributes under the `trace.metadata.*` namespace
* The `user` field maps to `user.id` in span attributes
* The `session_id` field maps to `session.id` in span attributes
* Sentry automatically correlates LLM traces with your application’s existing error and performance data when using `parent_span_id`

Privacy Mode
------------

When [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) for details.

Was this page helpful?

YesNo

[Previous](/docs/guides/features/broadcast/s3)[#### Snowflake

Send traces to Snowflake

Next](/docs/guides/features/broadcast/snowflake)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)