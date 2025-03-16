import streamlit as st

st.set_page_config(page_title="My App",page_icon="🧞‍♂️", layout="wide", initial_sidebar_state="expanded")
st.markdown(""" 
            <style>
            /* Set a fixed width for the sidebar */
            .stSidebar {
        width: 400px !important;  /* Set the desired width */
                        }   
            <style>    
            """, unsafe_allow_html=True)

pg = st.navigation([
    st.Page("home.py", title="Home",  icon="🧞‍♂️"),
    st.Page("search.py", title="Search", icon="🧞‍♂️"),
    st.Page("news.py", title="News",  icon="🧞‍♂️"),
    ])

pg.run()
