print("======================================")
print("        CODSOFT AI CHATBOT")
print("======================================")
print("Hello! I am your AI chatbot.")
print("Type 'bye' whenever you want to exit.\n")


def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! Nice to meet you. How can I help you?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    elif "your name" in user_input:
        return "I am a Rule-Based AI Chatbot created for my CodSoft internship."

    elif "what can you do" in user_input:
        return "I can answer basic questions using predefined rules."

    elif "thank" in user_input:
        return "You're welcome!"

    elif "bye" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that yet. Try asking something else."


while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if "bye" in user_input.lower():
        break