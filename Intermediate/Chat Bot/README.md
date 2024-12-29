# Python Chatbot Project

This Python script implements a simple chatbot that can answer questions based on a predefined set of knowledge stored in a JSON file. The bot uses the `difflib` library to find the closest matching question from a set of predefined questions and provides a relevant answer. The chatbot continues to interact with the user until the user says "bye".

## Features

- The chatbot can respond to user questions based on a predefined knowledge base stored in a JSON file.
- It uses `difflib.get_close_matches` to find the closest matching question.
- The chatbot stops when the user types "bye".
- The knowledge base is loaded from a `brain.json` file.

## Requirements

Before running the script, ensure that you have the following dependencies installed:

- Python 3.7 or higher

No external libraries are required for this project, as it uses Python's built-in `difflib` and `json` libraries.

## Setup

1. **Prepare the `brain.json` file**: Create a `brain.json` file that contains a dictionary of questions and answers. Here is an example structure for the `brain.json` file:

   ```json
   {
       "What is your name?": "I am a Python chatbot.",
       "How are you?": "I am doing well, thank you!",
       "What can you do?": "I can answer questions based on my knowledge base.",
       "bye": "Goodbye! Have a great day!"
   }
   ```

2. **Run the chatbot**:

   After setting up the `brain.json` file, run the script:

   ```bash
   python chatbot.py
   ```

   The bot will prompt you with "You:", where you can ask questions. The bot will respond with the closest matching answer from the `brain.json` file. If the bot doesn't recognize the question, it will ask you to rephrase it.

3. **Stop the chatbot**:

   Type `bye` to exit the chatbot.

## Code Overview

- **get_best_match**: This function compares the user's question with the questions in the knowledge base (`brain.json`) and returns the closest match using `difflib.get_close_matches`.
- **chat_boot**: The chatbot loop. It continuously asks the user for input and provides responses based on the knowledge base. It stops when the user types "bye".
- **load_knowledge**: Loads the knowledge base (a JSON file) into a Python dictionary.
- **main**: The entry point of the program. It loads the knowledge base and starts the chatbot.

## License

This project is licensed under the MIT License
