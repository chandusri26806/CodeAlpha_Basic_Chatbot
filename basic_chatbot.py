def chatbot_response(user_input):
    user_input=user_input.lower()
    if user_input=="hello" or user_input=="hi":
        return "Hello! How are you?"
    elif user_input=="how are you":
        return "I'm fine, thank you!"
    elif user_input=="thanks" or user_input=="thank you":
        return "You're welcome!"
    elif user_input=="bye" or user_input=="goodbye":
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I don't understand that."
print("BASIC PYTHON CHATBOT")
print("Type 'bye' or 'goodbye' to exit.")
while True:
    user_input=input("\nYou: ")
    response=chatbot_response(user_input)
    print("Bot:",response)
    if user_input.lower()=="bye" or user_input.lower()=="goodbye":
        break
