#!/usr/bin/env python

from time import sleep
from random import uniform
import sys
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

def typewritter_effect(text):
    green = "\033[0;32m"

    for x in text:
        print(green + x, end='')
        sys.stdout.flush()
        sleep(uniform(0, 0.1))
    print('\n')

def __main__():
    white = "\033[0;37m"
    api_key = ""
    try:
         api_key = os.environ["CHATGPT_API_KEY"]
    except KeyError:
        print("Missing CHATGPT_API_KEY")
        exit(1)

    print("Welcome to ChatGPT\nType \"exit\" if you want to quit\n")
    while True:
        try:
            prompt = input(white + "> ")
            if prompt:
                if prompt == 'exit':
                    break

                text = do_json(prompt, api_key)
                typewritter_effect(text)
        except EOFError:
            break

__main__()
