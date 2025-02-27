import streamlit as st
from PIL import Image
import base64


# Custom CSS for modern styling with adjusted colors and backgrounds
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Set purple as the official accent color */
    :root {
        --accent-color: #7B44F2;
        --accent-dark: #6233C1;
        --accent-light: #9D74F4;
        --background-light: #EFF1F5;
        --text-on-dark: #FFFFFF;
        --text-primary: #F9FAFB;
        --text-secondary: #E5E7EB;
        --card-bg: #283142;
    }
    
    /* Make content stand out against Streamlit's background */
    .main .block-container {
        padding-top: 2rem;
    }
    
    .main-header {
        font-size: 3.2rem !important;
        font-weight: 700 !important;
        background: linear-gradient(90deg, var(--accent-color), var(--accent-light));
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        margin-bottom: 0.5rem !important;
    }
    
    .sub-header {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        margin-bottom: 1rem !important;
    }
    
    /* Adjust card background to be less stark against Streamlit background */
    .feature-card {
        border-radius: 12px !important;
        padding: 1.5rem !important;
        background-color: var(--card-bg) !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.15) !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
        border: 1px solid rgba(123, 68, 242, 0.2) !important;
    }
    
    .feature-card:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2) !important;
        border: 1px solid var(--accent-color) !important;
    }
    
    .feature-title {
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        margin-top: 1rem !important;
        font-size: 1.3rem !important;
    }
    
    .feature-description {
        color: var(--text-secondary) !important;
        font-size: 1rem !important;
        line-height: 1.5 !important;
    }
    
    .cta-button {
        background-color: var(--accent-color) !important;
        color: var(--text-on-dark) !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        transition: background-color 0.3s ease !important;
    }
    
    .cta-button:hover {
        background-color: var(--accent-dark) !important;
    }
    
    .form-container {
        background-color: var(--card-bg) !important;
        border-radius: 12px !important;
        padding: 2rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
        color: var(--text-primary) !important;
        border: 1px solid rgba(123, 68, 242, 0.2) !important;
    }
    
    .footer {
        padding: 2rem 0 !important;
        border-top: 1px solid rgba(123, 68, 242, 0.2) !important;
        margin-top: 3rem !important;
    }
    
    .footer-link {
        color: var(--text-secondary) !important;
        text-decoration: none !important;
        transition: color 0.2s ease !important;
        font-weight: 500 !important;
        padding: 0.5rem 1rem !important;
    }
    
    .footer-link:hover {
        color: var(--accent-color) !important;
    }
    
    .copyright {
        color: var(--text-secondary) !important;
        font-size: 0.875rem !important;
        margin-top: 1rem !important;
    }
    
    .mission-text {
        font-size: 1.1rem !important;
        line-height: 1.7 !important;
        color: var(--text-secondary) !important;
    }
    
    /* Geometric background patterns like Squarespace */
    .geometric-bg {
        position: relative;
        overflow: hidden;
        z-index: 1;
    }
    
    .geometric-bg::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(123, 68, 242, 0.15) 0%, transparent 20%),
            radial-gradient(circle at 85% 60%, rgba(123, 68, 242, 0.1) 0%, transparent 30%),
            radial-gradient(circle at 40% 80%, rgba(123, 68, 242, 0.05) 0%, transparent 25%);
        z-index: -1;
    }
    
    .wave-bg {
        position: relative;
        overflow: hidden;
        z-index: 1;
    }
    
    .wave-bg::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 320'%3E%3Cpath fill='%237B44F2' fill-opacity='0.05' d='M0,224L48,208C96,192,192,160,288,144C384,128,480,128,576,149.3C672,171,768,213,864,224C960,235,1056,213,1152,181.3C1248,149,1344,107,1392,85.3L1440,64L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z'%3E%3C/path%3E%3C/svg%3E");
        background-size: cover;
        background-position: center;
        z-index: -1;
        opacity: 0.8;
    }
    
    .dots-bg {
        position: relative;
        overflow: hidden;
        z-index: 1;
    }
    
    .dots-bg::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: radial-gradient(var(--accent-color) 1px, transparent 1px);
        background-size: 20px 20px;
        opacity: 0.05;
        z-index: -1;
    }
    
    .stMarkdown, .stForm, .stText, p, h1, h2, h3 {
        color: var(--text-primary) !important;
    }
    
    /* Style for stat cards */
    .stat-card {
        background-color: var(--card-bg) !important;
        border: 5px solid rgba(123, 68, 242, 0.2) !important;
        border-radius: 10px !important;
        padding: 1.5rem !important;
        text-align: center !important;
    }
    
    /* Streamlit form fields styling */
    .stTextInput > div > div > input, 
    .stSelectbox > div > div > select {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(123, 68, 242, 0.3) !important;
    }
    
    .stTextInput > div > div > input:focus, 
    .stSelectbox > div > div > select:focus {
        border: 1px solid var(--accent-color) !important;
    }
    
    /* Light text placeholders */
    input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }
    
    /* Custom container styling */
    div[data-testid="stVerticalBlock"] > div:has(> div.element-container div.stMarkdown) {
        background-color: transparent;
        padding: 0;
        border-radius: 0;
    }
