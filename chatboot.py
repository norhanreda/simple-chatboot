
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hello, how can I help you?"]),
    (r"what is your name?", ["My name is Chatbot."]),
    (r"how are you?", ["I'm doing well, thank you!"]),
    (r"bye|goodbye", ["Goodbye, have a nice day!"]),
]

# Define a function to run the chatbot
def run_chatbot():
    print("Welcome to Chatbot! Please enter your input below.")
    chatbot = Chat(patterns, reflections)
    chatbot.converse()

# Run the chatbot
run_chatbot()


