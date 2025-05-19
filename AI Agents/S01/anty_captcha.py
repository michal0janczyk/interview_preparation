# This script automates the process of solving a CAPTCHA-like challenge
# using OpenAI's GPT-4 model. It fetches a question from a webpage, uses the LLM to generate an answer,
# and then submits the answer to gain access to a secret page.
# Requirements:
# export OPENAI_API_KEY=your-api-key-here
# pip install requests openai

import os
import re
import requests
import time
from dotenv import load_dotenv
from openai import OpenAI

# Load .env with API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 1: Fetch login page
session = requests.Session()
url = 'https://xyz.ag3nts.org/'
html = session.get(url).text
print("🍪 Cookies:", session.cookies.get_dict())
inputs = re.findall(r'<input[^>]*>', html)
for tag in inputs:
    print(f"🔍 Found input tag: {tag}")

# Step 2: Extract question
match = re.search(r'Question:\s*<br\s*/?>\s*(.*?)\?', html, re.IGNORECASE)
if not match:
    raise Exception("❌ Could not find a recognizable question.")
question = match.group(1).strip() + '?'
print(f"🧠 Cleaned question: {question}")

# Step 3: Get answer from OpenAI LLM (gpt-3.5-turbo)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a concise quiz solver. Respond with one short answer only."},
        {"role": "user", "content": question}
    ]
)
answer = response.choices[0].message.content.strip()
print(f"🔍 Raw answer repr: {repr(answer)}")
answer = re.sub(r'[^\w\dąćęłńóśźżĄĆĘŁŃÓŚŹŻ]', '', answer)
print(f"✅ Sanitized Answer: {answer}")

# Step 4: Prepare form data
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Referer': url,
    'Origin': 'https://xyz.ag3nts.org'
}
payload = {
    'username': 'tester',
    'password': '574e112a',
    'answer': answer
}

# Step 5: Submit login
# Note: The server may require a delay between requests to avoid being blocked
time.sleep(2)
print("🔒 Submitting login form...")
post_response = session.post(url, headers=headers, data=payload)


# Step 6: Extract secret URL and follow it
if "Download the latest software" in post_response.text:
    print("✅ Login successful! Saving secret page...")
    with open("secret_page.html", "w", encoding="utf-8") as f:
        f.write(post_response.text)
else:
    print("❌ Login failed or secret page not found.")
    print("🔧 Server response preview:\n", post_response.text)
