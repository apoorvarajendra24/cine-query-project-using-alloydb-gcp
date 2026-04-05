import streamlit as st
from root_agent import root_agent

st.set_page_config(page_title="CineQuery", page_icon="🎬")

st.title("🎬 CineQuery - Bollywood Movie Agent")

query = st.text_input("Ask about Bollywood movies:")

if st.button("Search"):
    if query:
        result = root_agent(query)

        if "error" in result:
            st.error(result["error"])
        else:
            st.subheader("Answer")
            st.write(result["answer"])

            # optional (good for demo)
            with st.expander("See SQL Query"):
                st.code(result["sql_query"], language="sql")

            with st.expander("Raw Data"):
                st.write(result["raw_result"])
