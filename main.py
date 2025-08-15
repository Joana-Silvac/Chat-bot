import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


modelo= OpenAI(api_key=api_key)
st.set_page_config(page_title="🤖 CHAT BOT", page_icon= "🤖")
st.title("CHAT")
st.markdown("Chat bot desenvolvido por Joana")

if st.button("Apagar conversa."):
    st.session_state["lista"]=[]
    st.rerun()



if not "lista" in st.session_state:
    st.session_state["lista"]=[]

for mensagem in st.session_state["lista"]:
    role= mensagem["role"]
    content= mensagem["content"]
    st.chat_message(role).write(content)

u_pergunta= st.chat_input("Digite sua pergunta aqui!")

if u_pergunta:
    mensagem={"role": "user", "content": u_pergunta}
    st.session_state["lista"].append(mensagem)
    st.chat_message("user").write(u_pergunta)
    

    resposta_m= modelo.chat.completions.create(
    messages=st.session_state["lista"],
    model= "gpt-4o-mini"
)

    resposta_ia= resposta_m.choices[0].message.content

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia={"role": "assistant", "content": resposta_ia}
    st.session_state["lista"].append(mensagem_ia)

    