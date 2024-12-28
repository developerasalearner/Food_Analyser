import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Streamlit page configuration
st.set_page_config(page_title="Personalized Health Advisor", page_icon="🍎", layout="wide")

# Custom CSS for styling the app
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-color: #f9f9f9;
    }
    .title {
        text-align: center;
        font-size: 36px;
        color: #4CAF50;
        margin-bottom: 20px;
    }
    .validation-success {
        color: green;
        font-weight: bold;
    }
    .validation-fail {
        color: red;
        font-weight: bold;
    }
    .intro-text {
        text-align: center;
        font-size: 18px;
        color: #333;
        margin-top: 20px;
    }
    .how-it-works {
        text-align: center;
        font-size: 16px;
        margin-top: 30px;
    }
    .future-features {
        text-align: center;
        font-size: 16px;
        color: #2196F3;
        margin-top: 30px;
    }
    .styled-details {
        font-size: 16px;
        line-height: 1.6;
        color: #333;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title and Header Image
st.markdown('<div class="title">Personalized Health Advisor</div>', unsafe_allow_html=True)
st.image("/Users/chinmayakumarpalo/Desktop/Food_Analyser/header_image.jpg", use_column_width=True)  # Replace with your header image URL

# Introduction Section
st.markdown("""
    <div class="intro-text">
    Welcome to the Personalized Health Advisor! This app helps you make informed decisions about your health based on the food you eat. 
    By entering simple details like your weight, height, and age, along with the food you consume, we provide personalized health recommendations. 
    Our app analyzes the nutritional value of the food, evaluates its suitability for your specific health profile, and gives you advice for a healthier lifestyle.
    </div>
""", unsafe_allow_html=True)

# How it Works Section
st.markdown("""
    <div class="how-it-works">
    **How it works:**
    1. Enter your weight, height, and age.
    2. Provide the name of the food you are consuming.
    3. Receive a detailed analysis of the food's nutritional value, macronutrient breakdown, and its impact on your health.
    4. Visualize the data in a tabular format and see the results in easy-to-understand charts.
    </div>
""", unsafe_allow_html=True)

# Future Features Section
st.markdown("""
    <div class="future-features">
    **Future Features:**
    - We're working on adding **camera access** to make the app even more convenient. Soon, you'll be able to simply take a photo of your food, and the app will automatically analyze it.
    - Stay tuned for more exciting updates that will help you lead a healthier lifestyle!
    </div>
""", unsafe_allow_html=True)

# Input fields
weight = st.number_input("Enter your weight (kg):", min_value=10, max_value=300, step=1)
if st.button("Validate Weight"):
    if 10 <= weight <= 300:
        st.markdown('<p class="validation-success">Weight is valid.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="validation-fail">Weight is out of range. Please adjust.</p>', unsafe_allow_html=True)
        st.stop()

height = st.number_input("Enter your height (ft):", min_value=3.0, max_value=8.0, step=0.1)
if st.button("Validate Height"):
    if 3.0 <= height <= 8.0:
        st.markdown('<p class="validation-success">Height is valid.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="validation-fail">Height is out of range. Please adjust.</p>', unsafe_allow_html=True)
        st.stop()

age = st.number_input("Enter your age (years):", min_value=1, max_value=150, step=1)
if st.button("Validate Age"):
    if 1 <= age <= 150:
        st.markdown('<p class="validation-success">Age is valid.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="validation-fail">Age is out of range. Please adjust.</p>', unsafe_allow_html=True)
        st.stop()

# Text input for food name
food_name = st.text_input("Enter the name of the food item:")

if food_name:
    st.write(f"Food item entered: {food_name}")
else:
    st.markdown('<p class="validation-fail">Please enter a food item name.</p>', unsafe_allow_html=True)
    st.stop()

# Analysis and output
if st.button("Analyze Data"):
    if not food_name:
        st.markdown('<p class="validation-fail">No valid food item provided for analysis.</p>', unsafe_allow_html=True)
        st.stop()

    # Enhanced analysis prompt
    analysis_prompt = f"""
    Based on the following inputs:
    - Weight: {weight} kg
    - Height: {height} ft
    - Age: {age} years
    - Food Item: {food_name}

    Please provide a detailed analysis of the food item including:
    1. Calories per serving
    2. Macronutrient breakdown (Carbs, Proteins, Fats)
    3. Vitamins and minerals
    4. Health benefits and potential risks
    5. Suitability for age, weight, and height
    6. Overall health recommendation
    """
    analysis_response = model.generate_content(analysis_prompt)
    analysis_text = analysis_response.text

    # Display the overall health recommendation in styled format
    st.markdown("<div class='styled-details'>### Health Recommendation</div>", unsafe_allow_html=True)
    st.write(analysis_text)
