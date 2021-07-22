from Backend.My_First_CB import Ask
from flask import Flask, render_template, request
from Backend.My_First_CB import Ask as BotAsk

app = Flask(__name__)
#create chatbot
#englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(englishBot)
#trainer.train("chatterbot.corpus.english") #train the chatter bot for english
#define app routes
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(BotAsk(userText))
if __name__ == "__main__":
    app.run(debug=True)