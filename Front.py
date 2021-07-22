from Backend.My_First_CB import Ask
from flask import Flask, render_template, request, jsonify
from Backend.My_First_CB import Ask as BotAsk
from Backend.My_First_CB import append_interaction_to_chat_log as ChatLog


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
#function for the bot response

def get_bot_response():
    userText = request.args.get('messageText')
    return str(BotAsk(userText)) ##?  To chatPanel

#def Bot()
#    incoming_msg = 
#    chat_log = 
#
#    answer = BotAsk(incoming_msg, chat_log)
#    session['chat_log'] = ChatLog(incoming_msg, answer, chat_log)
#    if answer is None:
#        answer = "Hello, I am ViA, your personal Assistant or something"
#    response = message(answer)
#    return response.__str__()
#? Chat_Log Access would go great.


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)