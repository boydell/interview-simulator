import os
import openai
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('openai-key')
if 'started' not in st.session_state:
  st.session_state['started'] = False
if 'generated' not in st.session_state:
  st.session_state['generated'] = []

# Stuff to add:
# * linkedIn links, twitter, etc?
# * Maybe include in the prompt, if it doesn't get enough detail, ask for more.
# * If empty, no specific industry or job title

def reset():
  type = "You are a hiring manager"
  if st.session_state['industry']:
    type = type + " for a " + st.session_state['industry'] + " company"
  if st.session_state['job-title']:
    type = type + ", hiring a " + st.session_state['job-title']

  type = type + """. Ask the candidate 6 questions, one at a time, and then ask the candidate if they have
    any questions for you. Make all the responses as concise as possible with a little humor expression."""
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

def start_click():
  st.session_state['started'] = True
  reset()

def end_click():
  st.session_state['past'] = []
  st.session_state['generated'] = []
  st.session_state['started'] = False

def chat_click():
  if st.session_state['user'] != '':
    chat_input = st.session_state['user']
    output=generate_response(chat_input)
    #store the output
    st.session_state['past'].append(chat_input)
    st.session_state['generated'].append(output)
    st.session_state['prompts'].append({"role": "assistant", "content": output})
    st.session_state['user'] = ""

# ---- Now do the things
st.set_page_config(page_title="Interview Simulator")
st.image("sit-interview.png", width=120)
st.title("Interview Simulator")
st.markdown("""This is a tool to practice interviews. Every time you run it, the questions will be similar, 
  but different. It will ask five questions, then ask if you have any questions. Think seriously 
  how you would answer each question in a real interview, and the simulator will give feedback for each answer.
  The simulator will be very nice, so don't expect actual interviews to be so pleasant. :smiley:

  You can leave __Industry__ and __Job Title__ blank, which will result in generic interview questions.
  """)

if st.session_state["started"] == False:
  industry = st.text_input("Industry", key="industry")
  job_title = st.text_input("Job Title", key="job-title")
  start_button = st.button("Start", on_click=start_click)
else:
  end_button=st.button("Start Over", on_click=end_click)
  user_input=st.text_area("You:", key="user")
  chat_button=st.button("Send", on_click=chat_click)

if st.session_state['generated']:
  for i in range(len(st.session_state['generated'])-1, -1, -1):
    message(st.session_state['generated'][i], key=str(i))
    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
