.PHONY: claude-haiku-4-5
claude-haiku-4-5:
	mkdir -p result
	MODEL_NAME=anthropic:claude-haiku-4-5 uv run pytest --md result/claude-haiku-4-5.md

.PHONY: claude-haiku-4-7
claude-haiku-4-7:
	mkdir -p result
	MODEL_NAME=anthropic:claude-sonnet-4-7 uv run pytest --md result/claude-sonnet-4-7.md

.PHONY: gemini-3.1-flash-lite
gemini-3.1-flash-lite:
	mkdir -p result
	MODEL_NAME=google_genai:gemini-3.1-flash-lite uv run pytest --md result/gemini-3.1-flash-lite-preview.md

