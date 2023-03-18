import streamlit as st
import streamlit.components.v1 as components

st.title("AI Resume Builder")
st.markdown("""
We are excited to announce that a new web application is currently in progress of being created that will utilize
ChatGPT to assist users in creating professional resumes. With the help of artificial intelligence, users will be
able to generate custom resumes with ease and precision.

## Features:

1. AI-powered resume builder: Users can input their personal details and work experience, and the ChatGPT algorithm
will generate a professional resume that is tailored to the user's unique qualifications and skill set.

2. Customizable templates: The application will offer a variety of templates for users to choose from, allowing them
to further customize the design and layout of their resume to fit their personal preferences.

3. Keyword optimization: The algorithm will analyze the job posting to which the user is applying and optimize the 
user's resume to include relevant keywords and phrases to increase the likelihood of being selected for an interview.

4. Easy editing: Users will have the ability to make edits and updates to their resume at any time, and the algorithm 
will seamlessly incorporate any changes made.

5. Save and download: Once the user is satisfied with their resume, they can save and download it in multiple file 
formats for easy sharing and submission.

Please note that this application is still in development and additional features may be added as the project progresses. 
If you would like to be notified about the official launch of this innovative new tool for job seekers, please enter 
your information below.
""")

components.iframe("https://docs.google.com/forms/d/e/1FAIpQLSeWfDjuaT0X7yLT4PuGSh8dYuA9z3yWQqGwGgLgrKFhp8EH4w/viewform?embedded=true", 
  width=640, height=780)