</style>
""", unsafe_allow_html=True)

# Create a placeholder for your logo
def get_placeholder_logo(text="RG", size=(150, 150), bg_color="#7B44F2", text_color="white"):
    from PIL import Image, ImageDraw, ImageFont
    import io
    
    # Create a new image with the specified background color
    img = Image.new('RGB', size, color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Use a default font since custom fonts might not be available
    try:
        # This attempts to use a system font if available
        font = ImageFont.truetype("Arial", size[0] // 2)
    except IOError:
        font = ImageFont.load_default()
    
    # Calculate text position to center it
    text_width, text_height = draw.textsize(text, font=font) if hasattr(draw, 'textsize') else (size[0]//3, size[1]//3)
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    
    # Draw the text
    draw.text(position, text, fill=text_color, font=font)
    
    # Convert the image to bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return img_byte_arr.getvalue()

# Header section with logo and navigation
st.markdown('<div class="geometric-bg">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    logo = get_placeholder_logo(text="RG", size=(100, 100))
    st.image(logo, width=80)
with col2:
    st.markdown('<h1 class="main-header">Research Genie</h1>', unsafe_allow_html=True)

# Main navigation
st.markdown("""
<div style="display: flex; justify-content: flex-end; margin-bottom: 2rem;">
    <a href="/home" style="text-decoration: none; color: #E5E7EB; font-weight: 500; margin-left: 1rem;">Home</a>
    <a href="/search" style="text-decoration: none; color: #E5E7EB; font-weight: 500; margin-left: 1rem;">Search</a>
    <a href="/news" style="text-decoration: none; color: #E5E7EB; font-weight: 500; margin-left: 1rem;">News</a>
    <a href="/more" style="text-decoration: none; color: #E5E7EB; font-weight: 500; margin-left: 1rem;">Learn More</a>
</div>
""", unsafe_allow_html=True)

# Hero section with unique background
st.markdown("""
<div style="background: linear-gradient(135deg, rgba(49, 46, 129, 0.6), rgba(76, 29, 149, 0.6)); padding: 3rem; border-radius: 12px; margin-bottom: 3rem; position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; z-index: -1; background-image: url('data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 86c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm28-65c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm23-11c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-6 60c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm29 22c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zM32 63c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm57-13c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-9-21c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM60 91c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM35 41c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM12 60c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2z' fill='%237B44F2' fill-opacity='0.1' fill-rule='evenodd'/%3E%3C/svg%3E'); background-size: 150px 150px;"></div>
    <h2 style="font-size: 2.5rem; font-weight: 700; color: #FFFFFF; margin-bottom: 1rem;">Your Personal Research Assistant</h2>
    <p style="font-size: 1.2rem; color: #E5E7EB; max-width: 700px; line-height: 1.6;">
        Discover, analyze, and organize scholarly research with the power of AI. ResearchGenie helps you find relevant papers and insights with unprecedented precision.
    </p>
    <button style="background-color: #7B44F2; color: white; border: none; border-radius: 8px; padding: 0.75rem 1.5rem; font-weight: 600; margin-top: 1rem; cursor: pointer;">Get Started</button>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# About Us section with wave background
