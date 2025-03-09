import requests
import json
import streamlit as st

# Replace with your actual values
OPENROUTER_API_KEY = st.secrets["OPENROUTER"]
# YOUR_SITE_URL = "YOUR_SITE_URL"  # e.g., "https://yourwebsite.com"
# YOUR_SITE_NAME = "YOUR_SITE_NAME"  # e.g., "MyChatApp"

def get_response(content):

    payload = {
    "model": "qwen/qwq-32b:free",
    "messages": [
        {
            "role": "system",
            "content":f"{content}"
        },
        {
            "role": "user",
            "content": f"{SYSTEM_PROMPT}"  # Replace with your query
        }
    ],
    "temperature": 0.6,
    "top_p": 0.95,          # Nucleus sampling threshold
    "top_k": 40,            # Vocabulary limit for top_k sampling (experiment with 20–40)
    "min_p": 0.01,          # Minimum probability for tokens (defaults to 0.0 if unsupported)
    "repetition_penalty": 1.0,  # 1.0 = disabled (adjust between 1.0 to 1.2 if needed)
    }



    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        # "HTTP-Referer": YOUR_SITE_URL,  # Optional metadata
        # "X-Title": YOUR_SITE_NAME      # Optional metadata
    },
    json=payload  # Use "json=" instead of "data=json.dumps()" for clarity
    )
    response = response.json()
    #print(response["choices"]["message"]["content"])
    return response["choices"][0]["message"]["content"]
    

SYSTEM_PROMPT="""
When you receive a question along with one or more pages of text (each separated by the delimiter <----------DELIMITER---------->), your task is to produce an integrated, continuous essay without any additional headers or titles. For each provided page, write one seamless section that summarizes, explains, and analyzes the content of that page. Do not create extra sections if only one page is given—each section must correspond exactly to one page of text.
After processing all pages, append one final section—following the last delimiter—that expands on the ideas presented, directly answers the original question, and provides a comprehensive conclusion. The overall structure is as follows:
A section for each page (one per page, each section separated by <----------DELIMITER---------->).
A final section after the last delimiter that integrates and expands on the information, addresses the question, and concludes the discussion.
The entire response should read as a continuous, cohesive essay with the delimiter marking the transitions between sections.
"""
