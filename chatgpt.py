#!/usr/local/bin/python

import os
import json
import openai

def do_json(prompt, api_key):
    openai.api_key = api_key
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        temperature=0,
    )
    return completions.choices[0].text

api_key = ""
try:
     api_key = os.environ["CHATGPT_API_KEY"]
except KeyError:
    print("Missing CHATGPT_API_KEY")
    exit(1)

while True:
    try:
        prompt = input("> ")
        if prompt:
            if prompt == 'exit':
                break

            text = do_json(prompt, api_key)
            print(text)
    except EOFError:
        break
