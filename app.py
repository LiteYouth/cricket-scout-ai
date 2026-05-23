import streamlit as st
import requests
import os
API_KEY = os.environ.get("GROQ_API_KEY")
st.title("Cricket Scout AI")

player = st.text_input("Enter player name")
format = st.selectbox("Select format", ["Test", "ODI", "T20"])

if st.button("Generate Scouting Report"):
    if player:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "user", "content": f"""Give me a scouting report for {player} in {format} cricket.
Use this exact format:

Player: Rohit Sharma \n
Format: ODI \n
Strengths: Master of the pull shot, difficult to dismiss once set \n
Weaknesses: Vulnerable to inswing early in innings \n
Best Conditions: Flat tracks with true bounce \n
Verdict: Elite ODI batsman, match winner on his day \n

Now do the same for {player} in {format}."""}
            ]
        }
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        result = data["choices"][0]["message"]["content"]
        st.write(result)
    else:
        st.warning("Please enter a player name.")