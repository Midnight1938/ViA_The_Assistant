from flask import Flask, render_template, request
from Backend.My_First_CB import Ask as BotAsk
from Backend.My_First_CB import append_interaction_to_chat_log as ChatLog

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def samplefunction():
    if request.method == "GET":
        return render_template("new.html")
    if request.method == "POST":

        human1 = request.form["human"]
        bot = BotAsk(human1)
        return render_template("new.html", bot=bot)


if __name__ == "__main__":
    app.run(debug=True)
