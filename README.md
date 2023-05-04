# Punko Discord Bot 

<div align="center">
  <img src="https://github.com/BiaDd/Punko/blob/main/gifs_and_images/poo.PNG" width=320>
</div>


This is a personal project meant for learning AI. I have integrated a few custom AI models to develop an AI Chatbot and an AI image generation feature for this bot

The AI Chatbot portion of this bot uses the [Microsoft DialoGPT conversational model](https://huggingface.co/microsoft/DialoGPT-medium) trained with message from people in family groupchat. I followed [Lynn Zheng's tutorial](https://www.freecodecamp.org/news/discord-ai-chatbot/) to create this portion of the bot.

Here is a demo of the Discord bot AI chat function.
<div>
  <img src="https://github.com/BiaDd/Punko/blob/main/gifs_and_images/discord.gif" width=300>
</div>

You can also directly chat with the model hosted on [Hugging Face's Model Hub](https://huggingface.co/BiaDd/DialoGPT-medium-Punko).
<div>
  <img src="https://github.com/BiaDd/Punko/blob/main/gifs_and_images/huggingface.gif" width=300>
</div>

## Structure of this Project

- `model_train_upload_workflow.ipyb`: Notebook to be run in Google Colab to train and upload the model to Hugging Face's Model Hub
- `DreamBooth_Stable_Diffusion.ipynb`: Notebook to train the image generation stable diffusion model
- `main.py`: Script to be imported into a Repl.it Python Discord.py project

## Roadmap

- [x] Train AI chatbot
- [x] Integrate AI chatbot with discord boy 
- [x] Train image generation model
- [ ] Integrate image generation model with discord bot


## Resource Links

- [Lynn Zheng's blog on freeCodeCamp](https://www.freecodecamp.org/news/discord-ai-chatbot/)
- [Lynn Zheng's video](https://youtu.be/UBwvFuTC1ZE)
- [Stable Diffusion Tutorial by SECourses](https://www.youtube.com/watch?v=mnCY8uM7E50&list=PL_pbwdIyffsmclLl0O144nQRnezKlNdx3)
- [My AI conversational chatbot model](https://huggingface.co/r3dhummingbird/DialoGPT-medium-joshua)
- [My AI image generation model WORK IN PROGRESS]()