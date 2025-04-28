import streamlit as st
import base64
from io import BytesIO

# Set page config
st.set_page_config(page_title="Lyle Cantalejo Contact", page_icon="📇", layout="centered")

# --- Load and Encode the Local Image
def get_base64_image(img_path):
    with open(img_path, "rb") as img_file:
        img_bytes = img_file.read()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

img_base64 = get_base64_image("Lyle Photo.jpg")

# --- Display Centered Image
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/jpeg;base64,{img_base64}' width='220' style='border-radius: 15px;'>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Continue with the rest of the app
st.markdown(
    """
    <h2 style='text-align: center; margin-bottom: 0;'>Lyle Cantalejo</h2>
    <h4 style='text-align: center; color: gray; margin-top: 0;'>Technical Service Manager</h4>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# (Continue with your sections for company, emails, phones, emergency contact...)

# (And your Download vCard Button)
