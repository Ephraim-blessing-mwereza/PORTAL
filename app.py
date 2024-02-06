import random


def get_response(user_input):
    responses = {
        "hi": ["Hello!", "Hi there!", "Hey!"],
        "how are you": ["I'm good, thanks!", "I'm doing well, how about you?"],
        "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
        "default": ["I'm not sure how to respond to that.", "Could you please rephrase that?", "I'm still learning!"],
    }

    input_lower = user_input.lower()
    if input_lower in responses:
        return random.choice(responses[input_lower])
    else:
        return random.choice(responses["default"])


def main():
    print("Welcome to the chatbot!")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)


if __name__ == "__main__":
    main()
