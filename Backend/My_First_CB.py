import os
import openai

openai.organization = "org-3fzd1diTNiEXq31xdIG8dViM"
openai.api_key = "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"
completion = openai.Completion()


name = "Human"
BotName = "ViA"
start_sequence = "\nViA:"
restart_sequence = f"\n{name} "
session_prompt = "This is ViA, your personal Assistant here to help you at every step"
question = "What are the sustainable development goals?"


def Ask(question):
    log = session_prompt
    Ans = Asker(question, log)
    log = append_interaction_to_chat_log(question, Ans, log)
    return Ans


def Asker(question, chat_log=None):
    prompt_text = f"{chat_log}{restart_sequence}: {question}{start_sequence}:"
    try:
        response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.3,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.1,
        stop=["\n"],
    )
        story = response["choices"][0]["text"]
    except:
        story = "Error Occured, Contact Maker" 
    return story


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}"