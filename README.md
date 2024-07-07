# GenAI_project
2024 genAI voice ai assistant bot

## pre-prepare (dotenv)
- an usable openAI secret key
- a discord bot token

## usage:
- press U to record voice, and release to save the voice file.
- The voice will be passed to the model which controls speech to text
- the text will be passed to text to text model to determinate the commands
- the ultimate text will be passed t text to speech model for voice outcomes.

## How to use
terminal 1
- cd .\marytts-installer-5.2\
- .\marytts.bat

terminal 2
-python main_folder\s2t2t2s.py
