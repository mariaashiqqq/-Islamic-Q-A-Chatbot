import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# -- Setup Gemini API --
GOOGLE_API_KEY = "AIzaSyA02m9uCQYMlftxAsejMTOas8wQCc2DYHY"
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)
output_parser = StrOutputParser()

# -- Prompt Template --
system_prompt = (
    "You are a knowledgeable Islamic scholar and assistant. "
    "Answer questions only using references from the Qur’an and authentic Hadith. "
    "Avoid personal opinions. If unsure, say 'I don't know based on Islamic knowledge.'"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "Question: {question}")
])

chain = prompt | llm | output_parser

# -- Streamlit App --
st.set_page_config(page_title="🕌 Islamic Chatbot", layout="centered")
st.title("🤖 Islamic Q&A Chatbot (Powered by Gemini)")
st.markdown("Ask anything related to **Qur’an, Hadith, Islamic terms, or practices**.")

user_input = st.text_input("✍️ Ask your Islamic question:")

if st.button("Get Answer") and user_input:
    with st.spinner("Thinking..."):
        try:
            answer = chain.invoke({"question": user_input})
            st.success("📜 Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ Error: {e}")
