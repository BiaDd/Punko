import discord
import responses
import json

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    with open("config.json", "r") as f:
        secrets = json.load(f)
    TOKEN = secrets["TOKEN"]
    client = discord.Client()


    @client.event
    async def on_ready():
        print(f'{client.user} is now running')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        user_message = str(message.content)
        await send_message(message, user_message)

    client.run(TOKEN)
