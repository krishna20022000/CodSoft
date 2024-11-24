import re

# Predefined responses for different types of input
def respond_to_input(user_input):
    user_input = user_input.lower().strip()  # Normalize input (lowercase, remove leading/trailing spaces)

    # Greeting responses
    if re.match(r"hello|hi|hey", user_input):
        return "Hello! How can I assist you today?"
    
    # Asking for name
    elif "your name" in user_input or "who are you" in user_input:
        return "I am a simple chatbot, created to help you with basic queries!"
    
    # Asking how the bot is doing
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! Thanks for asking."
    
    # Asking for time (this can be extended)
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    
    # Asking for help
    elif "help" in user_input:
        return "I can help you with general questions. Try asking me about my name or how I'm doing!"
    
    # Saying goodbye
    elif re.match(r"bye|goodbye|see you", user_input):
        return "Goodbye! It was nice talking to you."
    
    # Random response for unclear input
    else:
        return "I'm sorry, I didn't quite understand that. Could you rephrase?"

# Main chatbot loop
def chat():
    print("Chatbot: Hello! I am your assistant bot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # If the user says 'bye', end the chat
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get the bot's response based on the input
        response = respond_to_input(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
