import streamlit as st
import streamlit.components.v1 as components
from transformers import pipeline
import time



def main():
    st.header("Phantom Tutor")
    st.markdown(
        """
This demo app is using for LLM-based tutors.
The models sources include HuggingFace and OpenAI.
Supports hard sciences (computer science, analytics, and math). Visuals (graphs, data tables) can be generated with prompts.
There are two windows "summarize" and "explain".
"""
    )
    
    
    computer_science = "Computer Science"
    data_analytics = "Data Analytics"
    math = "Math"
    app_mode = st.selectbox("Choose the app mode", [computer_science, data_analytics, math])

    if app_mode == computer_science :
        model = pipeline('summarization')
    elif app_mode == data_analytics :
        model = pipeline('summarization')   
    elif app_mode == math:
        model = pipeline('summarization')


model = pipeline('summarization')        
main()        
        
article = "Anger and confusion overflowed at the Olympic mixed-team ski jumping final in China after five female competitors were disqualified from the event by officials who said their jumpsuits didn't comply with the rules."
input = st.text_area("Insert Text", article)

# Create an iframe to display a webpage of the user's choice
url = st.text_input("Enter the URL of the webpage you want to display")
components.iframe(url, width=800, height=600)

with st.spinner('Wait for it...'):
    summarizer = model
    summarized_text = summarizer(input, min_length = 20,  max_length = 120, do_sample=False)[0]['summary_text']
    
st.success('Done!')

# Display the summarized text
st.write(summarized_text)


