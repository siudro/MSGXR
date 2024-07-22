
import streamlit as st
import openai
st.title("اتكلم مع تركي")
"""
انا الروبوت تركي وانا ساساعدكم بالتعرف على الثقافه السعوديه خصيصا منطقة الاحساء
"""
if "messages" not in st.session_state:
        st.sessions_state["messages"] = [
        {"role": "system", "content":"  اسمك تركي تحب استخدام الايموجيز عند الكلام وانت تنقل ثقافه المملكة العربيه السعوديه خصيصا منطقة الاحساء تكلم الجميع باحترام وترد على جميع من يقارن الاحساء بمنطقه اخرى "}
        ]
user = st.chat_input()
if user:
    openai.api_key = st.secrets["api"]
    st.session_state.message.append({"role": "user", "content": user})
    st.chat_message("user").write(user)
    response = openai.ChatCompletion.creat(model="gpt-4o-mini", messages=st.session_state.messages)
    ai = response.choices[0].message
    st.session_state.messages.append(ai)
    st.chat_messag("assistant").write(ai.content)
    
