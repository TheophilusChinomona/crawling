Source: https://openrouter.ai/docs/guides/features/broadcast/otel-collector

Broadcast to OpenTelemetry Collector | OpenRouter Observability | OpenRouter | Documentation

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

* [Step 1: Get your OTLP endpoint and credentials](#step-1-get-your-otlp-endpoint-and-credentials)
* [Step 2: Enable Broadcast in OpenRouter](#step-2-enable-broadcast-in-openrouter)
* [Step 3: Configure OpenTelemetry Collector](#step-3-configure-opentelemetry-collector)
* [Step 4: Test and save](#step-4-test-and-save)
* [Step 5: Send a test trace](#step-5-send-a-test-trace)
* [Compatible backends](#compatible-backends)
* [Custom Metadata](#custom-metadata)
* [Supported Metadata Keys](#supported-metadata-keys)
* [Example](#example)
* [Span Attributes](#span-attributes)
* [Additional Context](#additional-context)
* [Privacy Mode](#privacy-mode)

[Features](/docs/guides/features/presets)[Broadcast](/docs/guides/features/broadcast/overview)

OpenTelemetry Collector
=======================

Copy page

Send traces to any OpenTelemetry-compatible backend

[OpenTelemetry](https://opentelemetry.io/) is an open-source observability framework for collecting, processing, and exporting telemetry data. OpenRouter can send traces to any backend that supports the OpenTelemetry Protocol (OTLP), including Axiom, Jaeger, Grafana Tempo, and self-hosted collectors.

Step 1: Get your OTLP endpoint and credentials
----------------------------------------------

Set up your OpenTelemetry-compatible backend and obtain the OTLP traces endpoint URL along with any required authentication headers.

For Axiom:

1. Create an Axiom account and dataset
2. Go to **Settings > API Tokens** and create a new token
3. Your endpoint is `https://api.axiom.co/v1/traces`
4. You’ll need headers: `Authorization: Bearer xaat-xxx` and `X-Axiom-Dataset: your-dataset`

For self-hosted collectors:

1. Deploy an OpenTelemetry Collector with an OTLP receiver
2. Configure the receiver to listen on a publicly accessible endpoint
3. Note the endpoint URL (typically ending in `/v1/traces`)

Step 2: Enable Broadcast in OpenRouter
--------------------------------------

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

Step 3: Configure OpenTelemetry Collector
-----------------------------------------

Click the edit icon next to **OpenTelemetry Collector** and enter:

* **Endpoint**: Your OTLP traces endpoint URL (e.g., `https://api.axiom.co/v1/traces` or `https://your-collector.example.com:4318/v1/traces`)
* **Headers** (optional): Custom HTTP headers as a JSON object for authentication

Example headers for Axiom:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "Authorization": "Bearer xaat-your-token", |
| 3 | "X-Axiom-Dataset": "your-dataset" |
| 4 | } |
```

Example headers for authenticated collectors:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "Authorization": "Bearer your-token", |
| 3 | "X-Custom-Header": "value" |
| 4 | } |
```

Step 4: Test and save
---------------------

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

Step 5: Send a test trace
-------------------------

Make an API request through OpenRouter and view the trace in your OpenTelemetry backend.

Compatible backends
-------------------

The OpenTelemetry Collector destination works with any backend that supports OTLP over HTTP, including:

* **Axiom** - Cloud-native log and trace management
* **Jaeger** - Distributed tracing platform
* **Grafana Tempo** - High-scale distributed tracing backend
* **Honeycomb** - Observability for distributed systems
* **Lightstep** - Cloud-native observability platform
* **Self-hosted OpenTelemetry Collector** - Route traces to multiple backends

##### 

OpenRouter sends traces using the OTLP/HTTP protocol with JSON encoding. Ensure your collector or backend is configured to accept OTLP over HTTP on the `/v1/traces` path.

Custom Metadata
---------------

Custom metadata from the `trace` field is sent as span attributes in the OTLP payload. How this metadata appears depends on your downstream backend.

### Supported Metadata Keys

| Key | OTLP Mapping | Description |
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
| 3 | "messages": [{ "role": "user", "content": "Hello!" }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_id": "app_trace_001", |
| 8 | "trace_name": "Chat Handler", |
| 9 | "generation_name": "Generate Response", |
| 10 | "environment": "staging", |
| 11 | "deployment": "us-east-1" |
| 12 | } |
| 13 | } |
```

### Span Attributes

Custom metadata keys are included as span attributes under the `trace.metadata.*` namespace. For example, `environment` from the trace field becomes `trace.metadata.environment` in the OTLP payload.

Standard GenAI semantic conventions (`gen_ai.*`) are used for model, token usage, and cost attributes.

### Additional Context

* The `user` field maps to `user.id` in span attributes
* The `session_id` field maps to `session.id` in span attributes
* Your downstream backend determines how these attributes are indexed, queried, and displayed
* Using `parent_span_id` lets you link OpenRouter traces to your application’s existing distributed traces

Privacy Mode
------------

When [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) for details.

Was this page helpful?

YesNo

[Previous](/docs/guides/features/broadcast/newrelic)[#### PostHog

Send traces to PostHog

Next](/docs/guides/features/broadcast/posthog)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)