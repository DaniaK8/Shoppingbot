from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a chatbot instance
chatbot = ChatBot('ShoppingChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

@app.route('/')
def index():
    return render_template('index_shopping_chatbot.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    bot_response = chatbot.get_response(user_message).text
    return {'response': bot_response}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)