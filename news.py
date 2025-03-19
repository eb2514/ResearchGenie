import streamlit as st
from PIL import Image
import base64
import io

st.session_state.show_sidebar = False
# Custom CSS for modern styling with dark theme based on the provided image
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Define our color palette - dark theme from image */
    :root {
        --background-dark: #1a1b24; /* Dark blue-black background */
        --background-darker: #0f1017; /* Even darker shade for contrast */
        --accent-color: #32333e; /* Slightly lighter dark blue */
        --text-primary: #ffffff; /* White text */
        --text-secondary: #b0b0b6; /* Light gray text */
        --card-bg: #252632; /* Dark card background */
        --border-color: #3a3b46; /* Subtle border color */
    }
    
    /* Overall background and text color */
    .stApp {
        background-color: var(--background-dark);
        color: var(--text-primary);
    }
    
    /* Title styling */
    h1 {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }
    
    h2, h3, .subheader {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        margin-top: 1.5rem !important;
    }
    
    /* Bold text styling */
    strong {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }
    
    /* Card styling for news and update items */
    .news-item {
        background-color: var(--card-bg) !important;
        border-radius: 10px !important;
        padding: 1.5rem !important;
        margin-bottom: 1rem !important;
        border: 1px solid var(--border-color) !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }
    
    .news-item:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3) !important;
        border: 1px solid var(--accent-color) !important;
    }
    
    /* Footer styling */
    .footer-dark {
        background-color: var(--background-darker) !important;
        color: var(--text-primary) !important;
        padding: 2rem 0 !important;
        text-align: center !important;
        margin-top: 2rem !important;
        border-top: 1px solid var(--border-color) !important;
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
</style>
""", unsafe_allow_html=True)

# For the logo to work in custom HTML, we need to convert it to base64
def get_image_as_base64(file_path):
    try:
        img = Image.open(file_path)
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()
    except Exception:
        # If the file doesn't exist, create a placeholder
        return get_placeholder_logo_base64()

def get_placeholder_logo_base64():
    # Create a placeholder dark square with "RG" text
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new('RGB', (100, 100), color="#32333e")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("Arial", 40)
    except IOError:
        font = ImageFont.load_default()
    
    draw.text((30, 30), "RG", fill="white", font=font)
    
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Store the base64 image in session state so it's accessible in the markdown
if 'logo_base64' not in st.session_state:
    st.session_state.logo_base64 = get_image_as_base64("researchgenielogo.jpg")

# Full-width header with centered logo and name, no navigation buttons
st.markdown(f"""
<style>
    /* Full-width container that breaks out of Streamlit's default layout */
    .full-width-header {{
        background-color: var(--background-darker);
        padding: 15px 0;
        width: 101vw;
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
    
    /* Container for logo and site name */
    .logo-container {{
        display: flex;
        align-items: center;
        justify-content: center;
    }}
</style>

<div class="full-width-header">
    <div class="logo-container">
        <img src="data:image/jpg;base64,{st.session_state.get('logo_base64', '')}" width="50" style="margin-right: 15px;">
        <span style="font-size: 1.8rem; font-weight: 700; color: white;">ResearchGenie Beta</span>
    </div>
</div>

<!-- Add some space after the header -->
<div style="margin-top: 20px;"></div>
""", unsafe_allow_html=True)

# Title and brief description
st.markdown('<h1 style="text-align: center; font-size: 2.2rem; margin-bottom: 0.5rem;">What\'s New?</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: var(--text-secondary); max-width: 700px; margin: 0 auto; margin-bottom: 2rem;">Stay up to date with the latest developments, projects, and news surrounding our website and company.</p>', unsafe_allow_html=True)

# News Section
st.markdown('<h2 style="text-align: center; font-size: 1.8rem; margin-bottom: 1.5rem;">Exciting News!</h2>', unsafe_allow_html=True)

# News Container
with st.container():
    # News Item 1
    with st.container():
        st.markdown('<div class="news-item">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("UnderCon.png", width=150)
        with col2:
            st.markdown("""
            <h3 style="color: var(--text-primary); margin-bottom: 0.5rem; font-size: 1.4rem;">Educational Partnerships</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">
                We are very excited to be working with several educational institutions to make ResearchGenie a vital component in creating graduate and undergraduate papers. These partnerships will help shape the future of academic research.
            </p>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # News Item 2
    with st.container():
        st.markdown('<div class="news-item">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("UnderCon.png", width=150)
        with col2:
            st.markdown("""
            <h3 style="color: var(--text-primary); margin-bottom: 0.5rem; font-size: 1.4rem;">Growing Research Community</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">
                We are very excited to be working with several educational institutions to make ResearchGenie a vital component to creating graduate and undergraduate papers. Our platform continues to gain recognition in academic circles.
            </p>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Updates Container
st.markdown('<h2 style="text-align: center; font-size: 1.8rem; margin-bottom: 1.5rem;">Upcoming Updates... In Probable Order :/ </h2>', unsafe_allow_html=True)

with st.container():
    # Update Item 1
    with st.container():
        st.markdown('<div class="news-item">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("UnderCon.png", width=150)
        with col2:
            st.markdown("""
            <h3 style="color: var(--text-primary); margin-bottom: 0.5rem; font-size: 1.4rem;">Taking Accountability</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">
                Yes we heard. We are working on adding accounts to save conversation history 
                and plenty of other personal preferences. This feature will enhance your research experience by allowing you to pick up right where you left off.
            </p>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Update Item 2
    with st.container():
        st.markdown('<div class="news-item">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("UnderCon.png", width=150)
        with col2:
            st.markdown("""
            <h3 style="color: var(--text-primary); margin-bottom: 0.5rem; font-size: 1.4rem;">Behind the Scenes</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">
                Speeding up search engine to handle the growing userbase. Our development team is optimizing every aspect of our platform to ensure lightning-fast results even as our user community expands.
            </p>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Update Item 3
    with st.container():
        st.markdown('<div class="news-item">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("UnderCon.png", width=150)
        with col2:
            st.markdown("""
            <h3 style="color: var(--text-primary); margin-bottom: 0.5rem; font-size: 1.4rem;">Linked-Search? Searched-in?</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">
                We are developing a way to foster a research-based community, 
                allowing people around the world to read and collaborate on research
                using this platform. This feature will revolutionize how researchers connect and work together.
            </p>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer - simplified with no navigation links
st.markdown("""
<div class="footer-dark">
    <div style="text-align: center;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 0.5rem;">ResearchGenie</div>
        <p class="copyright">© 2025 ResearchGenie. All rights reserved.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# import streamlit as st
# from PIL import Image
# import base64
# import io

# st.session_state.show_sidebar = False
# # Custom CSS for modern styling to match home page with cream/light-brown background and brown accents
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
#     html, body, [class*="css"] {
#         font-family: 'Inter', sans-serif;
#     }
    
#     /* Define our color palette - same as home page */
#     :root {
#         --background-light: #FAEBD7; /* AntiqueWhite cream background */
#         --accent-color: #8B4513; /* SaddleBrown for accents */
#         --accent-dark: #5C3317; /* Darker brown variant for hover states */
#         --accent-light: #D2B48C; /* Tan, a lighter brown shade */
#         --text-on-light: #4B3621; /* Dark brown text */
#         --text-primary: #4B3621;
#         --text-secondary: #6C584C;
#         --card-bg: #FFF8F0; /* Off-white cream for cards */
#     }
    
#     /* Overall background and text color */
#     .stApp {
#         background-color: var(--background-light);
#         color: var(--text-primary);
#     }
    
#     /* Title styling */
#     h1 {
#         color: var(--text-primary) !important;
#         font-weight: 700 !important;
#         margin-bottom: 0.5rem !important;
#     }
    
#     h2, h3, .subheader {
#         color: var(--text-primary) !important;
#         font-weight: 600 !important;
#         margin-top: 1.5rem !important;
#     }
    
#     # /* News container styling */
#     # .news-container {
#     #     background-color: var(--card-bg) !important;
#     #     border-radius: 12px !important;
#     #     padding: 1.5rem !important;
#     #     margin-bottom: 1.5rem !important;
#     #     box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
#     #     border: 1px solid rgba(139, 69, 19, 0.2) !important;
#     # }
    
#     # /* News item styling */
#     # .news-item {
#     #     background-color: var(--card-bg) !important;
#     #     border-radius: 10px !important;
#     #     padding: 1.5rem !important;
#     #     margin-bottom: 1rem !important;
#     #     border: 1px solid rgba(139, 69, 19, 0.15) !important;
#     #     transition: transform 0.3s ease, box-shadow 0.3s ease !important;
#     # }
    
#     # .news-item:hover {
#     #     transform: translateY(-3px) !important;
#     #     box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1) !important;
#     #     border: 1px solid var(--accent-color) !important;
#     # }
    
#     /* Bold text styling */
#     strong {
#         color: var(--accent-color) !important;
#         font-weight: 600 !important;
#     }
    
#     /* Footer styling */
#     .footer-dark {
#         background-color: var(--card-bg) !important;
#         color: var(--text-primary) !important;
#         padding: 2rem 0 !important;
#         text-align: center !important;
#         margin-top: 2rem !important;
#         border-top: 1px solid rgba(139, 69, 19, 0.2) !important;
#     }
    
#     .footer-link {
#         color: var(--text-secondary) !important;
#         text-decoration: none !important;
#         transition: color 0.2s ease !important;
#         font-weight: 500 !important;
#         padding: 0.5rem 1rem !important;
#     }
    
#     .footer-link:hover {
#         color: var(--accent-color) !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# # For the logo to work in custom HTML, we need to convert it to base64
# def get_image_as_base64(file_path):
#     try:
#         img = Image.open(file_path)
#         buffered = io.BytesIO()
#         img.save(buffered, format="JPEG")
#         return base64.b64encode(buffered.getvalue()).decode()
#     except Exception:
#         # If the file doesn't exist, create a placeholder
#         return get_placeholder_logo_base64()

# def get_placeholder_logo_base64():
#     # Create a placeholder brown square with "RG" text
#     from PIL import Image, ImageDraw, ImageFont
#     img = Image.new('RGB', (100, 100), color="#8B4513")
#     draw = ImageDraw.Draw(img)
#     try:
#         font = ImageFont.truetype("Arial", 40)
#     except IOError:
#         font = ImageFont.load_default()
    
#     draw.text((30, 30), "RG", fill="white", font=font)
    
#     buffered = io.BytesIO()
#     img.save(buffered, format="JPEG")
#     return base64.b64encode(buffered.getvalue()).decode()

# # Store the base64 image in session state so it's accessible in the markdown
# if 'logo_base64' not in st.session_state:
#     st.session_state.logo_base64 = get_image_as_base64("researchgenielogo.jpg")

# # Full-width header with the same style as home page
# st.markdown(f"""
# <style>
#     /* Override any conflicting styles for navigation links */
#     .nav-link {{
#         color: white !important;
#         font-weight: 500 !important;
#         margin-left: 20px !important;
#         text-decoration: none !important;
#     }}
    
#     /* Full-width container that breaks out of Streamlit's default layout */
#     .full-width-header {{
#         background-color: #8B4513;
#         padding: 15px 0;
#         width: 101vw;
#         position: relative;
#         left: 50%;
#         right: 50%;
#         margin-left: -50vw;
#         margin-right: -50vw;
#         margin-top: -75px;
#         margin-bottom: 30px;
#         display: flex;
#         align-items: center;
#     }}
    
#     /* Container for logo and site name */
#     .logo-container {{
#         display: flex;
#         align-items: center;
#         margin-left: 40px;
#     }}
    
#     /* Navigation container */
#     .nav-container {{
#         margin-left: auto;
#         margin-right: 40px;
#     }}
# </style>

# <div class="full-width-header">
#     <div class="logo-container">
#         <img src="data:image/jpg;base64,{st.session_state.get('logo_base64', '')}" width="50" style="margin-right: 15px;">
#         <span style="font-size: 1.8rem; font-weight: 700; color: white;">ResearchGenie</span>
#     </div>
#     <div class="nav-container">
#         <a href="/home" class="nav-link">Home</a>
#         <a href="/search" class="nav-link">Search</a>
#         <a href="/news" class="nav-link">News</a>
#         <a href="/more" class="nav-link">More</a>
#     </div>
# </div>

# <!-- Add some space after the header -->
# <div style="margin-top: 20px;"></div>
# """, unsafe_allow_html=True)

# # Title and brief description
# st.markdown('<h1 style="text-align: center; font-size: 2.2rem; margin-bottom: 0.5rem;">What\'s New?</h1>', unsafe_allow_html=True)
# st.markdown('<p style="text-align: center; font-size: 1.2rem; color: var(--text-secondary); max-width: 700px; margin: 0 auto; margin-bottom: 2rem;">Stay up to date with the latest developments, projects, and news surrounding our website and company.</p>', unsafe_allow_html=True)

# # News Section
# st.markdown('<h2 style="text-align: center; font-size: 1.8rem; margin-bottom: 1.5rem;">Exciting News!</h2>', unsafe_allow_html=True)

# # News Container - directly use st.container with custom CSS
# with st.container():
#     st.markdown('<div class="news-container">', unsafe_allow_html=True)
    
#     # News Item 1
#     with st.container():
#         st.markdown('<div class="news-item">', unsafe_allow_html=True)
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             st.image("UnderCon.png", width=150)
#         with col2:
#             st.markdown("""
#             <h3 style="color: var(--accent-color); margin-bottom: 0.5rem; font-size: 1.4rem;">Educational Partnerships</h3>
#             <p style="color: var(--text-secondary); line-height: 1.6;">
#                 We are very excited to be working with several educational institutions to make ResearchGenie a vital component in creating graduate and undergraduate papers. These partnerships will help shape the future of academic research.
#             </p>
#             """, unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     # News Item 2
#     with st.container():
#         st.markdown('<div class="news-item">', unsafe_allow_html=True)
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             st.image("UnderCon.png", width=150)
#         with col2:
#             st.markdown("""
#             <h3 style="color: var(--accent-color); margin-bottom: 0.5rem; font-size: 1.4rem;">Growing Research Community</h3>
#             <p style="color: var(--text-secondary); line-height: 1.6;">
#                 We are very excited to be working with several educational institutions to make ResearchGenie a vital component to creating graduate and undergraduate papers. Our platform continues to gain recognition in academic circles.
#             </p>
#             """, unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown('</div>', unsafe_allow_html=True) # Close the news container

# # Updates Container
# st.markdown('<h2 style="text-align: center; font-size: 1.8rem; margin-bottom: 1.5rem;">Upcoming Updates... In Probable Order :/ </h2>', unsafe_allow_html=True)

# with st.container():
#     st.markdown('<div class="news-container">', unsafe_allow_html=True)
    
#     # Update Item 1
#     with st.container():
#         st.markdown('<div class="news-item">', unsafe_allow_html=True)
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             st.image("UnderCon.png", width=150)
#         with col2:
#             st.markdown("""
#             <h3 style="color: var(--accent-color); margin-bottom: 0.5rem; font-size: 1.4rem;">Taking Accountability</h3>
#             <p style="color: var(--text-secondary); line-height: 1.6;">
#                 Yes we heard. We are working on adding accounts to save conversation history 
#                 and plenty of other personal preferences. This feature will enhance your research experience by allowing you to pick up right where you left off.
#             </p>
#             """, unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     # Update Item 2
#     with st.container():
#         st.markdown('<div class="news-item">', unsafe_allow_html=True)
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             st.image("UnderCon.png", width=150)
#         with col2:
#             st.markdown("""
#             <h3 style="color: var(--accent-color); margin-bottom: 0.5rem; font-size: 1.4rem;">Behind the Scenes</h3>
#             <p style="color: var(--text-secondary); line-height: 1.6;">
#                 Speeding up search engine to handle the growing userbase. Our development team is optimizing every aspect of our platform to ensure lightning-fast results even as our user community expands.
#             </p>
#             """, unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     # Update Item 3
#     with st.container():
#         st.markdown('<div class="news-item">', unsafe_allow_html=True)
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             st.image("UnderCon.png", width=150)
#         with col2:
#             st.markdown("""
#             <h3 style="color: var(--accent-color); margin-bottom: 0.5rem; font-size: 1.4rem;">Linked-Search? Searched-in?</h3>
#             <p style="color: var(--text-secondary); line-height: 1.6;">
#                 We are developing a way to foster a research-based community, 
#                 allowing people around the world to read and collaborate on research
#                 using this platform. This feature will revolutionize how researchers connect and work together.
#             </p>
#             """, unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown('</div>', unsafe_allow_html=True) # Close the updates container

# # Footer
# st.markdown("""
# <div class="footer-dark">
#     <div style="display: flex; justify-content: center; margin-bottom: 1rem;">
#         <a href="/home" class="footer-link">Home</a>
#         <a href="/search" class="footer-link">Search</a>
#         <a href="/news" class="footer-link">News</a>
#         <a href="/more" class="footer-link">More</a>
#     </div>
#     <div style="text-align: center;">
#         <div style="font-weight: 600; color: var(--accent-color); margin-bottom: 0.5rem;">ResearchGenie</div>
#         <p class="copyright">© 2025 ResearchGenie. All rights reserved.</p>
#     </div>
# </div>
# """, unsafe_allow_html=True)


# # import streamlit as st
# # from PIL import Image
# # import base64
# # import io

# # # Custom CSS for modern styling to match home page with cream/light-brown background and brown accents
# # st.markdown("""
# # <style>
# #     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
# #     html, body, [class*="css"] {
# #         font-family: 'Inter', sans-serif;
# #     }
    
# #     /* Define our color palette - same as home page */
# #     :root {
# #         --background-light: #FAEBD7; /* AntiqueWhite cream background */
# #         --accent-color: #8B4513; /* SaddleBrown for accents */
# #         --accent-dark: #5C3317; /* Darker brown variant for hover states */
# #         --accent-light: #D2B48C; /* Tan, a lighter brown shade */
# #         --text-on-light: #4B3621; /* Dark brown text */
# #         --text-primary: #4B3621;
# #         --text-secondary: #6C584C;
# #         --card-bg: #FFF8F0; /* Off-white cream for cards */
# #     }
    
# #     /* Overall background and text color */
# #     .stApp {
# #         background-color: var(--background-light);
# #         color: var(--text-primary);
# #     }
    
# #     /* Title styling */
# #     h1 {
# #         color: var(--text-primary) !important;
# #         font-weight: 700 !important;
# #         margin-bottom: 0.5rem !important;
# #     }
    
# #     h2, h3, .subheader {
# #         color: var(--text-primary) !important;
# #         font-weight: 600 !important;
# #         margin-top: 1.5rem !important;
# #     }
    
# #     /* News container styling */
# #     .news-container {
# #         background-color: var(--card-bg) !important;
# #         border-radius: 12px !important;
# #         padding: 1.5rem !important;
# #         margin-bottom: 1.5rem !important;
# #         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
# #         border: 1px solid rgba(139, 69, 19, 0.2) !important;
# #     }
    
# #     /* News item styling */
# #     .news-item {
# #         background-color: var(--card-bg) !important;
# #         border-radius: 10px !important;
# #         padding: 1.5rem !important;
# #         margin-bottom: 1rem !important;
# #         border: 1px solid rgba(139, 69, 19, 0.15) !important;
# #         transition: transform 0.3s ease, box-shadow 0.3s ease !important;
# #     }
    
# #     .news-item:hover {
# #         transform: translateY(-3px) !important;
# #         box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1) !important;
# #         border: 1px solid var(--accent-color) !important;
# #     }
    
# #     /* Bold text styling */
# #     strong {
# #         color: var(--accent-color) !important;
# #         font-weight: 600 !important;
# #     }
    
# #     /* Footer styling */
# #     .footer-dark {
# #         background-color: var(--card-bg) !important;
# #         color: var(--text-primary) !important;
# #         padding: 2rem 0 !important;
# #         text-align: center !important;
# #         margin-top: 2rem !important;
# #         border-top: 1px solid rgba(139, 69, 19, 0.2) !important;
# #     }
    
# #     .footer-link {
# #         color: var(--text-secondary) !important;
# #         text-decoration: none !important;
# #         transition: color 0.2s ease !important;
# #         font-weight: 500 !important;
# #         padding: 0.5rem 1rem !important;
# #     }
    
# #     .footer-link:hover {
# #         color: var(--accent-color) !important;
# #     }
    
# #     /* Override Streamlit's default container borders */
# #     [data-testid="stVerticalBlock"] > [style*="flex"] {
# #         gap: 0.75rem !important;
# #     }
# # </style>
# # """, unsafe_allow_html=True)

# # # For the logo to work in custom HTML, we need to convert it to base64
# # def get_image_as_base64(file_path):
# #     try:
# #         img = Image.open(file_path)
# #         buffered = io.BytesIO()
# #         img.save(buffered, format="JPEG")
# #         return base64.b64encode(buffered.getvalue()).decode()
# #     except Exception:
# #         # If the file doesn't exist, create a placeholder
# #         return get_placeholder_logo_base64()

# # def get_placeholder_logo_base64():
# #     # Create a placeholder brown square with "RG" text
# #     from PIL import Image, ImageDraw, ImageFont
# #     img = Image.new('RGB', (100, 100), color="#8B4513")
# #     draw = ImageDraw.Draw(img)
# #     try:
# #         font = ImageFont.truetype("Arial", 40)
# #     except IOError:
# #         font = ImageFont.load_default()
    
# #     draw.text((30, 30), "RG", fill="white", font=font)
    
# #     buffered = io.BytesIO()
# #     img.save(buffered, format="JPEG")
# #     return base64.b64encode(buffered.getvalue()).decode()

# # # Store the base64 image in session state so it's accessible in the markdown
# # if 'logo_base64' not in st.session_state:
# #     st.session_state.logo_base64 = get_image_as_base64("researchgenielogo.jpg")

# # logo_image = "researchgenielogo.jpg"
# # # Display it here but hide it later
# # logo_placeholder = st.empty()
# # logo_placeholder.image(logo_image, width=1)
# # # Now hide it since we'll show it in our custom header
# # logo_placeholder.empty()

# # # Full-width header with the same style as home page
# # st.markdown(f"""
# # <style>
# #     /* Override any conflicting styles for navigation links */
# #     .nav-link {{
# #         color: white !important;
# #         font-weight: 500 !important;
# #         margin-left: 20px !important;
# #         text-decoration: none !important;
# #     }}
    
# #     /* Full-width container that breaks out of Streamlit's default layout */
# #     .full-width-header {{
# #         background-color: #8B4513;
# #         padding: 15px 0;
# #         width: 101vw;
# #         position: relative;
# #         left: 50%;
# #         right: 50%;
# #         margin-left: -50vw;
# #         margin-right: -50vw;
# #         margin-top: -75px;
# #         margin-bottom: 30px;
# #         display: flex;
# #         align-items: center;
# #     }}
    
# #     /* Container for logo and site name */
# #     .logo-container {{
# #         display: flex;
# #         align-items: center;
# #         margin-left: 40px;
# #     }}
    
# #     /* Navigation container */
# #     .nav-container {{
# #         margin-left: auto;
# #         margin-right: 40px;
# #     }}
# # </style>

# # <div class="full-width-header">
# #     <div class="logo-container">
# #         <img src="data:image/jpg;base64,{st.session_state.get('logo_base64', '')}" width="50" style="margin-right: 15px;">
# #         <span style="font-size: 1.8rem; font-weight: 700; color: white;">ResearchGenie</span>
# #     </div>
# #     <div class="nav-container">
# #         <a href="/home" onclick="return false;" class="nav-link">Home</a>
# #         <a href="/search" onclick="return false;" class="nav-link">Search</a>
# #         <a href="/news" onclick="return false;" class="nav-link">News</a>
# #         <a href="/more" onclick="return false;" class="nav-link">More</a>
# #     </div>
# # </div>

# # <!-- Add some space after the header -->
# # <div style="margin-top: 20px;"></div>
# # """, unsafe_allow_html=True)

# # # Title and brief description
# # st.markdown('<h1 style="text-align: center; font-size: 2.2rem; margin-bottom: 0.5rem;">What\'s New?</h1>', unsafe_allow_html=True)
# # st.markdown('<p style="text-align: center; font-size: 1.2rem; color: var(--text-secondary); max-width: 700px; margin: 0 auto; margin-bottom: 2rem;">Stay up to date with the latest developments, projects, and news surrounding our website and company.</p>', unsafe_allow_html=True)

# # # News Section
# # st.markdown('<h2 style="text-align: center; font-size: 1.8rem; margin-bottom: 1.5rem;">Exciting News!</h2>', unsafe_allow_html=True)

# # # News Container
# # st.markdown("""
# # <div style="background-color: var(--card-bg); border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); border: 1px solid rgba(139, 69, 19, 0.2); margin-bottom: 2rem;">
# # """, unsafe_allow_html=True)

# # # News Item 1
# # with st.container():
# #     st.markdown('<div class="news-item">', unsafe_allow_html=True)
# #     col1, col2 = st.columns([1, 3])
# #     with col1:
# #         st.image("UnderCon.png", width=250, use_container_width=True)
# #     with col2:
# #         st.markdown("""
# #         <h3 style="color: var(--accent-color); margin-bottom: 0.5rem; font-size: 1.4rem;">Educational Partnerships</h3>
# #         <p style="color: var(--text-secondary); line-height: 1.6;">
# #             We are very excited to be working with several educational institutions to make ResearchGenie a vital component in creating graduate and undergraduate papers. These partnerships will help shape the future of academic research.
# #         </p>
# #         """, unsafe_allow_html=True)
# #     st.markdown('</div>', unsafe_allow_html=True)

# # # News Item 2
# # with st.container():
# #     st.markdown('<div class="news-item">', unsafe_allow_html=True)
# #     col1, col2 = st.columns([1, 3])
# #     with col1:
# #         st.image("UnderCon.png", width=250, use_container_width=True)
# #     with col2:
# #         st.markdown("""
# #         <h3 style="color: var(--accent-color); margin-bottom: 0.5rem; font-size: 1.4rem;">Growing Research Community</h3>
# #         <p style="color: var(--text-secondary); line-height: 1.6;">
# #             We are very excited to be working with several educational institutions to make ResearchGenie a vital component to creating graduate and undergraduate papers. Our platform continues to gain recognition in academic circles.
# #         </p>
# #         """, unsafe_allow_html=True)
# #     st.markdown('</div>', unsafe_allow_html=True)

# # st.markdown('</div>', unsafe_allow_html=True) # Close the news container

# # # Updates Container
# # st.markdown('<h2 style="text-align: center; font-size: 1.8rem; margin-bottom: 1.5rem;">Upcoming Updates... In Probable Order :/ </h2>', unsafe_allow_html=True)

# # st.markdown("""
# # <div style="background-color: var(--card-bg); border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); border: 1px solid rgba(139, 69, 19, 0.2);">
# # """, unsafe_allow_html=True)

# # # Update Item 1
# # with st.container():
# #     st.markdown('<div class="news-item">', unsafe_allow_html=True)
# #     col1, col2 = st.columns([1, 3])
# #     with col1:
# #         st.image("UnderCon.png", width=250, use_container_width=True)
# #     with col2:
# #         st.markdown("""
# #         <h3 style="color: var(--accent-color); margin-bottom: 0.5rem; font-size: 1.4rem;">Taking Accountability</h3>
# #         <p style="color: var(--text-secondary); line-height: 1.6;">
# #             Yes we heard. We are working on adding accounts to save conversation history 
# #             and plenty of other personal preferences. This feature will enhance your research experience by allowing you to pick up right where you left off.
# #         </p>
# #         """, unsafe_allow_html=True)
# #     st.markdown('</div>', unsafe_allow_html=True)

# # # Update Item 2
# # with st.container():
# #     st.markdown('<div class="news-item">', unsafe_allow_html=True)
# #     col1, col2 = st.columns([1, 3])
# #     with col1:
# #         st.image("UnderCon.png", width=250, use_container_width=True)
# #     with col2:
# #         st.markdown("""
# #         <h3 style="color: var(--accent-color); margin-bottom: 0.5rem; font-size: 1.4rem;">Behind the Scenes</h3>
# #         <p style="color: var(--text-secondary); line-height: 1.6;">
# #             Speeding up search engine to handle the growing userbase. Our development team is optimizing every aspect of our platform to ensure lightning-fast results even as our user community expands.
# #         </p>
# #         """, unsafe_allow_html=True)
# #     st.markdown('</div>', unsafe_allow_html=True)

# # # Update Item 3
# # with st.container():
# #     st.markdown('<div class="news-item">', unsafe_allow_html=True)
# #     col1, col2 = st.columns([1, 3])
# #     with col1:
# #         st.image("UnderCon.png", width=250, use_container_width=True)
# #     with col2:
# #         st.markdown("""
# #         <h3 style="color: var(--accent-color); margin-bottom: 0.5rem; font-size: 1.4rem;">Linked-Search? Searched-in?</h3>
# #         <p style="color: var(--text-secondary); line-height: 1.6;">
# #             We are developing a way to foster a research-based community, 
# #             allowing people around the world to read and collaborate on research
# #             using this platform. This feature will revolutionize how researchers connect and work together.
# #         </p>
# #         """, unsafe_allow_html=True)
# #     st.markdown('</div>', unsafe_allow_html=True)

# # st.markdown("""
# # <div class="footer-dark">
# #     <div style="display: flex; justify-content: center; margin-bottom: 1rem;">
# #         <a href="/home" class="footer-link">Home</a>
# #         <a href="/search" class="footer-link">Search</a>
# #         <a href="/news" class="footer-link">News</a>
# #         <a href="/more" class="footer-link">More</a>
# #     </div>
# #     <div style="text-align: center;">
# #         <div style="font-weight: 600; color: var(--accent-color); margin-bottom: 0.5rem;">ResearchGenie</div>
# #         <p class="copyright">© 2025 ResearchGenie. All rights reserved.</p>
# #     </div>
# # </div>
# # """, unsafe_allow_html=True)
