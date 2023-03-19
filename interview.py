import os
import openai
import streamlit as st
import streamlit.components.v1 as components
from streamlit_chat import message
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('openai-key')
if 'started' not in st.session_state:
  st.session_state['started'] = False
if 'generated' not in st.session_state:
  st.session_state['generated'] = []

# Stuff to add:
# * Include the industry and job title on the chat page.

def reset():
  type = "You are a hiring manager"
  if st.session_state['industry']:
    type = type + " for a " + st.session_state['industry'] + " company"
  if st.session_state['job-title']:
    type = type + ", hiring a " + st.session_state['job-title']

  type = type + """, running an interview with a candidate. Do not ask all the questions at once. Ask the candidate 5 individual questions, one at a time and allow the candidate can respond to each question before going on to the next. And then ask the candidate if they have any questions for you. Make all the responses as concise as possible with a little humor expression."""
  st.session_state['prompts'] = [{"role": "system", "content": type}]
  st.session_state['past'] = []
  st.session_state['generated'] = []
  st.session_state['user'] = "Hi, thanks for inviting me to this interview."
  chat_click()

def generate_response(prompt):
  st.session_state['prompts'].append({"role": "user", "content": prompt})

  try:
    completion=openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages = st.session_state['prompts']
    )
    message=completion.choices[0].message.content
  except:
    message = "Whoops. I ran out of stuff to say. You might have to try again later."
  
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

if st.session_state["started"] == False:
  st.markdown("""Interviewing is hard! This is a tool to help you practice. It uses ChatGPT to ask five questions 
  related to the industry and job title, then ask if you have any questions. Every session is different. Interview 
  sessions are not logged or saved on the server.
  
  The questions are similar to a real interview, so use this to imagine your ideal responses. However, the simulator
  is friendly and always responds in an upbeat way, so don't expect actual interviews to be so pleasant. :smiley:

  You can leave the two fields, __Industry__ and __Job Title__, blank, which will result in generic interview questions.
  """)
  industry = st.text_input("Industry", key="industry")
  job_title = st.text_input("Job Title", key="job-title")
  start_button = st.button("Start", on_click=start_click)
else:
  st.markdown("If you like this tool, follow me on [LinkedIn](https://www.linkedin.com/in/boydellbown/) for updates.")
  end_button=st.button("Start Over", on_click=end_click)

  if st.session_state['generated']:
    # for i in range(len(st.session_state['generated'])-1, -1, -1):
    for i in range(0, len(st.session_state['generated'])):
      message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
      message(st.session_state['generated'][i], key=str(i))

  user_input=st.text_area("You:", key="user")
  chat_button=st.button("Send", on_click=chat_click)
