Source: https://openrouter.ai/docs/api-reference/limits

API Rate Limits | Configure Usage Limits in OpenRouter | OpenRouter | Documentation

Search

`/`

Ask AI

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

* API Guides

  + [Overview](/docs/api/reference/overview)
  + [Streaming](/docs/api/reference/streaming)
  + [Embeddings](/docs/api/reference/embeddings)
  + [Limits](/docs/api/reference/limits)
  + [Authentication](/docs/api/reference/authentication)
  + [Parameters](/docs/api/reference/parameters)
  + [Errors and Debugging](/docs/api/reference/errors-and-debugging)
  + Responses API
* API Reference

  + Responses
  + OAuth
  + Anthropic Messages
  + Analytics
  + Chat
  + Credits
  + Embeddings
  + Generations
  + Models
  + Endpoints
  + Providers
  + API Keys
  + Guardrails

Light

On this page

* [Rate Limits and Credits Remaining](#rate-limits-and-credits-remaining)

[API Guides](/docs/api/reference/overview)

Limits
======

Copy page

Rate Limits

##### 

Making additional accounts or API keys will not affect your rate limits, as we
govern capacity globally. We do however have different rate limits for
different models, so you can share the load that way if you do run into
issues.

Rate Limits and Credits Remaining
---------------------------------

To check the rate limit or credits left on an API key, make a GET request to `https://openrouter.ai/api/v1/key`.

TypeScript SDKPythonTypeScript (Raw API)

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '{{API_KEY_REF}}', |
| 5 | }); |
| 6 |  |
| 7 | const keyInfo = await openRouter.apiKeys.getCurrent(); |
| 8 | console.log(keyInfo); |
```

If you submit a valid API key, you should get a response of the form:

TypeScript

```
|  |  |
| --- | --- |
| 1 | type Key = { |
| 2 | data: { |
| 3 | label: string; |
| 4 | limit: number | null; // Credit limit for the key, or null if unlimited |
| 5 | limit_reset: string | null; // Type of limit reset for the key, or null if never resets |
| 6 | limit_remaining: number | null; // Remaining credits for the key, or null if unlimited |
| 7 | include_byok_in_limit: boolean;  // Whether to include external BYOK usage in the credit limit |
| 8 |  |
| 9 | usage: number; // Number of credits used (all time) |
| 10 | usage_daily: number; // Number of credits used (current UTC day) |
| 11 | usage_weekly: number; // ... (current UTC week, starting Monday) |
| 12 | usage_monthly: number; // ... (current UTC month) |
| 13 |  |
| 14 | byok_usage: number; // Same for external BYOK usage |
| 15 | byok_usage_daily: number; |
| 16 | byok_usage_weekly: number; |
| 17 | byok_usage_monthly: number; |
| 18 |  |
| 19 | is_free_tier: boolean; // Whether the user has paid for credits before |
| 20 | // rate_limit: { ... } // A deprecated object in the response, safe to ignore |
| 21 | }; |
| 22 | }; |
```

There are a few rate limits that apply to certain types of requests, regardless of account status:

1. Free usage limits: If you’re using a free model variant (with an ID ending in `:free`), you can make up to 20 requests per minute. The following per-day limits apply:

* If you have purchased less than 10 credits, you’re limited to 50 `:free` model requests per day.
* If you purchase at least 10 credits, your daily limit is increased to 1000 `:free` model requests per day.

2. **DDoS protection**: Cloudflare’s DDoS protection will block requests that dramatically exceed reasonable usage.

If your account has a negative credit balance, you may see `402` errors, including for free models. Adding credits to put your balance above zero allows you to use those models again.

Was this page helpful?

YesNo

[Previous](/docs/api/reference/embeddings)[#### Authentication

API Authentication

Next](/docs/api/reference/authentication)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)