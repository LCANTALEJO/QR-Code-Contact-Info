import streamlit as st
from io import BytesIO

# Set page config
st.set_page_config(page_title="Lyle Cantalejo Contact", page_icon="📇", layout="centered")

# --- Contact Information
name = "Lyle Cantalejo"
title = "Technical Service Manager"
company = "WEVO Chemical (Asia-Pacific) Pte. Ltd."
address_office = "German Centre, Office #04-13/14\n25 International Business Park\nSingapore, 609916"
email_work = "Lyle.Cantalejo@wevochemical.com"
email_personal = "Lyle.Cantalejo@gmail.com"
phone_sg = "+65 6990 9594"
phone_ph = "+63 945 170 2105"
emergency_contact = "Geejay T. Cantalejo"
emergency_phone = "+63 906 236 9758"
emergency_address = "Lot 8, Block 23, Phase 4A, San Antonio Heights, Santo Tomas, Batangas 4234"

# Main container
with st.container():
    st.image("Lyle Photo.jpg", width=180)

    st.markdown(
        f"""
        <h2 style='text-align: center; margin-bottom: 0;'>{name}</h2>
        <h4 style='text-align: center; color: gray; margin-top: 0;'>{title}</h4>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("📍 Company")
    st.markdown(f"**{company}**  \n{address_office}", unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("📧 Emails")
    st.markdown(
        f"""
        [📨 {email_work}](mailto:{email_work})  
        [📨 {email_personal}](mailto:{email_personal})
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("📞 Phone Numbers")
    st.markdown(
        f"""
        [📱 {phone_sg} (Singapore)](tel:{phone_sg.replace(' ', '')})  
        [📱 {phone_ph} (Philippines)](tel:{phone_ph.replace(' ', '')})
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("🚨 Emergency Contact")
    st.markdown(
        f"""
        **{emergency_contact}**  
        [📱 {emergency_phone}](tel:{emergency_phone.replace(' ', '')})  
        {emergency_address}
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --- Create vCard string ---
    vcard = f"""
BEGIN:VCARD
VERSION:3.0
N:Cantalejo;Lyle;;;
FN:Lyle Cantalejo
ORG:{company}
TITLE:{title}
TEL;TYPE=WORK,VOICE:{phone_sg.replace(' ', '')}
TEL;TYPE=CELL,VOICE:{phone_ph.replace(' ', '')}
EMAIL;TYPE=WORK:{email_work}
EMAIL;TYPE=HOME:{email_personal}
ADR;TYPE=WORK:;;German Centre, Office #04-13/14, 25 International Business Park;Singapore;;609916;Singapore
END:VCARD
    """.strip()

    vcard_bytes = BytesIO(vcard.encode())

    st.download_button(
        label="📇 Download Contact Card (vCard)",
        data=vcard_bytes,
        file_name="Lyle_Cantalejo_Contact.vcf",
        mime="text/vcard"
    )

    st.caption("Made with ❤️ by Lyle Cantalejo • Powered by Streamlit")

