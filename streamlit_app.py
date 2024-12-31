import streamlit as st
from datetime import datetime
import time

# Set page config for a modern look
st.set_page_config(
    page_title="New Year Wishes 2025",
    page_icon="🎉",
    layout="centered"
)

# Path to your uploaded image
image_path = "WhatsApp Image 2024-12-31 at 23.25.20_1cea4870.jpg"

# Custom CSS to set the uploaded image as background
st.markdown(f"""
   <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

.stApp {{
    background: url(data:image/jpeg;base64,{open(image_path, "rb").read().encode("base64").decode()}) no-repeat center center fixed;
    background-size: cover;
    color: white;
    font-family: 'Poppins', sans-serif;
}}

.big-font {{
    font-size: 2.5rem;
    font-weight: 600;
    text-align: center;
    margin-bottom: 2rem;
}}

.wish-text {{
    font-size: 1.8rem;
    text-align: center;
    padding: 2rem;
    background: rgba(0, 0, 0, 0.5);
    border-radius: 15px;
    margin: 2rem 0;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
}}
</style>
""", unsafe_allow_html=True)

# Title with custom styling
st.markdown('<p class="big-font">✨ New Year Wishes 2025 ✨</p>', unsafe_allow_html=True)

# Input field for name
name = st.text_input("Enter your name", key="name_input")

# Button to generate wish
if st.button("Generate Wish", key="wish_button"):
    if name:
        # Create a progress bar for animation effect
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)
        
        # Display the wish with animation
        wish = f"""
        <div class="wish-text">
            <span>✨</span>
            Dear {name},<br><br>
            May the New Year 2025 bring you<br>
            endless joy, success, and wonderful moments!<br><br>
            Wishing you 365 days of happiness!
            <span>✨</span>
        </div>
        """
        st.markdown(wish, unsafe_allow_html=True)
        
        # Add confetti effect
        st.balloons()
    else:
        st.warning("Please enter your name to generate the wish!")

# Footer
st.markdown("---")
current_year = datetime.now().year
st.markdown(
    f'<p style="text-align: center; color: white;">© {current_year} | Made with ❤️ by nabin</p>',
    unsafe_allow_html=True
)




