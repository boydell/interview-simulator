import os
import openai
import streamlit as st
from streamlit_chat import message

openai.api_key = os.environ.get('openai-key')
st.session_state['industry'] = 'Healthcare'
st.session_state['job title'] = 'Software Engineer'

def reset():
  type = ("You are a hiring manager for a " + st.session_state['industry'] + 
    " company, hiring a " + st.session_state['job title'] + "." +
    " Ask the candidate 5 questions one at a time, and then ask the candidate if they have" +
    " any questions for you. Answer as concisely as possible with a little humor expression.")
  st.session_state['prompts'] = [{"role": "system", "content": type}]
  st.session_state['past'] = []
  st.session_state['generated'] = []
  st.session_state['user'] = "Hi, thanks for inviting me to this interview."
  chat_click()

def generate_response(prompt):
  st.session_state['prompts'].append({"role": "user", "content": prompt})
  completion=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = st.session_state['prompts']
  )
  
  message=completion.choices[0].message.content
  return message

def end_click():
  reset()

def chat_click():
  if st.session_state['user'] != '':
    chat_input = st.session_state['user']
    output=generate_response(chat_input)
    #store the output
    st.session_state['past'].append(chat_input)
    st.session_state['generated'].append(output)
    st.session_state['prompts'].append({"role": "assistant", "content": output})
    st.session_state['user'] = ""

if 'prompts' not in st.session_state:
  reset()

# Now do the things
# st.image("{Your logo}", width=80)
st.title("Interview Simulator")
end_button=st.button("Start Over", on_click=end_click)

user_input=st.text_area("You:", key="user")
chat_button=st.button("Send", on_click=chat_click)

if st.session_state['generated']:
  for i in range(len(st.session_state['generated'])-1, -1, -1):
    message(st.session_state['generated'][i], key=str(i))
    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
