Source: https://openrouter.ai/docs/guides/features/broadcast/langsmith

Broadcast to LangSmith | OpenRouter Observability | OpenRouter | Documentation

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

* [Step 1: Get your LangSmith API key and Project name](#step-1-get-your-langsmith-api-key-and-project-name)
* [Step 2: Enable Broadcast in OpenRouter](#step-2-enable-broadcast-in-openrouter)
* [Step 3: Configure LangSmith](#step-3-configure-langsmith)
* [Step 4: Test and save](#step-4-test-and-save)
* [Step 5: Send a test trace](#step-5-send-a-test-trace)
* [What data is sent](#what-data-is-sent)
* [Custom Metadata](#custom-metadata)
* [Supported Metadata Keys](#supported-metadata-keys)
* [Tags](#tags)
* [Example](#example)
* [Run Types](#run-types)
* [Additional Context](#additional-context)
* [Privacy Mode](#privacy-mode)

[Features](/docs/guides/features/presets)[Broadcast](/docs/guides/features/broadcast/overview)

LangSmith
=========

Copy page

Send traces to LangSmith

[LangSmith](https://smith.langchain.com/) is LangChain’s platform for debugging, testing, evaluating, and monitoring LLM applications.

Step 1: Get your LangSmith API key and Project name
---------------------------------------------------

In LangSmith, go to **Settings > API Keys** to create a new API key. Then navigate to your project or create a new one to get the project name.

Step 2: Enable Broadcast in OpenRouter
--------------------------------------

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

Step 3: Configure LangSmith
---------------------------

Click the edit icon next to **LangSmith** and enter:

* **Api Key**: Your LangSmith API key (starts with `lsv2_pt_...`)
* **Project**: Your LangSmith project name
* **Endpoint** (optional): Default is `https://api.smith.langchain.com`. Change for self-hosted instances

Step 4: Test and save
---------------------

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

Step 5: Send a test trace
-------------------------

Make an API request through OpenRouter and view the trace in LangSmith. Your traces will appear in the specified project with full details including:

* Input and output messages
* Token usage (prompt, completion, and total tokens)
* Cost information
* Model and provider information
* Timing and latency metrics

What data is sent
-----------------

OpenRouter sends traces to LangSmith using the OpenTelemetry (OTEL) protocol with the following attributes:

* **GenAI semantic conventions**: Model name, token counts, costs, and request parameters
* **LangSmith-specific attributes**: Trace name, span kind, user ID, and custom metadata
* **Error handling**: Exception events with error types and messages when requests fail

##### 

LangSmith uses the OTEL endpoint at `/otel/v1/traces` for receiving trace data. This ensures compatibility with LangSmith’s native tracing infrastructure.

Custom Metadata
---------------

LangSmith supports trace hierarchies, tags, and custom metadata for organizing and analyzing your LLM calls.

### Supported Metadata Keys

| Key | LangSmith Mapping | Description |
| --- | --- | --- |
| `trace_id` | Trace ID | Group multiple runs into a single trace |
| `trace_name` | Run Name | Custom name displayed in the LangSmith trace list |
| `span_name` | Run Name | Name for intermediate chain/tool runs |
| `generation_name` | Run Name | Name for the LLM run |
| `parent_span_id` | Parent Run ID | Link to an existing run in your trace hierarchy |

### Tags

Any array of strings passed in metadata can be used as tags. Tags in LangSmith are comma-separated values that help you filter and organize traces.

### Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Analyze this text..." }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_id": "analysis_workflow_123", |
| 8 | "trace_name": "Text Analysis Pipeline", |
| 9 | "span_name": "Sentiment Analysis", |
| 10 | "generation_name": "Extract Sentiment", |
| 11 | "environment": "production", |
| 12 | "team": "nlp-team" |
| 13 | } |
| 14 | } |
```

### Run Types

OpenRouter maps observation types to LangSmith run types:

* **GENERATION** → `llm` run type
* **SPAN** → `chain` run type
* **EVENT** → `tool` run type

### Additional Context

* The `user` field maps to LangSmith’s User ID
* The `session_id` field maps to LangSmith’s Session ID for conversation tracking
* Custom metadata keys are passed as span attributes and viewable in the run details

Privacy Mode
------------

When [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) for details.

Was this page helpful?

YesNo

[Previous](/docs/guides/features/broadcast/langfuse)[#### New Relic

Send traces to New Relic

Next](/docs/guides/features/broadcast/newrelic)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)