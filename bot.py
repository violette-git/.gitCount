
import discord
import responses
from dotenv import load_dotenv
load_dotenv()
import os


async def send_message(message, param, user_message ):
    try:
        response = responses.get_response(message, user_message)

        await message.channel.send(response)

    except Exception as e:
        
        print(e)

def run_bot():


    token = os.environ.get('TOKEN')
    # test = os.environ
    print(token)
    # print(test)

    intents = discord.Intents.default()

    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():

        print(f'{client.user} is on!')

    @client.event
    async def on_message(message):

        if message.author == client.user:

            return

        # username = str(message.author)

        embeds = message.embeds

        # channel = str(message.channel)

        for embed in embeds:

            author = embed.author.name

            title = embed.title

            # print(f'{title}\n{author}')
        user_message = str(message.content)
        # print(user_message)
        await send_message(message, embeds, user_message)

    
    client.run(token)