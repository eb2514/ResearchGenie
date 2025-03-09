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
When you receive a question along with several pages of text separated by the delimiter <----------DELIMITER---------->, your task is to produce one continuous, well-structured essay in a scientific, research paper-like style without any section headers or titles (except for the delimiters). For each page of provided text, you should summarize its content, explain its relevance, and analyze its key points while consistently referencing the information contained within that page. Each section corresponding to a page must be separated by the exact delimiter <----------DELIMITER---------->. After processing all pages, include a final, integrated discussion that expands on the topic and offers a cohesive conclusion, ensuring that the entire response remains a unified essay. The response should appear as follows:

response section 1 (your integrated summary, explanation, and analysis of the first page's content, presented in continuous essay form)
<----------DELIMITER---------->
response section 2 (your integrated summary, explanation, and analysis of the second page's content, presented in continuous essay form)
<----------DELIMITER---------->
(subsequent sections as needed for additional pages, each separated by the delimiter)
<----------DELIMITER---------->
(a final integrated discussion that expands on the topic and provides a comprehensive conclusion)

Remember, do not add any additional headers, titles, or breaks aside from the specified delimiter. The entire output should read as a seamless essay with the delimiter marking transitions between sections.
"""
