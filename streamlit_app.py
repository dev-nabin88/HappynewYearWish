import streamlit as st
from datetime import datetime
import time


# Set page config for a modern look
st.set_page_config(
    page_title="New Year Wishes 2025",
    page_icon="🎉",
    layout="centered"

)

image_path = "WhatsApp Image 2024-12-31 at 23.25.20_1cea4870.jpg"
# Custom CSS for modern styling
st.markdown("""
   <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');


@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.stApp {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96C93D, #FED766);
    background-size: 300% 300%;
    animation: gradient 10s ease infinite;
}

.stTextInput > label {
    font-family: 'Poppins', sans-serif;
    color: white !important;
    font-size: 1.2rem !important;
}

.big-font {
    font-family: 'Poppins', sans-serif;
    color: white;
    font-size: 2.5rem !important;
    font-weight: 600;
    text-align: center;
    margin-bottom: 2rem;
}

.wish-text {
    font-family: 'Poppins', sans-serif;
    color: white;
    font-size: 1.8rem !important;
    text-align: center;
    padding: 2rem;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 15px;
    backdrop-filter: blur(10px);
    margin: 2rem 0;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
}

.sparkles {
    font-size: 2rem;
    margin: 0 0.5rem;
}



""", unsafe_allow_html=True)

# Title with custom styling
st.markdown('<p class="big-font">✨🎉 New Year Wishes 2025 🎉✨</p>', unsafe_allow_html=True)

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
            <span class="sparkles">✨</span>
            Dear {name},<br><br>
            May the New Year 2025 bring you<br>
            endless joy, success, and wonderful moments!<br><br>
            Wishing you 365 days of happiness!
            <span class="sparkles">✨</span>
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



