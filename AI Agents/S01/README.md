🤖 Anty-Captcha Agent
=====================

This Python script automates logging into a protected website using OpenAI's language model to answer
an anti-bot question (CAPTCHA-like). It simulates a real user session by solving the dynamic question,
submitting login credentials, and retrieving the secret page.

------------------------------------------------------------

🔧 Requirements:
- Python 3.11+
- OpenAI API Key
- Packages: `requests`, `openai`, `python-dotenv`

------------------------------------------------------------

🛠️ Setup Instructions:

1. Install dependencies:
   pip install openai requests python-dotenv

2. Create a .env file in the same folder with the following line:
   OPENAI_API_KEY=sk-your-openai-api-key

   You can get your API key from:
   https://platform.openai.com/account/api-keys

------------------------------------------------------------

▶️ How to Run:

   python anty_captcha.py

This will:
- Fetch the login page
- Extract the anti-human question
- Use GPT-3.5-turbo to answer it
- Submit credentials with the answer
- Save the secret page to `secret_page.html` (if login succeeds)

------------------------------------------------------------

✅ Sample Output:

🧠 Cleaned question: Rok zrzucenia bomby na Hiroszimę?

🔍 Raw answer repr: '1945'

✅ Sanitized Answer: 1945

🔒 Submitting login form...

✅ Login successful! Saving secret page...

------------------------------------------------------------

📁 Output:

If login is successful, the secret page will be saved to:
  ./secret_page.html

------------------------------------------------------------

📄 License:
MIT License
