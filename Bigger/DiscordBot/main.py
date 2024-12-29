from discord import Intents, Client
from dotenv import load_dotenv
import responses
import os

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


def run_bot(token: str):
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    brain: dict = responses.load_brain('brain.json')

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content:
            print(f'{message.channel}: {message.author}: "{message.content}"')
            response: str = responses.get_response(message.content, brain=brain)
            await message.channel.send(response)
        else:
            print(f'Bot not mentioned in message: {message.content}')

    client.run(token=token)


if __name__ == '__main__':
    run_bot(token=DISCORD_TOKEN)
