import streamlit as st
import openai

st.title("اتكلم مع تركي")
"""
انا الروبوت تركي وانا ساساعدكم بالتعرف على الثقافه السعوديه خصيصا منطقة الاحساء
"""
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "اسمك تركي تحب استخدام الايموجيز عند الكلام وانت تنقل ثقافه المملكة العربيه السعوديه خصيصا منطقة الاحساء تكلم الجميع باحترام وترد على جميع من يقارن الاحساء بمنطقه اخرى"}
    ]

user_input = st.text_input("أسألني شيء:", key="user_input")

if user_input:
    openai.api_key = st.secrets["api"]
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    response = openai.ChatCompletion.create(model="gpt-4o-mini", messages=st.session_state.messages)
    ai_response = response.choices[0].message
    st.session_state.messages.append(ai_response)
    st.chat_message("assistant").write(ai_response.content)
