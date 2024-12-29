# Discord Bot Project

This is a simple Python-based Discord bot that uses the `discord.py` library to interact with users and respond based on predefined responses loaded from a JSON file. The bot listens for messages and provides relevant responses.

## Features

- Responds to messages in a Discord server based on predefined responses.
- Uses `dotenv` to securely load the Discord token from an `.env` file.
- Bot listens for messages and sends a response based on content.

## Requirements

Before running the bot, ensure that you have the following dependencies installed:

- Python 3.7 or higher
- `discord.py` library
- `python-dotenv` library

You can install these dependencies using pip:

```bash
pip install discord.py python-dotenv
```

## Setup

1. **Create an `.env` file** in the root directory of your project with the following content:

   ```ini
   DISCORD_TOKEN=your_discord_token_here
   ```

   Replace `your_discord_token_here` with the actual Discord bot token. You can create a bot and get the token by following the [Discord Developer documentation](https://discord.com/developers/docs/intro).

2. **Set up a `brain.json` file** containing the predefined responses. This file will be loaded when the bot starts. Ensure this file contains the appropriate responses in JSON format.

3. **Run the bot**:

   Once you have the necessary files set up, you can start the bot by running the Python script:

   ```bash
   python main.py
   ```

   The bot should now be online and ready to respond to messages in your server.

## Code Overview

- The bot uses `discord.py` to interact with the Discord API.
- `dotenv` is used to load environment variables securely from the `.env` file.
- `responses.py` is assumed to be a custom module that contains the logic for loading the brain (predefined responses) and generating responses based on the incoming message.

### Example `brain.json` structure:

Here’s a simple example of what the `brain.json` might look like:

```json
{
  "hello": "Hi there! How can I help you today?",
  "bye": "Goodbye! Have a great day!"
}
```

### Example `responses.py` structure:

This file should include the functions to load the brain (responses) and generate responses based on the user's input. Here's a basic example:

```python
import json

def load_brain(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_response(message_content, brain):
    return brain.get(message_content.lower(), "Sorry, I don't understand that.")
```

## License

This project is licensed under the MIT License
