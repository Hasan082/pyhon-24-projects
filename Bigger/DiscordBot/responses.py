from difflib import get_close_matches
import json


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list[str] = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    if matches:
        return matches[0]


def get_response(message: str, brain: dict) -> str | None:
    best_match: str = get_best_match(message, brain)

    if answer := brain.get(best_match):
        return answer
    else:
        return f"I couldn't find anything for you. Please try again."


def load_brain(file: str) -> dict:
    with open(file) as f:
        return json.load(f)


if __name__ == '__main__':
    test_brain: dict = load_brain('brain.json')
    text_response: dict = get_response('bye', brain=test_brain)
    print(text_response)
