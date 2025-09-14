import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Vindhya IT Consultancy & Services",
                   page_icon="💻",
                   layout="wide")

# --- Hero Section ---
st.markdown(
    """
    <div style="text-align:center; padding:40px 0;">
        <h1 style="color:#1E3A8A;">Vindhya IT Consultancy & Services</h1>
        <h3>Innovating. Optimizing. Delivering. Excellence.</h3>
        <p style="font-size:18px;">Your trusted partner in IT Consulting, Cloud, and Automation Solutions.</p>
        <a href="#contact"><button style="padding:10px 20px; font-size:16px; border-radius:8px; background:#1E3A8A; color:white; border:none;">Get in Touch</button></a>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("---")

# --- About Us ---
st.header("About Us")
st.write("""
At **Vindhya IT Consultancy & Services**, we help businesses achieve their digital transformation goals.
Our team of experts specializes in IT strategy, cloud adoption, data solutions, and automation to
drive efficiency and growth.
""")

st.write("---")

# --- Services ---
st.header("Our Services")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💼 IT Consulting")
    st.write("End-to-end IT strategy, planning, and execution tailored to your business needs.")

with col2:
    st.subheader("☁️ Cloud Solutions")
    st.write("Deploy, migrate, and optimize cloud environments for scalability and cost savings.")

with col3:
    st.subheader("⚙️ Automation")
    st.write("Streamline operations with automation tools and Ansible/DevOps pipelines.")

st.write("---")

# --- Testimonials ---
st.header("What Our Clients Say")
st.info("⭐ 'Vindhya IT made our cloud migration seamless and efficient.' – Client A")
st.info("⭐ 'Their consulting services helped optimize our IT costs by 30%.' – Client B")
st.info("⭐ 'We rely on their automation expertise for critical deployments.' – Client C")

st.write("---")

# --- Contact Section ---
st.header("📞 Contact Us")
st.write("We’d love to hear from you! Fill in your details below:")

with st.form("contact_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success(f"Thank you {name}, we will reach out to you at {email} soon!")

st.write("📍 Location: Mirzapur, Uttar Pradesh, India")
st.write("✉️ Email: info@vindhyait.com")
st.write("📞 Phone: +91-XXXXXXXXXX")

st.write("---")
st.caption("© 2025 Vindhya IT Consultancy & Services. All Rights Reserved.")
