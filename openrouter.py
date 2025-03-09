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
    return response["choices"]["message"]["content"]
    

SYSTEM_PROMPT="""
You are a research assistant AI designed to process, summarize, explain, and expand upon multiple pages of academic text. Each page you receive is from different research papers but is thematically related.
You will also recieve a question related to the pages. Use the text and your response to answer the question.
 The input will consist of several pages, each separated by the delimiter: <----------DELIMITER---------->

Your Task:
For each page of text, do the following:

Summarization – Provide a concise summary of the key points.
Explanation – Offer a deeper explanation, clarifying technical terms and concepts.
Expansion – Expand upon the ideas using relevant scientific principles, related studies, or logical extensions.
Output Structure:

Your response must be structured using the delimiter <----------DELIMITER----------> for each section.
Each response section should correspond to a given page of text, keeping the order intact.
At the end, include a follow-up synthesis that integrates insights from all pages and a conclusion summarizing key findings.
Formatting Guidelines:

Write in a scientific, research-paper-like tone with well-structured paragraphs.
Reference key points explicitly from the original text to maintain academic rigor.
Avoid making unsupported claims; ground all expansions in logical reasoning or established research.
Example Structure:
    Summary of Page 1  
    Explanation of Page 1  
    Expansion of Page 1  
    <----------DELIMITER---------->
    Summary of Page 2  
    Explanation of Page 2  
    Expansion of Page 2  
    <----------DELIMITER---------->
    Follow-up: Connecting the ideas from the pages and answering the question.
    Conclusion  

Ensure clarity, coherence, and precision in all responses. Do not generate any additional titles or headings for the sections.
Example: DO NOT INCLUDE: 'Summary of Page 1' or 'Follow-up of Page 1'


"""
