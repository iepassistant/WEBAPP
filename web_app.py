import openai
import streamlit as st
import config

# Set OpenAI API key
openai.api_key = config.api_key

st.markdown(
    """
    <style>
    /* Add your CSS code here */
    </style>
    """,
    unsafe_allow_html=True,
)

def write_iep():
    st.title("IEP Assist")

def write_sidebar():
    st.sidebar.title("What is IEP Assist?")
    st.sidebar.info(
        "IEP Assist generates responses using OpenAI's language generation technology. The technology uses machine learning algorithms trained on large amounts of text data to generate new text based on a given prompt. In the case of IEP Assist, the prompt consists of the student data entered by the user (academic, functional, behavioral information), and the technology generates a Present Levels of Academic Achievement and Functional Performance (PLAAFP) for the student based on the data.")
        
    # Add a text area
    user_query = st.text_area("Enter student data (ie. academic, functional, behavioral). To ensure that the generated PLAAFP statement accurately reflects the student's needs and abilities, it is important to provide as much relevant information as possible:", height=250)

    # Add a submit button
    if st.button("Analyze"):
        # Use OpenAI to generate IEP based on student
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt= "You are a special education case manager, the following data has been collected. Analyze and summarize this data into a cohesive PLAAFP statement, make it clear and concise and provide areas of strength and areas of need and strageties to improve areas of need: \n" + user_query,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.8
        )
        iep = response["choices"][0]["text"]
        st.write(iep)

def main():
    write_iep()
    write_sidebar()

if __name__ == "__main__":
    main()