import os
from embedchain import App
from dotenv import load_dotenv

# sqlite3 is not supporting the function
# so we write below lines for using pysqlite3 
#[ this was required for deployment in pythonanywhere

import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

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
