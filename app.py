import streamlit as st
import base64
from io import BytesIO

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Lyle Cantalejo Contact", page_icon="📇", layout="centered")

# --- LOAD and ENCODE LOCAL PHOTO ---
def get_base64_image(img_path):
    with open(img_path, "rb") as img_file:
        img_bytes = img_file.read()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

img_base64 = get_base64_image("Lyle Photo.jpg")

# --- DISPLAY CENTERED PROFILE PHOTO ---
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/jpeg;base64,{img_base64}' width='220' style='border-radius: 20px;'>
    </div>
    """,
    unsafe_allow_html=True
)

# --- NAME and TITLE ---
st.markdown(
    """
    <h2 style='text-align: center; margin-bottom: 0;'>Lyle Cantalejo</h2>
    <h4 style='text-align: center; color: gray; margin-top: 0;'>Technical Service Manager</h4>
    """,
    unsafe_allow_html=True
)

# st.markdown("---")

# --- COMPANY INFORMATION ---
#st.subheader("📍 Company")
st.markdown(
    """
    <div style='text-align: left; font-size:20px;'>
    <strong>WEVO Chemical (Asia-Pacific) Pte. Ltd.</strong><br>
    <span style='font-size:20px;'>German Centre, Office #04-13/14<br>
    25 International Business Park<br>
    Singapore, 609916</span>
    </div>
    """,
    unsafe_allow_html=True
)

#st.markdown("---")

# --- EMAILS ---
#st.subheader("📧 Emails")
st.markdown(
    """
    <div style='text-align: left; font-size:20px;'>
     <a href="mailto:Lyle.Cantalejo@wevochemical.com">Lyle.Cantalejo@wevochemical.com</a><br>
     <a href="mailto:Lyle.Cantalejo@gmail.com">Lyle.Cantalejo@gmail.com</a>
    </div>
    """,
    unsafe_allow_html=True
)

#st.markdown("---")

# --- PHONE NUMBERS ---
#st.subheader("📞 Phone Numbers")
st.markdown(
    """
    <div style='text-align: left; font-size:20px;'>
     <a href="tel:+6569909594">+65 6990 9594 (Singapore)</a><br>
     <a href="tel:+639451702105">+63 945 170 2105 (Philippines)</a>
    </div>
    """,
    unsafe_allow_html=True
)

#st.markdown("---")

# --- EMERGENCY CONTACT ---
st.subheader("Emergency Contact")
st.markdown(
    """
    <div style='text-align: left; font-size:20px;'>
    <strong>Geejay T. Cantalejo</strong><br>
     <a href="tel:+639062369758">+63 906 236 9758</a><br>
    Lot 8, Block 23, Phase 4A, San Antonio Hts<br>
    Sto. Tomas, Batangas 4234
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- CREATE VCARD FILE ---
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

# --- DOWNLOAD BUTTON FOR VCARD ---
st.download_button(
    label="📇 Download Contact Card (vCard)",
    data=vcard_bytes,
    file_name="Lyle_Cantalejo_Contact.vcf",
    mime="text/vcard"
)

# --- FOOTER ---
st.caption("Made with ❤️ by Lyle Cantalejo • Powered by Streamlit")

