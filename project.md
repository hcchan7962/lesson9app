This project is a minimal Streamlit app that accepts a system prompt, contextual input, and a user question, then streams an AI response from OpenRouter in real time. Built in Python, it uses Pydantic AI to define typed schemas and lightweight orchestration so inputs/outputs are validated and predictable. The Streamlit UI provides three text areas and a live token-by-token output region, while the backend calls OpenRouter with an environment-based API key (`OPENROUTER_API_KEY`) using streaming for low-latency feedback. Langfuse instrumentation records traces, inputs/outputs, timings, and token usage to enable observability and iterative prompt improvement. The code follows functional, modular patterns with clear type hints, making it simple to extend with caching, guardrails, or multi-model routing.

## Phased Implementation Checklist

### Phase 1 — MVP (Non‑streaming)
- [ ] Phase 1.1 — Sidebar key input and session state
  - [ ] Add `OpenRouter API Key` password input
  - [ ] Save to `st.session_state["openrouter_api_key"]` on change
  - [ ] Show warning if missing when clicking “Stream Response”

- [ ] Phase 1.2 — Input model and validation
  - [ ] Create `PromptInput` model with `system`, `context`, `question`, `model`, `temperature`, `max_tokens`
  - [ ] Trim/coerce strings; require non‑empty `question`
  - [ ] Clamp `temperature` [0.0–1.5]; bound `max_tokens` [32–4096]

- [ ] Phase 1.3 — Message assembly
  - [ ] Build OpenAI‑style `messages`: system → role=system; context → role=system; question → role=user
  - [ ] Apply `temperature` and `max_tokens` parameters

- [ ] Phase 1.4 — PydanticAI/OpenRouter non‑streaming call
  - [ ] Configure base URL `https://openrouter.ai/api/v1`
  - [ ] Use `Authorization: Bearer <API_KEY>` (optional `HTTP-Referer`/`X-Title`)
  - [ ] Send request via PydanticAI `OpenAIModel` and capture final text

- [ ] Phase 1.5 — UI interaction and state flow
  - [ ] Disable inputs during request; re‑enable afterward
  - [ ] Render response text in the Response panel
  - [ ] Show elapsed time and a simple “Finished” badge

- [ ] Phase 1.6 — Clear/reset
  - [ ] Implement “Clear” to reset text areas and output
  - [ ] Preserve API key in session

- [ ] Phase 1.7 — Error handling and timeouts
  - [ ] 30s connect/read timeout; friendly messages for HTTP/network errors
  - [ ] Keep inputs intact on error

### Phase 2 — Streaming (optional enhancement)
- [ ] Add streaming via OpenAI‑compatible client with `stream=True`
- [ ] Incrementally update Streamlit placeholder with text deltas
- [ ] Graceful fallback to non‑streaming on error

### Phase 3 — Documentation and polish
- [ ] README: setup (`.venv`), installs (`streamlit`, `pydantic-ai`, streaming client)
- [ ] README: run (`streamlit run main.py`) and usage guidance
- [ ] UI tweaks for mobile compactness (textarea heights/expanders)

### Phase 4 — Later (deprioritized)
- [ ] Langfuse instrumentation (traces, timings, token usage)
