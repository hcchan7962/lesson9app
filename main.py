import streamlit as st


def render_ui() -> None:
    st.set_page_config(page_title="OpenRouter Streamlit Chat", layout="wide")

    st.title("OpenRouter Streamlit Chat")
    st.caption("System + Context + Question → Streaming response")

    left_col, right_col = st.columns([2, 1])

    with left_col:
        system_prompt: str = st.text_area(
            "System Prompt",
            height=120,
            placeholder="e.g., You are a helpful assistant...",
        )
        context_text: str = st.text_area(
            "Context",
            height=160,
            placeholder="Background/context...",
        )
        question_text: str = st.text_area(
            "Question",
            height=120,
            placeholder="What would you like to ask?",
            help="Required when sending a prompt",
        )

    with right_col:
        model_name: str = st.selectbox(
            "Model",
            options=["<choose a model>", "openrouter/model-a", "openrouter/model-b"],
            index=0,
            help="Select a model to use via OpenRouter",
        )
        temperature: float = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.5,
            value=0.7,
            step=0.05,
            help="Higher values produce more creative but less deterministic outputs",
        )
        max_tokens: int = st.slider(
            "Max Tokens",
            min_value=64,
            max_value=4096,
            value=512,
            step=64,
            help="Maximum number of tokens to generate in the response",
        )
        show_stream: bool = st.checkbox("Show token stream", value=True)

        st.markdown("\n")
        st.write(":material/rocket_launch: Actions")
        action_status = st.empty()
        stream_btn: bool = st.button("Stream Response", use_container_width=True)
        clear_btn: bool = st.button("Clear", type="secondary", use_container_width=True)

        if stream_btn:
            api_key_value: str = st.session_state.get("openrouter_api_key", "").strip()
            if not api_key_value:
                action_status.warning("OpenRouter API key is required to send requests.")
            else:
                action_status.info("API key detected. Ready to send request (mock only).")

    st.markdown("---")
    st.subheader("Response")
    response_container = st.container()
    with response_container:
        st.info(
            "Streaming output will appear here (mock only; no external calls are made)."
        )
        st.caption(
            "Status: tokens/sec, elapsed time, and usage will display here in a real run."
        )

    with st.sidebar:
        st.header("Run Settings")
        if "openrouter_api_key" not in st.session_state:
            st.session_state["openrouter_api_key"] = ""

        def _normalize_api_key() -> None:
            st.session_state["openrouter_api_key"] = (
                st.session_state.get("openrouter_api_key", "").strip()
            )

        openrouter_api_key: str = st.text_input(
            "OpenRouter API Key",
            placeholder="sk-or-...",
            type="password",
            help="Paste your OpenRouter API key here (stored only in session).",
            key="openrouter_api_key",
            on_change=_normalize_api_key,
        )
        key_is_set: bool = bool(st.session_state.get("openrouter_api_key", ""))
        if key_is_set:
            st.success("API key set in session")
            st.caption(
                f"Stored (masked). Length: {len(st.session_state['openrouter_api_key'])}"
            )
        else:
            st.warning("No API key set")

        def _clear_api_key() -> None:
            st.session_state["openrouter_api_key"] = ""

        st.button("Clear API Key", on_click=_clear_api_key, use_container_width=True)
        enable_langfuse: bool = st.toggle("Enable Langfuse tracing", value=True)
        session_name: str = st.text_input(
            "Session name", placeholder="e.g., demo-session"
        )
        user_id: str = st.text_input("User id", placeholder="optional")
        st.caption("This is a UI mockup. No logic or integrations are implemented.")

    # Note: additional validation and request execution will be added in later phases.


def main() -> None:
    render_ui()


if __name__ == "__main__":
    main()


