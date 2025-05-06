import streamlit as st

# Set up chatbot title
st.set_page_config(page_title="TN IT Placement ChatBot", layout="centered")
st.title("IT Placement ChatBot - Tamil Nadu")

# Sample IT company placement information
placement_info = {
    "Infosys": "Infosys has offices in Chennai and Mahindra World City. They conduct campus recruitment and off-campus drives frequently.",
    "TCS": "TCS has a major presence in Chennai. They offer placements through the NQT and direct campus recruitment.",
    "Cognizant": "Cognizant is headquartered in Chennai and offers bulk recruitment through campuses and walk-ins.",
    "Wipro": "Wipro has offices in Chennai and Coimbatore. Placements are offered via their Elite National Talent Hunt.",
    "HCL": "HCL has a major campus in Madurai and Chennai. They run a program called HCL TechBee for freshers.",
    "Zoho": "Zoho, based in Chennai, regularly conducts off-campus drives and hires from regional colleges."
}

# Function to process user input
def get_bot_response(message):
    message = message.lower()
    if "company" in message or "list" in message:
        return "Here are some IT companies in Tamil Nadu: " + ", ".join(placement_info.keys())
    for company in placement_info:
        if company.lower() in message:
            return placement_info[company]
    if "placement" in message or "opportunities" in message:
        return "Tamil Nadu has many placement opportunities through campus drives and walk-ins. Ask about a specific company for more details."
    elif "hello" in message or "hi" in message:
        return "Hello! Ask me about IT company placements in Tamil Nadu."
    elif "thanks" in message or "thank you" in message:
        return "You're welcome!"
    else:
        return "Sorry, I can only help with IT placement information in Tamil Nadu."

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You:", key="input")

if user_input:
    # Add user message
    st.session_state.chat_history.append(("You", user_input))
    
    # Get bot response
    bot_response = get_bot_response(user_input)
    st.session_state.chat_history.append(("Bot", bot_response))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")

