from Backend.My_First_CB import Ask
from flask import Flask, render_template, request, jsonify
from Backend.My_First_CB import Ask as BotAsk


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")

#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(BotAsk(userText))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)