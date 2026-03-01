Source: https://openrouter.ai/docs/guides/features/broadcast/snowflake

Broadcast to Snowflake | OpenRouter Observability | OpenRouter | Documentation

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

* [Step 1: Create the traces table](#step-1-create-the-traces-table)
* [Step 2: Create access credentials](#step-2-create-access-credentials)
* [Step 3: Enable Broadcast in OpenRouter](#step-3-enable-broadcast-in-openrouter)
* [Step 4: Configure Snowflake](#step-4-configure-snowflake)
* [Step 5: Test and save](#step-5-test-and-save)
* [Step 6: Send a test trace](#step-6-send-a-test-trace)
* [Example queries](#example-queries)
* [Cost analysis by model](#cost-analysis-by-model)
* [User activity analysis](#user-activity-analysis)
* [Error analysis](#error-analysis)
* [Provider performance comparison](#provider-performance-comparison)
* [Usage by API key](#usage-by-api-key)
* [Accessing VARIANT columns](#accessing-variant-columns)
* [Parsing input messages](#parsing-input-messages)
* [Schema design](#schema-design)
* [Typed columns](#typed-columns)
* [VARIANT columns](#variant-columns)
* [Custom Metadata](#custom-metadata)
* [Supported Metadata Keys](#supported-metadata-keys)
* [Example](#example)
* [Querying Custom Metadata](#querying-custom-metadata)
* [Additional Context](#additional-context)
* [Privacy Mode](#privacy-mode)

[Features](/docs/guides/features/presets)[Broadcast](/docs/guides/features/broadcast/overview)

Snowflake
=========

Copy page

Send traces to Snowflake

[Snowflake](https://snowflake.com/) is a cloud data warehouse platform. OpenRouter can stream traces directly to your Snowflake database for custom analytics, long-term storage, and business intelligence.

Step 1: Create the traces table
-------------------------------

Before connecting OpenRouter, create the `OPENROUTER_TRACES` table in your Snowflake database. You can find the exact SQL in the OpenRouter dashboard when configuring the destination:

![Snowflake Table Setup](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/db3ff2b0530882403aeb9f9eaba5ca71e222c9b8c10f525c6177e677fa576c56/content/pages/features/broadcast/snowflake-table-setup.png)

Step 2: Create access credentials
---------------------------------

Generate a [Programmatic Access Token](https://docs.snowflake.com/en/user-guide/programmatic-access-tokens) with `ACCOUNTADMIN` permissions in the Snowflake UI under **Settings > Authentication**.

![Snowflake PAT](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/eead64d1e537b198567e1ce337babdb22cfa6c0f102856b4dd69355f10e74ed6/content/pages/features/broadcast/snowflake-pat.png)

Step 3: Enable Broadcast in OpenRouter
--------------------------------------

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

Step 4: Configure Snowflake
---------------------------

Click the edit icon next to **Snowflake** and enter:

* **Account**: Your Snowflake account identifier (e.g., `eac52885.us-east-1`). You can find your account region and your account number at the end of your Snowflake instance’s URL: <https://app.snowflake.com/us-east-1/eac52885>; together these make your account identifier.
* **Token**: Your Programmatic Access Token.
* **Database**: Target database name (default: `SNOWFLAKE_LEARNING_DB`).
* **Schema**: Target schema name (default: `PUBLIC`).
* **Table**: Table name (default: `OPENROUTER_TRACES`).
* **Warehouse**: Compute warehouse name (default: `COMPUTE_WH`).

Step 5: Test and save
---------------------

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

Step 6: Send a test trace
-------------------------

Make an API request through OpenRouter and query your Snowflake table to verify the trace was received.

![Snowflake Test Trace](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/d6fd2cb5005ff249fbc228889402a09c81ee584bbd9cd00aa5fc59ccfa4a4fa5/content/pages/features/broadcast/snowflake-test-trace.png)

Example queries
---------------

### Cost analysis by model

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | DATE_TRUNC('day', TIMESTAMP) as day, |
| 3 | MODEL, |
| 4 | SUM(TOTAL_COST) as total_cost, |
| 5 | SUM(TOTAL_TOKENS) as total_tokens, |
| 6 | COUNT(*) as request_count |
| 7 | FROM OPENROUTER_TRACES |
| 8 | WHERE TIMESTAMP >= DATEADD(day, -30, CURRENT_TIMESTAMP()) |
| 9 | AND STATUS = 'ok' |
| 10 | AND SPAN_TYPE = 'GENERATION' |
| 11 | GROUP BY day, MODEL |
| 12 | ORDER BY day DESC, total_cost DESC; |
```

### User activity analysis

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | USER_ID, |
| 3 | COUNT(DISTINCT TRACE_ID) as trace_count, |
| 4 | COUNT(DISTINCT SESSION_ID) as session_count, |
| 5 | SUM(TOTAL_TOKENS) as total_tokens, |
| 6 | SUM(TOTAL_COST) as total_cost, |
| 7 | AVG(DURATION_MS) as avg_duration_ms |
| 8 | FROM OPENROUTER_TRACES |
| 9 | WHERE TIMESTAMP >= DATEADD(day, -7, CURRENT_TIMESTAMP()) |
| 10 | AND SPAN_TYPE = 'GENERATION' |
| 11 | GROUP BY USER_ID |
| 12 | ORDER BY total_cost DESC; |
```

### Error analysis

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | TRACE_ID, |
| 3 | TIMESTAMP, |
| 4 | MODEL, |
| 5 | LEVEL, |
| 6 | FINISH_REASON, |
| 7 | METADATA as user_metadata, |
| 8 | INPUT, |
| 9 | OUTPUT |
| 10 | FROM OPENROUTER_TRACES |
| 11 | WHERE STATUS = 'error' |
| 12 | AND TIMESTAMP >= DATEADD(hour, -1, CURRENT_TIMESTAMP()) |
| 13 | ORDER BY TIMESTAMP DESC; |
```

### Provider performance comparison

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | PROVIDER_NAME, |
| 3 | MODEL, |
| 4 | AVG(DURATION_MS) as avg_duration_ms, |
| 5 | PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY DURATION_MS) as p50_duration_ms, |
| 6 | PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY DURATION_MS) as p95_duration_ms, |
| 7 | COUNT(*) as request_count |
| 8 | FROM OPENROUTER_TRACES |
| 9 | WHERE TIMESTAMP >= DATEADD(day, -7, CURRENT_TIMESTAMP()) |
| 10 | AND STATUS = 'ok' |
| 11 | AND SPAN_TYPE = 'GENERATION' |
| 12 | GROUP BY PROVIDER_NAME, MODEL |
| 13 | HAVING request_count >= 10 |
| 14 | ORDER BY avg_duration_ms; |
```

### Usage by API key

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | API_KEY_NAME, |
| 3 | COUNT(DISTINCT TRACE_ID) as trace_count, |
| 4 | SUM(TOTAL_COST) as total_cost, |
| 5 | SUM(PROMPT_TOKENS) as prompt_tokens, |
| 6 | SUM(COMPLETION_TOKENS) as completion_tokens |
| 7 | FROM OPENROUTER_TRACES |
| 8 | WHERE TIMESTAMP >= DATEADD(day, -30, CURRENT_TIMESTAMP()) |
| 9 | AND SPAN_TYPE = 'GENERATION' |
| 10 | GROUP BY API_KEY_NAME |
| 11 | ORDER BY total_cost DESC; |
```

### Accessing VARIANT columns

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | TRACE_ID, |
| 3 | METADATA:custom_field::STRING as custom_value, |
| 4 | ATTRIBUTES:"gen_ai.request.model"::STRING as requested_model |
| 5 | FROM OPENROUTER_TRACES |
| 6 | WHERE METADATA:custom_field IS NOT NULL; |
```

### Parsing input messages

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | TRACE_ID, |
| 3 | INPUT:messages[0]:role::STRING as first_message_role, |
| 4 | INPUT:messages[0]:content::STRING as first_message_content |
| 5 | FROM OPENROUTER_TRACES |
| 6 | WHERE SPAN_TYPE = 'GENERATION'; |
```

Schema design
-------------

### Typed columns

The schema extracts commonly-queried fields as typed columns for efficient filtering and aggregation:

* **Identifiers**: TRACE\_ID, USER\_ID, SESSION\_ID, etc.
* **Timestamps**: For time-series analysis
* **Model Info**: For cost and performance analysis
* **Metrics**: Tokens and costs for billing

### VARIANT columns

Less commonly-accessed and variable-structure data is stored in VARIANT columns:

* **ATTRIBUTES**: Full OTEL attribute set
* **INPUT/OUTPUT**: Variable message structures
* **METADATA**: User-defined key-values
* **MODEL\_PARAMETERS**: Model-specific configurations

This design balances query performance with schema flexibility and storage efficiency.

Custom Metadata
---------------

Custom metadata from the `trace` field is stored in the `METADATA` VARIANT column. You can query it using Snowflake’s semi-structured data functions.

### Supported Metadata Keys

| Key | Snowflake Mapping | Description |
| --- | --- | --- |
| `trace_id` | `TRACE_ID` column / `METADATA:trace_id` | Custom trace identifier for grouping |
| `trace_name` | `METADATA:trace_name` | Custom name for the trace |
| `span_name` | `METADATA:span_name` | Name for intermediate spans |
| `generation_name` | `METADATA:generation_name` | Name for the LLM generation |

### Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Forecast next quarter revenue..." }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_name": "Revenue Forecasting", |
| 8 | "generation_name": "Generate Forecast", |
| 9 | "department": "finance", |
| 10 | "quarter": "Q2-2026", |
| 11 | "model_version": "v3" |
| 12 | } |
| 13 | } |
```

### Querying Custom Metadata

Use Snowflake’s VARIANT column syntax to query your custom metadata:

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | TRACE_ID, |
| 3 | METADATA:department::STRING as department, |
| 4 | METADATA:quarter::STRING as quarter, |
| 5 | METADATA:model_version::STRING as model_version, |
| 6 | TOTAL_COST, |
| 7 | TOTAL_TOKENS |
| 8 | FROM OPENROUTER_TRACES |
| 9 | WHERE METADATA:department IS NOT NULL |
| 10 | AND SPAN_TYPE = 'GENERATION' |
| 11 | ORDER BY TIMESTAMP DESC; |
```

### Additional Context

* The `user` field maps to the `USER_ID` typed column
* The `session_id` field maps to the `SESSION_ID` typed column
* All custom metadata keys from `trace` are stored in the `METADATA` VARIANT column for flexible querying
* You can create materialized views on frequently queried metadata fields for better performance

Privacy Mode
------------

When [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) for details.

Was this page helpful?

YesNo

[Previous](/docs/guides/features/broadcast/sentry)[#### 

W&B Weave

Send traces to W&B Weave

Next](/docs/guides/features/broadcast/weave)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)