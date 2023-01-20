#!/bin/bash

if [[ ! $(pip --version) ]]
then
    echo "[!] Please install python pip."
    exit
fi

if [ -z "$1" ]
then
    echo "[!] Please insert a chatgpt api key"
    exit
fi

echo "CHATGPT_API_KEY=$1" >> $HOME/.bashrc
echo "CHATGPT_API_KEY=$1" >> $HOME/.bash_profile

pip install openai

curl -L -o ~/.local/bin/chatgpt https://raw.githubusercontent.com/jerlysonsantos/chatgpt-client/main/chatgpt.py 

chmod 777 ~/.local/bin/chatgpt
