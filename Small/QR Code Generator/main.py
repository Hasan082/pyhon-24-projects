import qrcode
from pathlib import Path


def generate_qr(qr_text: str) -> str:
    base_name = "qr"
    img_ext = ".png"
    counter = 1
    filename = f"{base_name}_{counter}.{img_ext}"
    while Path(filename).exists():
        filename = f"{base_name}_{counter}.{img_ext}"
        counter += 1
    img = qrcode.make(qr_text)
    img.save(filename)
    return qr_text


if __name__ == '__main__':
    input_text = input("Enter your text: ")
    generate_qr(input_text)
