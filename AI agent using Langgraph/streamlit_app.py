import streamlit as st
from agent.workflow import create_agent

st.title("LangGraph Agent Example")

query = st.text_input("Enter your query:")
if st.button("Run"):
    workflow = create_agent()
    result = workflow.invoke({"query": query})
    st.write("Answer:", result.get("answer"))
