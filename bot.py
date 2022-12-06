
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

        # print(message.content)

        # channel = str(message.channel)

        for embed in embeds:

            author = embed.author.name

            title = embed.title

            n = 1

            groups = title.split('] ')

            ' '.join(groups[:n])
            
            ' '.join(groups[n:])
            # print(user_messaged)
            user_messaged = groups[1]
            # print(user_messaged)
            # print(message.content)
            
            # print(f'{title}\n{author}\n')

            # return user_messaged
            
        user_message = str(message.content)
        # print(type(user_message))

        # print(user_message)
        await send_message(message, embeds, user_message)

    
    client.run(token)