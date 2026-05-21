# =========================================
# Advanced Basic Chatbot in Python
# CodeAlpha Internship Project
# =========================================

import datetime

# =========================================
# Chatbot Function
# =========================================

def chatbot_response(user_input):

    # Convert input to lowercase
    user_input = user_input.lower()

    # Greetings
    greetings = ["hello", "hi", "hey"]

    if user_input in greetings:
        return "Hello! 👋 Nice to meet you."

    # How are you
    elif "how are you" in user_input:
        return "I'm fine and ready to help you! 😊"

    # Name
    elif "your name" in user_input:
        return "I am an Advanced Python Chatbot 🤖"

    # Time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"⏰ Current Time is: {current_time}"

    # Date
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        return f"📅 Today's Date is: {current_date}"

    # Help
    elif "help" in user_input:
        return (
            "You can ask me:\n"
            "- hello\n"
            "- how are you\n"
            "- what is your name\n"
            "- time\n"
            "- date\n"
            "- bye"
        )

    # Goodbye
    elif user_input == "bye":
        return "Goodbye! 👋 Have a great day."

    # Unknown Input
    else:
        return "❌ Sorry, I don't understand that."

# =========================================
# Main Program
# =========================================

print("====================================")
print("      🤖 ADVANCED CHATBOT")
print("====================================")
print("Type 'help' to see commands.")
print("Type 'bye' to exit.")

# Chat Loop
while True:

    # User Input
    user_message = input("\nYou: ")

    # Empty Input Check
    if user_message.strip() == "":
        print("Bot: ⚠ Please type something.")
        continue

    # Get Bot Response
    response = chatbot_response(user_message)

    # Print Response
    print("Bot:", response)

    # Exit Condition
    if user_message.lower() == "bye":
        break

# Ending Message
print("\n✅ Chatbot Program Ended.")
