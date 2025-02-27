import streamlit as st

# Title and brief description
st.title("What's New?")
st.write("Stay up to date with the latest developments, projects, and news surrounding our website and company.")

# Spacer to give some breathing room
st.write("\n" * 2)


#News Container
st.subheader("Exciting News!")
with st.container(border=True):
    #News Item 1
    n1 = st.container(border=True)
    with n1:
        st.image("UnderCon.png", width=300, use_container_width=False)
        st.write("We are very exciting to be working with several educational institutions \
                 to make ResearchGenie a vital component to creating graduate and undergraduate papers.")
    n2 = st.container(border=True)
    with n2:
        st.image("UnderCon.png", width=300, use_container_width=False)
        st.write("We are very exciting to be working with several educational institutions \
                 to make ResearchGenie vital component to creating graduate and undergraduate papers.")





# Updates Container
st.subheader("Upcoming Updates... In Probable Order :/ ")
with st.container(border=True):
    # Update Item 1
    u1 = st.container(border=True)
    with u1:
        col1, col2 = st.columns([1, 3])  # Set column width ratio for image and text
        with col1:
            st.image("UnderCon.png", width=300, use_container_width=False)  # Display image
        with col2:
            st.markdown(
                """
                **Taking Accountability**
                Yes we heard. We are working on adding accounts to save conversation history 
                and plenty of other personal preferences.
                """
            )
    # Update Item 2
    u2 = st.container(border=True)
    with u2:
   
        col1, col2 = st.columns([1, 3])  # Reuse column layout
        with col1:
            st.image("UnderCon.png", width=300, use_container_width=False)  # Display image
        with col2:
            st.markdown(
                """
                **Behind the Scenes**
                Speeding up search engine to handle the growing userbase.
                """
            )
    # Update Item 3
    u3 = st.container(border=True)
    with u3:
        col1, col2 = st.columns([1, 3])  # Reuse column layout
        with col1:
            st.image("UnderCon.png", width=300, use_container_width=False)  # Display image
        with col2:
            st.markdown(
                """
                **Linked-Search? Searched-in?**
                We are developing a way to foster a research based community, 
                allowing people around the world to read and collaborate on research
                  using this platform.
                """
            )
    
    # Spacer between news items
    st.write("\n" * 1)

st.markdown("""
    <hr style="border: 1px solid #eee; margin-top: 50px;">
    <div style="text-align: center; color: gray; font-size: small; max-width: 800px; margin: 0 auto; display: flex; justify-content: space-evenly; align-items: center;">
        <a href="/home" style="color: gray; text-decoration: none; padding: 5px 10px;">Home</a> | 
        <a href="/search" style="color: gray; text-decoration: none; padding: 5px 10px;">Search</a> |
        <a href="/news" style="color: gray; text-decoration: none; padding: 5px 10px;">News</a> |     
        <a href="/more" style="color: gray; text-decoration: none; padding: 5px 10px;">Learn More</a>
    </div>
     <div style="text-align: center; color: gray; font-size: small;">
        &copy; 2025 ResearchGenie Inc. All rights reserved. <br>
    </div>       
""", unsafe_allow_html=True)
