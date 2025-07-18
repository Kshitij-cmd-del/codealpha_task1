def basic_chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. You can say 'hello', 'how are you', or 'bye'.")

    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easier matching

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # Exit the loop to end the chat
        else:
            print("Chatbot: I don't understand that. Please try 'hello', 'how are you', or 'bye'.")

if __name__ == "__main__":
    basic_chatbot()