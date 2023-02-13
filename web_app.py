import os
import openai
import streamlit as st

# Get API key from environment variable
api_key = os.environ.get("API_KEY")
if api_key is None:
    raise ValueError("API_KEY environment variable not set")

# Set API key for OpenAI
openai.api_key = api_key

st.title("IEP Assist Premium")

# Add a sidebar with instructions
st.sidebar.title("Instructions")
st.sidebar.write("1. Select the student's grade level.")
st.sidebar.write("2. Select the student's qualifying condition.")
st.sidebar.write("3. Choose a prompt to generate a PLAAFP statement.")
st.sidebar.write("4. Enter student data.")
st.sidebar.write("5. Click the 'Analyze' button to generate the statement.")

st.sidebar.write("")
st.sidebar.write("")

st.sidebar.write("Note: This app uses OpenAI's GPT-3 API to generate the PLAAFP statement. Please enter data that is relevant and appropriate for generating the statement.")

# Add a horizontal line for separation
st.write("---")

# Select the student's grade level
st.write("Select the student's grade level:")
grade_level = st.selectbox("Grade:", ["K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], key="grade-level")

# Select the student's qualifying condition
st.write("Select the student's qualifying condition:")
qualifying_condition = st.multiselect("Qualifying Condition:", ["Specific Learning Disability", "Emotional Disturbance", "Autism", "Intellectual Disability", "Speech/Language Impairment", "Other Health Impairment", "Orthopedic Impairment", "Traumatic Brain Injury", "Deafness", "Blindness", "Developmental Delay"], key="qualifying-condition")

# Choose a prompt
st.write("Choose a prompt:")
prompts = [    "Analyze the data provided on the student and provide a summary of their strengths and areas of need in regards to their academic performance.",    "Provide a summary of the student's behavior data and suggest possible interventions to try based on their areas of need.",    "Summarize the data provided on the student's academic performance, highlighting their strengths and areas of need, and suggesting possible interventions to try."]
selected_prompt = st.selectbox("Prompt:", options=prompts, key="prompt")

st.write("Enter student data:")
student_data = st.text_area("Paste data here", height=250, key="student-data")

# Add a button to generate the PLAAFP statement
if st.button("Analyze", key="analyze-button"):
    # Set OpenAI API key
    openai.api_key = api_key

    # Call the OpenAI API and generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{selected_prompt} {student_data} {grade_level} {qualifying_condition}",
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.85,
    )

    # Extract the generated statement from the API response
    statement = response["choices"][0]["text"]

    # Show the generated statement
    st.write("PLAAFP statement:", statement)
