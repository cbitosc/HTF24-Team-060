'''from flask import Flask, request, jsonify
from rasa_core import Agent
from rasa_core.interpreter import RasaNLUInterpreter

app = Flask(__name__)

agent = Agent('models/current/dialogue',
              interpreter=RasaNLUInterpreter('models/current/nlu'))

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.get_json()['user_input']
    response = agent.handle_text(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)'''

from flask import Flask, request, jsonify
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

app = Flask(__name__)

# Define a dictionary to store the chatbot's responses
responses = {
    'hello': 'Hi, how are you?',
    'how are you': 'I\'m good, thanks!',
    'what is your name': 'My name is ChatBot',
    'default': 'I didn\'t understand that. Can you please rephrase?'
}

# Define a function to process the user's input
def process_input(user_input):
    # Tokenize the user's input
    tokens = nltk.word_tokenize(user_input)
    
    # Lemmatize the tokens
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Check if the user's input matches any of the predefined responses
    for lemma in lemmas:
        if lemma in responses:
            return responses[lemma]
    
    # If no match is found, return the default response
    return responses['default']

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.get_json()['user_input']
    response = process_input(user_input)
    return jsonify({'response': response})
