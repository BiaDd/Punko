import os
import discord
import json
import requests
import random
from keep_alive import keep_alive

API_URL = 'https://api-inference.huggingface.co/models/BiaDd/'


class MyBot(discord.Client):

    def __init__(self, model_name):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.api_endpoint = API_URL + model_name
        hf_token = "HUGGING FACE TOKEN HERE"
        self.request_headers = {'Authorization': 'Bearer {}'.format(hf_token)}

    def query(self, payload):
        """
          make request to the Hugging Face model API
          """
        data = json.dumps(payload)
        response = requests.request('POST',
                                    self.api_endpoint,
                                    headers=self.request_headers,
                                    data=data)
        ret = json.loads(response.content.decode('utf-8'))
        return ret

    def random_emoji(self, message):
        emojis = message.guild.emojis
        if emojis:
            return str(random.choice(emojis))
        return ''

    async def on_message(self, message):
        if message.author.id == self.user.id or self.user not in message.mentions:
            return
        payload = {
            'inputs': {
                'text': message.content
            },
            "options": {
                "wait_for_model": True
            }
        }

        random_int = random.randint(1, 3)

        async with message.channel.typing():
            response = self.query(payload)
        bot_response = response.get('generated_text', None)

        if not bot_response:
            # print(response)
            if 'error' in response:
                bot_response = '`Error: {}`'.format(response['error'])
            else:
                bot_response = 'Hmm... something is not right.'

        # send the model's response to the Discord channel

        match random_int:
            case 1:
                await message.channel.send(self.random_emoji(message) + bot_response)
            case 2:
                await message.channel.send(bot_response + self.random_emoji(message))
            case 3:
                await message.channel.send(self.random_emoji(message))
                await message.channel.send(bot_response)
            case _:
                await message.channel.send(bot_response)


def main():
    client = MyBot('DialoGPT-medium-Punko')
    keep_alive()
    client.run("DISCORD TOKEN HERE")


if __name__ == '__main__':
    main()