st.markdown('<div class="wave-bg">', unsafe_allow_html=True)
about_us = st.container()
with about_us:
    st.markdown('<h2 class="sub-header">Our Mission</h2>', unsafe_allow_html=True)
    st.markdown("""
    <p class="mission-text">
        At ResearchGenie, our mission is to revolutionize the way researchers explore,
        source, and synthesize academic knowledge. We strive to empower researchers with 
        an intelligent AI-driven search engine that simplifies the discovery of relevant 
        papers, helping them navigate vast repositories of scholarly work with precision 
        and ease. By streamlining the process of finding and organizing references, 
        ResearchGenie serves as a trusted research companion, enabling academics and 
        professionals to focus on what truly matters: advancing knowledge, fostering 
        innovation, and contributing to their fields. Our goal is to make research 
        accessible, efficient, and inspiring, paving the way for groundbreaking discoveries.
    </p>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# What We Do section with dots background
st.markdown('<div class="dots-bg">', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">What We Do</h2>', unsafe_allow_html=True)

# Feature cards with improved layout and darker backgrounds
cols = st.columns(3)

features = [
    {
        "title": "Smart Search",
        "description": "Helping experts around the world continue their research with AI-powered discovery tools.",
        "icon": "🔍"
    },
    {
        "title": "Academic Contribution",
        "description": "Setting up for success by providing research grants for winning papers and innovative studies.",
        "icon": "🏆"
    },
    {
        "title": "Collaboration",
        "description": "Share your work and collaborate with other experts in your field through our platform.",
        "icon": "🤝"
    }
]

for i, col in enumerate(cols):
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <div style="font-size: 3rem; color: #7B44F2; text-align: center;">{features[i]['icon']}</div>
            <h3 class="feature-title" style="text-align: center;">{features[i]['title']}</h3>
            <p class="feature-description" style="text-align: center;">{features[i]['description']}</p>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Sign-Up Form Section with geometric background
st.markdown('<div class="geometric-bg">', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">Join Our Research Community</h2>', unsafe_allow_html=True)
st.markdown("""
<p style="font-size: 1.1rem; color: #E5E7EB; margin-bottom: 2rem;">
    Stay informed about the latest updates, research trends, and news from ResearchGenie!
</p>
""", unsafe_allow_html=True)

# Modern form
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    with st.form("signup_form", clear_on_submit=True):
        st.markdown('<h3 style="font-size: 1.5rem; font-weight: 600; color: #F9FAFB; margin-bottom: 1.5rem;">Sign Up for Updates</h3>', unsafe_allow_html=True)
        name = st.text_input("Your Name", placeholder="Enter your full name")
        email = st.text_input("Your Email", placeholder="Enter your email address")
        research_field = st.selectbox("Research Field", ["", "Computer Science", "Medicine", "Physics", "Biology", "Economics", "Psychology", "Other"])
        subscribe = st.checkbox("Subscribe to our newsletter")
        
        col1, col2 = st.columns(2)
        with col1:
            submit_button = st.form_submit_button("Sign Up", use_container_width=True)
        with col2:
            st.markdown('<div style="margin-top: 10px; font-size: 0.8rem; color: #E5E7EB;">We respect your privacy.</div>', unsafe_allow_html=True)
        
        if submit_button:
            if name and email and subscribe:
                st.success(f"Thank you, {name}! You've successfully signed up for updates.")
            else:
                st.error("Please complete the form and check the subscription box to sign up.")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Statistics section with wave background
st.markdown('<div class="wave-bg">', unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="padding: 2rem; border-radius: 12px; margin: 3rem 0;">
    <h2 style="text-align: center; font-size: 1.8rem; font-weight: 600; color: #F9FAFB; margin-bottom: 2rem;">ResearchGenie in Numbers</h2>
    <div style="display: flex; justify-content: space-around; text-align: center; flex-wrap: wrap;">
        <div class="stat-card" style="flex: 1; margin: 0 10px; min-width: 200px;">
            <h3 style="font-size: 2.5rem; font-weight: 700; color: #7B44F2; margin-bottom: 0.5rem;">500K+</h3>
            <p style="color: #E5E7EB; font-size: 1.1rem;">Research Papers</p>
        </div>
        <div class="stat-card" style="flex: 1; margin: 0 10px; min-width: 200px;">
            <h3 style="font-size: 2.5rem; font-weight: 700; color: #7B44F2; margin-bottom: 0.5rem;">50K+</h3>
            <p style="color: #E5E7EB; font-size: 1.1rem;">Researchers</p>
        </div>
        <div class="stat-card" style="flex: 1; margin: 0 10px; min-width: 200px;">
            <h3 style="font-size: 2.5rem; font-weight: 700; color: #7B44F2; margin-bottom: 0.5rem;">100+</h3>
            <p style="color: #E5E7EB; font-size: 1.1rem;">Universities</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer section with geometric dots background
st.markdown('<div class="dots-bg">', unsafe_allow_html=True)
st.markdown("""
<footer class="footer">
    <div style="display: flex; justify-content: center; flex-wrap: wrap; margin-bottom: 1rem;">
        <a href="/home" class="footer-link">Home</a>
        <a href="/search" class="footer-link">Search</a>
        <a href="/news" class="footer-link">News</a>
        <a href="/more" class="footer-link">Learn More</a>
        <a href="/privacy" class="footer-link">Privacy Policy</a>
        <a href="/terms" class="footer-link">Terms of Service</a>
        <a href="/contact" class="footer-link">Contact Us</a>
    </div>
    <div style="text-align: center; margin-top: 1rem;">
        <div style="display: flex; justify-content: center; gap: 1rem; margin-bottom: 1rem;">
            <span style="font-size: 1.5rem; color: #E5E7EB;">📱</span>
            <span style="font-size: 1.5rem; color: #E5E7EB;">💻</span>
            <span style="font-size: 1.5rem; color: #E5E7EB;">📧</span>
        </div>
        <p class="copyright">&copy; 2025 ResearchGenie Inc. All rights reserved.</p>
    </div>
</footer>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)