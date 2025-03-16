import streamlit as st
from PIL import Image
import base64
import io

# Custom CSS for dark theme based on the image colors
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Define our new color palette based on the dark image */
    :root {
        --background-dark: #1e1e25; /* Dark background from image */
        --background-darker: #121218; /* Darker part from image */
        --accent-color: #4a4a5a; /* Muted accent color */
        --accent-light: #6e6e82; /* Lighter accent */
        --text-on-dark: #ffffff; /* White text for dark backgrounds */
        --text-primary: #e0e0e5; /* Light text */
        --text-secondary: #a0a0b0; /* Muted text */
        --card-bg: #282833; /* Slightly lighter than background for cards */
    }
    
    /* Overall background and text color */
    .stApp {
        background-color: var(--background-dark);
        color: var(--text-primary);
    }
    
    /* Make content stand out against Streamlit's background */
    .main .block-container {
        padding-top: 2rem;
    }
    
    .main-header {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        margin-bottom: 0.5rem !important;
    }
    
    .sub-header {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        margin-bottom: 1rem !important;
        text-align: center !important;
    }
    
    /* Card styling */
    .feature-card {
        border-radius: 12px !important;
        padding: 1.5rem !important;
        background-color: var(--card-bg) !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2) !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    .feature-card:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.3) !important;
        border: 1px solid var(--accent-light) !important;
    }
    
    .feature-title {
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        margin-top: 1rem !important;
        font-size: 1.3rem !important;
        text-align: center !important;
    }
    
    .feature-description {
        color: var(--text-secondary) !important;
        font-size: 1rem !important;
        line-height: 1.5 !important;
        text-align: center !important;
    }
    
    .cta-button {
        background-color: var(--accent-color) !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        transition: background-color 0.3s ease !important;
    }
    
    .cta-button:hover {
        background-color: var(--accent-light) !important;
    }
    
    .form-container {
        background-color: var(--card-bg) !important;
        border-radius: 12px !important;
        padding: 2rem !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2) !important;
        color: var(--text-primary) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    .footer {
        padding: 2rem 0 !important;
        border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
        margin-top: 3rem !important;
        background-color: var(--card-bg) !important;
    }
    
    .footer-link {
        color: var(--text-secondary) !important;
        text-decoration: none !important;
        transition: color 0.2s ease !important;
        font-weight: 500 !important;
        padding: 0.5rem 1rem !important;
    }
    
    .footer-link:hover {
        color: var(--text-primary) !important;
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
        text-align: center !important;
        max-width: 800px !important;
        margin: 0 auto !important;
    }
    
    .hero-section {
        background-color: var(--background-darker) !important;
        color: var(--text-primary) !important;
        padding: 2rem !important;
        text-align: center !important;
        border-radius: 12px !important;
        margin-top: 2rem !important;
    }
    
    .hero-title {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        margin-bottom: 1rem !important;
    }
    
    .hero-subtitle {
        font-size: 1.2rem !important;
        color: var(--text-secondary) !important;
        max-width: 700px !important;
        margin: 0 auto !important;
        line-height: 1.6 !important;
        margin-bottom: 1.5rem !important;
    }
    
    /* Stat cards */
    .stat-card {
        background-color: var(--card-bg) !important;
        border-radius: 10px !important;
        padding: 1.5rem !important;
        text-align: center !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    .stat-section {
        background-color: var(--background-dark) !important;
        padding: 3rem 0 !important;
    }
    
    .stat-number {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        margin-bottom: 0.5rem !important;
    }
    
    .stat-label {
        color: var(--text-secondary) !important;
        font-size: 1rem !important;
    }
    
    .subscribe-section {
        background-color: var(--background-darker) !important;
        padding: 2rem !important;
        text-align: center !important;
        color: white !important;
        border-radius: 12px !important;
        margin: 2rem 0 !important;
    }
    
    .subscribe-title {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        color: white !important;
        margin-bottom: 1rem !important;
    }
    
    .subscribe-subtitle {
        font-size: 1rem !important;
        color: var(--text-secondary) !important;
        margin-bottom: 1.5rem !important;
    }
    
    .subscribe-form {
        display: flex !important;
        justify-content: center !important;
        margin: 0 auto !important;
        max-width: 500px !important;
    }
    
    .subscribe-input {
        padding: 0.5rem 1rem !important;
        border: none !important;
        border-radius: 4px 0 0 4px !important;
        width: 100% !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: var(--text-primary) !important;
    }
    
    .subscribe-button {
        background-color: var(--accent-color) !important;
        color: white !important;
        border: none !important;
        border-radius: 0 4px 4px 0 !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        cursor: pointer !important;
    }
    
    /* Footer styling */
    .footer-dark {
        background-color: var(--background-darker) !important;
        color: var(--text-primary) !important;
        padding: 2rem 0 !important;
        text-align: center !important;
        border-radius: 12px 12px 0 0 !important;
        margin-top: 2rem !important;
    }
</style>
""", unsafe_allow_html=True)

logo_image = "researchgenielogo.jpg"
# Display it here but hide it later
logo_placeholder = st.empty()
logo_placeholder.image(logo_image, width=1)
# Now hide it since we'll show it in our custom header
logo_placeholder.empty()

# Function to convert image to base64
def get_image_as_base64(file_path):
    try:
        img = Image.open(file_path)
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()
    except Exception:
        # If the file doesn't exist, create a placeholder
        return get_placeholder_logo_base64()

# Function to create a placeholder logo as base64
def get_placeholder_logo_base64():
    try:
        from PIL import ImageDraw, ImageFont
        # Create a placeholder dark square with "RG" text
        img = Image.new('RGB', (100, 100), color="#282833")
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("Arial", 40)
        except IOError:
            font = ImageFont.load_default()
        
        draw.text((30, 30), "RG", fill="white", font=font)
        
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()
    except Exception:
        # Fallback if there are issues with PIL
        return ""

# Store the base64 image in session state so it's accessible in the markdown
if 'logo_base64' not in st.session_state:
    st.session_state.logo_base64 = get_image_as_base64("researchgenielogo.jpg")

# New centered header without navigation buttons
st.markdown(f"""
<style>
    .full-width-header {{
        background-color: var(--background-darker);
        padding: 20px 0;
        width: 100%;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        margin-top: -75px;
        margin-bottom: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    
    .logo-container {{
        display: flex;
        align-items: center;
        justify-content: center;
    }}
</style>

<div class="full-width-header">
    <div class="logo-container">
        <img src="data:image/jpg;base64,{st.session_state.get('logo_base64', '')}" width="50" style="margin-right: 15px;">
        <span style="font-size: 1.8rem; font-weight: 700; color: white;">ResearchGenie</span>
    </div>
</div>

<!-- Add some space after the header -->
<div style="margin-top: 20px;"></div>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Your Personal Research Assistant</h1>
    <p class="hero-subtitle">
        Discover, analyze, and organize scholarly research with the power of AI. ResearchGenie helps you find relevant papers and insights with unprecedented precision.
    </p>
    <button class="cta-button">Research Now</button>
</div>
""", unsafe_allow_html=True)

# Mission section
st.markdown("<br>", unsafe_allow_html=True)
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

# What We Do section
st.markdown('<br><br>', unsafe_allow_html=True)

# Feature cards with improved layout
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
            <div style="font-size: 2rem; color: var(--text-primary); text-align: center;">{features[i]['icon']}</div>
            <h3 class="feature-title">{features[i]['title']}</h3>
            <p class="feature-description">{features[i]['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Sign-Up Form Section
st.markdown("""
<div class="subscribe-section">
    <h2 class="subscribe-title">Join Our Research Community</h2>
    <p class="subscribe-subtitle">
        Stay informed about the latest updates, research trends, and news from ResearchGenie!
    </p>
    <div class="subscribe-form">
        <input type="email" placeholder="Your email address" class="subscribe-input">
        <button class="subscribe-button">Subscribe</button>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="stat-section">
    <h2 class="sub-header">ResearchGenie in Numbers</h2>
    <div style="display: flex; justify-content: center; gap: 20px; margin-top: 2rem; max-width: 900px; margin-left: auto; margin-right: auto;">
        <div class="stat-card" style="flex: 1; min-width: 0;">
            <h3 class="stat-number">1 Million +</h3>
            <p class="stat-label">Research Papers</p>
        </div>
        <div class="stat-card" style="flex: 1; min-width: 0;">
            <h3 class="stat-number">50 Thousand +</h3>
            <p class="stat-label">Researchers</p>
        </div>
        <div class="stat-card" style="flex: 1; min-width: 0;">
            <h3 class="stat-number">100 +</h3>
            <p class="stat-label">Universities</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer (simplified without navigation links)
st.markdown("""
<div class="footer-dark">
    <div style="text-align: center;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 0.5rem;">ResearchGenie</div>
        <p class="copyright">© 2025 ResearchGenie. All rights reserved.</p>
    </div>
</div>
""", unsafe_allow_html=True)







