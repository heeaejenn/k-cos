import streamlit as st
from langchain_core.messages.chat import ChatMessage
from asker2 import answer_by_gpt

st.title('K-Cosmetics Counseler Chatbot')

# 대화기록 리스트 생성
if 'message' not in st.session_state:
    st.session_state['message'] = []

# 이전 대화 메시지 출력 함수 생성
def print_messages():
    # 저장한 대화기록 출력
    for chat_message in st.session_state['message']:
        st.chat_message(chat_message.role).write(chat_message.content)

# 이전 대화 메세지 저장 함수 생성
def save_messages(role, message):
    st.session_state['message'].append(ChatMessage(role=role, content=message))


# -------------------------------메시지 출력란------------------------------------------
with st.chat_message("ai"):
    st.write("Hi there! What are you looking for?")

print_messages()

user_input_in_here = st.chat_input('Chat here :-)')

if user_input_in_here:
    # 말풍선 생성
    st.chat_message('user').write(user_input_in_here)
    resp = answer_by_gpt(user_input_in_here)
    st.chat_message('ai').write(resp)

    save_messages('user', user_input_in_here)
    save_messages('ai',resp)

