import streamlit as st

# Add CSS to add background image to the app
st.markdown("""
    <style>
        body {
            background-image: url("https://images.pexels.com/photos/461077/pexels-photo-461077.jpeg?cs=srgb&dl=pexels-picjumbocom-461077.jpg&fm=jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)



# Add title to the app
st.markdown(
    """
    <style>
        .title {
            font-size: 70px;
            font-weight: bold;
            color: #333333;
            text-shadow: 2px 2px #dddddd;
            text-align: center;
            margin-top: 50px;
            margin-bottom: 20px;
        }
        
        .subtitle {
            font-size: 40px;
            font-weight: normal;
            color: #111111;
            text-align: center;
            margin-bottom: 50px;
        }
    </style>
    
    <h1 class="title">Laptop Price Predictor</h1>
    <p class="subtitle">Analyze and predict laptop prices with machine learning</p>
    """,
    unsafe_allow_html=True
)
