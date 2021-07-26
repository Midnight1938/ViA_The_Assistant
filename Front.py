from Backend.My_First_CB import Ask
from flask import Flask, render_template, request, jsonify, redirect
from Backend.My_First_CB import Ask as BotAsk
from Backend.My_First_CB import append_interaction_to_chat_log as ChatLog

user_responses = []
asst_responses = []

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return render_template("chat.html")
    
    if request.method == "POST":
        req = request.form
        print(req.keys)
        resp = req['user']
        asst = "Assistant: " + BotAsk(resp)
        #asst = BotAsk(resp)
        resp = "User: " + resp
        if asst is None:
            asst = "Hello, I am ViA, your personal Assistant or something"
        asst_responses.append(asst)
        asst_responses.reverse()
        user_responses.append(resp)
        user_responses.reverse()
        print(resp)
        print(len(user_responses))
        return render_template("chat.html", user_responses=user_responses, asst_responses = asst_responses, len_user=len(user_responses), len_asst=len(asst_responses))
    

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
    app.run(debug=True)