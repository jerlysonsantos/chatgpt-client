#!/bin/bash

if [[ ! $(pip --version) ]]
then
    echo "[!] Please install python pip."
    exit
fi

echo -n "Please enter a chatgpt api key: "
read CHATGPT_API_KEY

echo "CHATGPT_API_KEY=$CHATGPT_API_KEY" >> $HOME/.bashrc
echo "CHATGPT_API_KEY=$CHATGPT_API_KEY" >> $HOME/.bash_profile

pip install openai

curl -L -o ~/.local/bin/chatgpt https://raw.githubusercontent.com/jerlysonsantos/chatgpt-client/main/chatgpt.py 

chmod 777 ~/.local/bin/chatgpt
