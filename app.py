import streamlit as st
import requests
import time

# Page configuration
st.set_page_config(page_title="Fake News Detector", layout="centered")

# Custom CSS for overall layout and styling with Helvetica, Arial, Sans Serif and centered submit button
st.markdown(
    """
    <style>
    /* Set global font family */
    * {
        font-family: Helvetica, Arial, sans-serif !important;
    }
    /* App background */
    .stApp {
        background-color: #232325;
    }
    /* Center the logo */
    .centered-logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 20px;
    }
    /* Welcome text styling */
    .welcome-text {
        text-align: center;
        font-size: 24px;
        color: #F2F2F2;
        margin-bottom: 0px;
    }
    /* Styling for the input text area */
    .stTextArea textarea {
        background-color: #2e2e30 !important;
        border: 2px solid #434345 !important;
        color: #F2F2F2 !important;
        font-size: 24px;
        border-radius: 10px !important;
        padding: 10px !important;
        width: 700px noresize !important;
        height: 400px noresize !important;
        resize: none !important;  /* Fixed size: disable resize */
    }

    /* Disclaimer checkbox styling */
    .custom-container .stCheckbox {
        margin-top: 10px;
        text-align: center;
        font-size: 24px;
    }
    .stCheckbox label {
        font-size: 24px;
    }
    /* Submit button styling: enlarged and centered */
    .custom-container .stButton button {
        align-items: center !important;
        display: block;
        margin: 20px auto 0 auto;
        font-size: 24px !important;
        padding: 12px 24px !important;
    }
    /* Result text styling */
    .result-text {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #F2F2F2;
        margin-top: 30px;
    }
    /* Change spinner color to white */
    [data-testid="stSpinner"] svg {
        stroke: #F2F2F2 !important;
    }
    /* Change progress bar color to white */
    [data-testid="stProgressBar"] > div > div {
        background-color: #F2F2F2 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo (SVG)
st.image(
    'Fake_News_Detector_w.svg', use_container_width=True
)

# Display welcome text between the logo and the text input
st.markdown(
    '<div class="welcome-text">Welcome to our app! Input an article and receive a prediction on whether or not it contains fake information.</div>',
    unsafe_allow_html=True
)

# Custom container for text area, disclaimer, and submit button
st.markdown('<div class="custom-container">', unsafe_allow_html=True)

# Text input area (fixed size, no resize)
text_input = st.text_area(
    label="",
    placeholder="Please paste the text of the news article here",
    height=200
)

# Disclaimer checkbox
disclaimer = st.checkbox(
    "Disclaimer: I acknowledge that the model does not fact-check the content of the news article but uses its linguistic patterns to classify it as fake or real. Our prediction should not be considered as definitive proof."
)

# Submit button (enlarged and centered)
submit = st.button("Submit")

st.markdown('</div>', unsafe_allow_html=True)

# When the submit button is clicked
if submit:
    if not text_input.strip():
        st.error("Please enter some text.")
    elif not disclaimer:
        st.error("Please acknowledge the disclaimer.")
    else:
        # Simulate a progress bar
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.005)
            progress_bar.progress(i)

        # API call to the Fake News Detector
        api_url = "https://fakenewsdocker-973308060059.europe-west1.run.app/predict"
        params = {"text": text_input}

        with st.spinner("Analyzing..."):
            try:
                response = requests.get(api_url, params=params, timeout=10)
                response.raise_for_status()
                result_json = response.json()
                # Expected API response:
                # {'Based on our current state-of-the-art algorithm, we predict that this text contains information that is': result}
                result = list(result_json.values())[0]
            except Exception as e:
                st.error(f"Error during API request: {e}")
                result = None

        # Display the result
        if result:
            # Map the API result: "true" remains "true", "fake" becomes "false"
            if result.lower() == "true":
                prediction = "true"
            elif result.lower() == "fake":
                prediction = "false"
            else:
                prediction = result

            st.markdown(
                f'<div class="result-text">Prediction: Based on our model, we predict that this article contains {prediction} information.</div>',
                unsafe_allow_html=True
            )
