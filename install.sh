#!/bin/bash

if [[ ! $(pip --version) ]]
then
    echo "[!] Please install python pip."
    exit
fi

pip install openai

curl -L -o ~/.local/bin/chatgpt https://raw.githubusercontent.com/jerlysonsantos/chatgpt-client/main/chatgpt.py 

chmod +x ~/.local/bin/chatgpt
