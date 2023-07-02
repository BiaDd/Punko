import os
import discord
import json
import requests
import random
from PIL import Image
import io
from keep_alive import keep_alive

CHATBOT_URL = 'https://api-inference.huggingface.co/models/BiaDd/DialoGPT-medium-Punko'
DREAMBOOTH_URL = 'https://api-inference.huggingface.co/models/BiaDd/Dreambooth-Punko'


class MyBot(discord.Client):

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.api_endpoint = CHATBOT_URL
        self.api_endpoint_draw = DREAMBOOTH_URL
        hf_token = os.environ['HUGGINGFACE_TOKEN']
        self.request_headers = {
            'Authorization': 'Bearer {}'.format(hf_token),
            "X-Wait-For-Model": "true",
            "X-Use-Cache": "false"
        }

    def query(self, payload, payload_type=1):
        """
          make request to the Hugging Face model API
          """
        data = json.dumps(payload)
        response = requests.request('POST',
                                    self.api_endpoint_draw,
                                    headers=self.request_headers,
                                    data=data)
        if payload_type == 1:
            ret = json.loads(response.content.decode('utf-8'))
        elif payload_type == 2:
            ret = Image.open(io.BytesIO(response.content))

        return ret

    def random_emoji(self, message):
        emojis = message.guild.emojis
        if emojis:
            return str(random.choice(emojis))
        return ''

    # def slugify(text):
    #   # remove non-word characters and foreign characters
    #   text = re.sub(r"[^\w\s]", "", text)
    #   text = re.sub(r"\s+", "-", text)
    #   return text

    async def on_ready(self):
        await self.change_presence(activity=discord.Game('Cyberpoop'))

    async def on_message(self, message):

        if message.author.id == self.user.id or (self.user not in message.mentions):
            return
        draw = 1
        payload = {
            'inputs': {
                'text': message.content
            },
            "options": {
                "wait_for_model": True
            }
        }
        author_mention = f'<@{message.author.id}>'
        random_int = random.randint(1, 4)

        if message.content.startswith('!draw'):
            payload = {"inputs": message.content.split(' ', 1)[1]}
            draw = 2
        async with message.channel.typing():
            response = self.query(payload, draw)

        if draw == 1:
            bot_response = response.get('generated_text', None)
        elif draw == 2:
            response.save(f"temp.png")
            bot_response = 'success'
            random_int = 5

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
            case 4:
                await message.channel.send(bot_response)
            case _:
                if os.path.isfile("temp.png"):
                    await message.channel.send(f'{author_mention}', file=discord.File('temp.png'))
                    os.remove("temp.png")
                else:
                    await message.channel.send("I couldn't draw that")


def main():
    client = MyBot()
    keep_alive()
    client.run(os.environ['DISCORD_TOKEN'])


if __name__ == '__main__':
    main()