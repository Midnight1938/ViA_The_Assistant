from Backend.My_First_CB import Ask
from flask import Flask, render_template, request, jsonify
from Backend.My_First_CB import Ask as BotAsk

app = Flask(__name__)
#create chatbot
#englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(englishBot)
#trainer.train("chatterbot.corpus.english") #train the chatter bot for english
#define app routes
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():
    if request.method == 'POST':
        the_question = request.form['question']
        response = BotAsk(the_question)
        return jsonify({"response": response })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)