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
                {"role": "system", "content": "You are a cricket analyst. Only generate reports for real, individual cricket players. If the input is a team name, gibberish, or not a real player, respond with exactly: 'Invalid input. Please enter a real cricket player name.'"},
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
        with st.spinner("Generating scouting report..."):
            import time
            time.sleep(3)
            response = requests.post(url, headers=headers, json=payload)
            data = response.json()
        result = data["choices"][0]["message"]["content"]
        if "Invalid input. Please enter a real cricket player name." in result:
            st.warning("Invalid input. Please enter a real cricket player name.")
        else:
            st.write(result)
    else:
        st.warning("Please enter a player name.")