
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Add your API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Correct model name
model = genai.GenerativeModel("models/gemini-2.5-flash")

st.title("🌱 AgroGuard AI")
st.write("""
AgroGuard AI is an AI-powered plant disease detection system 
that helps farmers identify diseases early and prevent crop loss.
""")
st.subheader("AI-Based Plant Disease Detection")
st.write("Upload a plant leaf image to detect disease.")
st.write("### 🌿 Supported Plants")

st.write("""
- 🌾 Rice  
- 🍅 Tomato  
- 🥔 Potato  
- 🌹 Rose  
- 🍆 Brinjal  
- 🌽 Maize  
- 🥬 Spinach  
- 🌿 Mint  
""")

uploaded_file = st.file_uploader(
    "Upload Plant Leaf Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

# Resize image to make processing faster
    image = image.resize((512, 512))

    st.image(image, caption="Uploaded Image")

    if st.button("Detect Disease"):

        with st.spinner("Analyzing plant image..."):

            prompt = """
            You are an expert agricultural scientist.

            Analyze the plant leaf image carefully.

            Provide output in this format:

            Plant Name:
            Disease Name:
            Health Status:

            Treatment:
            - Step 1
            - Step 2

            Prevention:
            - Tip 1
            - Tip 2

            Severity Level:
            Low / Medium / High
            """

            # Generate response
            response = model.generate_content(
                [prompt, image]
            )

            st.success("Analysis Complete!")

            # Show result safely
            st.write(response.text)

# Risk Prediction

st.write("## 🌡 Risk Prediction")

temperature = st.number_input("Enter Temperature (°C)")
humidity = st.number_input("Enter Humidity (%)")

if st.button("Check Risk Level"):

    if temperature > 30 and humidity > 70:
        st.error("High Risk of Disease")

    elif temperature > 25 and humidity > 60:
        st.warning("Medium Risk of Disease")

    else:
        st.success("Low Risk of Disease")
