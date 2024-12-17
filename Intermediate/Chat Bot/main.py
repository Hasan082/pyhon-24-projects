from difflib import get_close_matches
import json


def get_best_match(user_questions: str, list_questions: dict) -> str | None:
    all_questions: list[str] = list(list_questions.keys())
    matches: list[str] = get_close_matches(user_questions, all_questions, n=1, cutoff=0.6)
    if matches:
        return matches[0]


def chat_boot(knowledge: dict):
    while True:
        user_questions = input("You: ")
        best_match: str | None = get_best_match(user_questions, knowledge)
        if 'bye' in user_questions.lower():
            print(f"Bot: Goodbye! Have a great day!")
            break
        if answer := knowledge.get(best_match):
            print(f"Bot: {answer}")
        else:
            print(f"Bot: I could not recognize your question. Could you rephrase it?")


def load_knowledge(json_file: dict) -> dict:
    with open(json_file, 'r') as file:
        return json.load(file)


def main():
    questions = load_knowledge("brain.json")
    chat_boot(questions)


if __name__ == '__main__':
    main()
