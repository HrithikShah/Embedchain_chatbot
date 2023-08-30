import os
from embedchain import App
from dotenv import load_dotenv

# Create a bot instance
load_dotenv()
os.environ["OPENAI_API_KEY"]
chat_bot = App()

# Embed online resources
def train(file):
    chat_bot.add(file)


# Query the bot
def query(question):
    response=chat_bot.query(question)
    return str(response)
