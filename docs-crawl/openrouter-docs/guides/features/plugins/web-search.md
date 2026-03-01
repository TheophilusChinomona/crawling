Source: https://openrouter.ai/docs/guides/features/plugins/web-search

Web Search | Add Real-time Web Data to AI Model Responses | OpenRouter | Documentation

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

* [Parsing web search results](#parsing-web-search-results)
* [Customizing the Web Plugin](#customizing-the-web-plugin)
* [Engine Selection](#engine-selection)
* [Default Behavior](#default-behavior)
* [Forcing Engine Selection](#forcing-engine-selection)
* [Engine-Specific Pricing](#engine-specific-pricing)
* [Pricing](#pricing)
* [Exa Search Pricing](#exa-search-pricing)
* [Native Search Pricing (Provider Passthrough)](#native-search-pricing-provider-passthrough)
* [Search Context Size Thresholds](#search-context-size-thresholds)
* [Specifying Search Context Size](#specifying-search-context-size)

[Features](/docs/guides/features/presets)[Plugins](/docs/guides/features/plugins/overview)

Web Search
==========

Copy page

Model-agnostic grounding

You can incorporate relevant web search results for *any* model on OpenRouter by activating and customizing the `web` plugin, or by appending `:online` to the model slug:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.2:online" |
| 3 | } |
```

You can also append `:online` to `:free` model variants like so:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-oss-20b:free:online" |
| 3 | } |
```

##### 

Using web search will incur extra costs, even with free models. See the [pricing section](/docs/guides/features/plugins/web-search#pricing) below for details.

`:online` is a shortcut for using the `web` plugin, and is exactly equivalent to:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openrouter/auto", |
| 3 | "plugins": [{ "id": "web" }] |
| 4 | } |
```

The web search plugin is powered by native search for Anthropic, OpenAI, Perplexity, and xAI models.

##### 

For xAI models, the web search plugin enables both Web Search and X Search.

For other models, the web search plugin is powered by [Exa](https://exa.ai/). It uses their [“auto”](https://docs.exa.ai/reference/how-exa-search-works#combining-neural-and-keyword-the-best-of-both-worlds-through-exa-auto-search) method (a combination of keyword search and embeddings-based web search) to find the most relevant results and augment/ground your prompt.

Parsing web search results
--------------------------

Web search results for all models (including native-only models like Perplexity and OpenAI Online) are available in the API and standardized by OpenRouter to follow the same annotation schema in the [OpenAI Chat Completion Message type](https://platform.openai.com/docs/api-reference/chat/object):

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "message": { |
| 3 | "role": "assistant", |
| 4 | "content": "Here's the latest news I found: ...", |
| 5 | "annotations": [ |
| 6 | { |
| 7 | "type": "url_citation", |
| 8 | "url_citation": { |
| 9 | "url": "https://www.example.com/web-search-result", |
| 10 | "title": "Title of the web search result", |
| 11 | "content": "Content of the web search result", // Added by OpenRouter if available |
| 12 | "start_index": 100, // The index of the first character of the URL citation in the message. |
| 13 | "end_index": 200 // The index of the last character of the URL citation in the message. |
| 14 | } |
| 15 | } |
| 16 | ] |
| 17 | } |
| 18 | } |
```

Customizing the Web Plugin
--------------------------

The maximum results allowed by the web plugin and the prompt used to attach them to your message stream can be customized:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.2:online", |
| 3 | "plugins": [ |
| 4 | { |
| 5 | "id": "web", |
| 6 | "engine": "exa", // Optional: "native", "exa", or undefined |
| 7 | "max_results": 1, // Defaults to 5 |
| 8 | "search_prompt": "Some relevant web results:" // See default below |
| 9 | } |
| 10 | ] |
| 11 | } |
```

By default, the web plugin uses the following search prompt, using the current date:

```
|  |
| --- |
| A web search was conducted on `date`. Incorporate the following web search results into your response. |
|  |
| IMPORTANT: Cite them using markdown links named using the domain of the source. |
| Example: [nytimes.com](https://nytimes.com/some-page). |
```

Engine Selection
----------------

The web search plugin supports the following options for the `engine` parameter:

* **`native`**: Always uses the model provider’s built-in web search capabilities
* **`exa`**: Uses Exa’s search API for web results
* **`undefined` (not specified)**: Uses native search if available for the provider, otherwise falls back to Exa

### Default Behavior

When the `engine` parameter is not specified:

* **Native search is used by default** for OpenAI, Anthropic, Perplexity, and xAI models that support it
* **Exa search is used** for all other models or when native search is not supported

When you explicitly specify `"engine": "native"`, it will always attempt to use the provider’s native search, even if the model doesn’t support it (which may result in an error).

### Forcing Engine Selection

You can explicitly specify which engine to use:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.2", |
| 3 | "plugins": [ |
| 4 | { |
| 5 | "id": "web", |
| 6 | "engine": "native" |
| 7 | } |
| 8 | ] |
| 9 | } |
```

Or force Exa search even for models that support native search:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.2", |
| 3 | "plugins": [ |
| 4 | { |
| 5 | "id": "web", |
| 6 | "engine": "exa", |
| 7 | "max_results": 3 |
| 8 | } |
| 9 | ] |
| 10 | } |
```

### Engine-Specific Pricing

* **Native search**: Pricing is passed through directly from the provider (see provider-specific pricing info below)
* **Exa search**: Uses OpenRouter credits at $4 per 1000 results (default 5 results = $0.02 per request)

Pricing
-------

### Exa Search Pricing

When using Exa search (either explicitly via `"engine": "exa"` or as fallback), the web plugin uses your OpenRouter credits and charges *$4 per 1000 results*. By default, `max_results` set to 5, this comes out to a maximum of $0.02 per request, in addition to the LLM usage for the search result prompt tokens.

### Native Search Pricing (Provider Passthrough)

Some models have built-in web search. These models charge a fee based on the search context size, which determines how much search data is retrieved and processed for a query.

### Search Context Size Thresholds

Search context can be ‘low’, ‘medium’, or ‘high’ and determines how much search context is retrieved for a query:

* **Low**: Minimal search context, suitable for basic queries
* **Medium**: Moderate search context, good for general queries
* **High**: Extensive search context, ideal for detailed research

### Specifying Search Context Size

You can specify the search context size in your API request using the `web_search_options` parameter:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4.1", |
| 3 | "messages": [ |
| 4 | { |
| 5 | "role": "user", |
| 6 | "content": "What are the latest developments in quantum computing?" |
| 7 | } |
| 8 | ], |
| 9 | "web_search_options": { |
| 10 | "search_context_size": "high" |
| 11 | } |
| 12 | } |
```

##### Native Web Search Pricing

Refer to each provider’s documentation for their native web search pricing info:

* [OpenAI Pricing](https://platform.openai.com/docs/pricing#built-in-tools)
* [Anthropic Pricing](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool#usage-and-pricing)
* [Perplexity Pricing](https://docs.perplexity.ai/getting-started/pricing)
* [xAI Pricing](https://docs.x.ai/docs/models#tool-invocation-costs)

Native web search pricing only applies when using `"engine": "native"` or when native search is used by default for supported models. When using `"engine": "exa"`, the Exa search pricing applies instead.

Was this page helpful?

YesNo

[Previous](/docs/guides/features/plugins/overview)[#### Response Healing

Automatically fix malformed JSON responses

Next](/docs/guides/features/plugins/response-healing)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)