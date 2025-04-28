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

# --- Now NORMAL Streamlit Components start properly
st.markdown("")  # (blank line for safety)

# Display Name and Title
st.markdown(
    """
    <h2 style='text-align: center; margin-bottom: 0;'>Lyle Cantalejo</h2>
    <h4 style='text-align: center; color: gray; margin-top: 0;'>Technical Service Manager</h4>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Company Information
st.subheader("📍 Company")
st.write("""
**WEVO Chemical (Asia-Pacific) Pte. Ltd.**  
German Centre, Office #04-13/14  
25 International Business Park  
Singapore, 609916
""")

st.markdown("---")

# Emails
st.subheader("📧 Emails")
st.markdown(
    """
    [📨 Lyle.Cantalejo@wevochemical.com](mailto:Lyle.Cantalejo@wevochemical.com)  
    [📨 Lyle.Cantalejo@gmail.com](mailto:Lyle.Cantalejo@gmail.com)
    """, unsafe_allow_html=True)

st.markdown("---")

# Phone Numbers
st.subheader("📞 Phone Numbers")
st.markdown(
    """
    [📱 +65 6990 9594 (Singapore)](tel:+6569909594)  
    [📱 +63 945 170 2105 (Philippines)](tel:+639451702105)
    """, unsafe_allow_html=True)

st.markdown("---")

# Emergency Contact
st.subheader("🚨 Emergency Contact")
st.write("""
**Geejay T. Cantalejo**  
📱 +63 906 236 9758  
Lot 8, Block 23, Phase 4A, San Antonio Heights  
Santo Tomas, Batangas 4234
""")

st.markdown("---")

# Create vCard for download
vcard = f"""
BEGIN:VCARD
VERSION:3.0
N:Cantalejo;Lyle;;;
FN:Lyle Cantalejo
ORG:WEVO Chemical (Asia-Pacific) Pte. Ltd.
TITLE:Technical Service Manager
TEL;TYPE=WORK,VOICE:+6569909594
TEL;TYPE=CELL,VOICE:+639451702105
EMAIL;TYPE=WORK:Lyle.Cantalejo@wevochemical.com
EMAIL;TYPE=HOME:Lyle.Cantalejo@gmail.com
ADR;TYPE=WORK:;;German Centre, Office #04-13/14, 25 International Business Park;Singapore;;609916;Singapore
END:VCARD
""".strip()

vcard_bytes = BytesIO(vcard.encode())

# Download Button
st.download_button(
    label="📇 Download Contact Card (vCard)",
    data=vcard_bytes,
    file_name="Lyle_Cantalejo_Contact.vcf",
    mime="text/vcard"
)

st.caption("Made with ❤️ by Lyle Cantalejo • Powered by Streamlit")
