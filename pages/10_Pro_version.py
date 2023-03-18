import streamlit as st
import streamlit.components.v1 as components

st.title("Interview Simulator Pro")
st.markdown("""
We are working on a professional version of this application that will do more than just give you questions.
It will also be designed to grant a score on the quality of your answers, and generate feedback on how you
could improve.

# Possible features
1. Use the GPT 4 API, which could respond in more realistic ways.
2. If your responses to the question are incomplete, or lacking in details, ask follow-up questions.
3. Generate a score from 1 to 100 based on the quality of your responses.
4. Provide feedback on areas that could use improvement.

This tool would use a credits model, with each interview session likely costing between \$1.00 to \$5.00, depending
on the length of the session.

If you would like to be notified when this tool becomes available, please enter your email address below.
Early entries could be granted free Beta access.
""")

components.iframe("https://docs.google.com/forms/d/e/1FAIpQLSf86CaKicj9KRO4MoSbcL08dSj6NxOxQcctYqHIuV_QAMYCuA/viewform?embedded=true", 
  width=640, height=760)
