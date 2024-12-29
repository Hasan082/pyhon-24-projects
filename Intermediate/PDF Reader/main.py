import re
from collections import Counter
from PyPDF2 import PdfReader


def extract(pdf) -> list[str]:
    with open(pdf, 'rb') as fdf:
        reader = PdfReader(fdf, strict=False)
        print("Total pages", len(reader.pages))
        print('-' * 20)

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text


def count_word(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        all_words += [word for word in split_text if word]
    return Counter(all_words)


def main():
    extract_text: list[str] = extract('sample-12.pdf')
    counter: Counter = count_word(extract_text)
    print(extract_text)
    output = (
        f"Total Characters: {sum(len(word) for word in extract_text)}\n"
        f"Total Words: {sum(counter.values())}\n\n"
        "Top 10 most used words are below:\n"
        f"{'-' * 33}"
    )
    print(output)

    for i, (word, mention) in enumerate(counter.most_common(10), start=1):
        print(f'{i:2} - {word:12}: {mention} times')


if __name__ == '__main__':
    main()
