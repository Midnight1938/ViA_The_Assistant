from flask import Flask, render_template, request, jsonify
from Backend.My_First_CB import Ask as BotAsk
from Backend.My_First_CB import append_interaction_to_chat_log as ChatLog


app = Flask(__name__)


def hello():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    message = request.form["messageText"]
    # kernel now ready for use
    while True:
        if message == "quit":
            exit()
        else:
            bot_response = BotAsk(message)
            # print bot_response
            return jsonify({"status": "OK", "answer": bot_response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888", debug=True)

