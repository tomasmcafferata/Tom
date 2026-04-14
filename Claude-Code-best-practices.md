# Claude Code Best Practices

## File & Document Management

- **Convert files to text:** Extract clean text from PDFs, DOCXs, and PPTs before uploading, as formatting and metadata consume massive amounts of tokens. Crop screenshots tightly.
- **Don't over-share files:** Only upload files necessary for the specific task. Avoid dumping entire folders "just in case." Keep permanent context files (like "About Me") short (under 2,000 words).
- **Use Projects for recurring files:** Instead of uploading the same file to multiple chats, upload it to a Project where it gets cached, saving tokens on future references. For Claude Code, use a concise CLAUDE.md file to set permanent rules.

## Prompting & Chat Strategies

- **Edit instead of following up:** If Claude makes a mistake, don't reply with "No, I meant..." (which adds to the history). Instead, hit the Edit button on your original prompt, fix it, and regenerate.
- **Targeted edits:** Instead of asking Claude to rewrite an entire report, specify the exact section that needs changing (e.g., "only redo section 3").
- **Make Claude ask questions:** Use short prompts (e.g., 30 words) and tell Claude to "ask me questions" before starting. This prevents you from writing massive, token-heavy instruction blocks.
- **Batch tasks:** Put multiple requests (e.g., summarize, list points, suggest a headline) into a single prompt to avoid multiple context reloads.
- **Voice prompting:** Using voice-to-text tools like Wispr Flow allows you to give more detailed, one-shot context naturally, reducing the need for back-and-forth corrections.

## Workflow & Tool Optimization

- **Plan in Chat, build in Cowork:** Do your brainstorming and structuring in the cheaper Chat interface. Once the plan is locked in, move to the more expensive Cowork/Opus interface to execute it.
- **Pick the right model:** Use Haiku or Sonnet for simple, quick tasks (formatting, grammar, short answers). Reserve the heavy machinery (Opus) for deep, complex work.
- **Turn off unused features:** Turn off web search, connectors, extended thinking, and memory if you don't need them for the specific task, as they automatically consume tokens.
- **Start fresh:** When a conversation gets too long, ask Claude to summarize it. Then, take that summary, open a completely new chat, and paste it to start with a clean slate. Always start a new chat when changing topics.
- **Pace yourself:** Claude uses a rolling 5-hour usage limit window. Spread your intensive tasks throughout the morning, afternoon, and evening to maximize your daily capacity.
- **Use the right AI:** Don't waste Claude tokens on tasks it's bad at, like generating images or real-time web searches. Switch to tools like ChatGPT, Gemini, or Grok for those.
