# GenAI_project
2024 genAI voice ai assistant bot

## pre-prepare (dotenv)
make a file named .env, within it should contain:
- an usable openAI secret key
  ```
  openaiTOKEN=<OPEN_AI_SECRET_KEY>
  ```
- a discord bot token
  ```
  BOT_TOKEN==<DISCORD_BOT_TOKEN>
  ```
- modify the discord bot token in the discordbotyeah.py too

## usage:
- press U to record voice, and release to save the voice file.
- The voice will be passed to the model which controls speech to text
- the text will be passed to text to text model to determinate the commands
- the ultimate text will be passed t text to speech model for voice outcomes.

## How to use
- Execute the commands below
  - cd .\marytts-installer-5.2\
  - .\marytts.bat

- switch to another terminal and d the command:
  -python main_folder\s2t2t2s.py 
