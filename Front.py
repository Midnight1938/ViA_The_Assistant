from flask import Flask, render_template, request
from Backend.My_First_CB import Ask as BotAsk


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(BotAsk(userText))

#if __name__ == "__main__":
#    app.run(host="0.0.0.0")