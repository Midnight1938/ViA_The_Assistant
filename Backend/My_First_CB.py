import os
import openai

openai.organization = "org-3fzd1diTNiEXq31xdIG8dViM"
openai.api_key = "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"
completion = openai.Completion()

name = "Human"
start_sequence = "\nViA:"
restart_sequence = f"\n{name} "
session_prompt = "This is ViA, your personal Assistant here to help you at every step"
question = "What are the sustainable development goals?"


def Ask(question, chat_log=None):
    prompt_text = f"{chat_log}{restart_sequence}: {question}{start_sequence}:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.4,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"], )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt 
        return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}"


#Name = str(input("Whats your Name? "))
#while True:
#    question = str(input(f"{Name}: "))
#    if question == "BREAK":
#        break
#    print("Via: ",Ask(question, chat_log=None))
#