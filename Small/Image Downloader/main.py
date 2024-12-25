import os
import requests


def get_extension(image_url: str) -> str:
    extension: list[str] = ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp']
    for ext in extension:
        if ext in image_url:
            return ext


def download_image(image_url: str, name: str, folder: str = None) -> str:
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f"{folder}/{name}{ext}"
        else:
            image_name: str = f"{name}{ext}"
    else:
        raise Exception('Image Extension Not Found')

    if os.path.exists(image_name):
        raise Exception(f'{image_name} is already Exists')

    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            handler.close()
            print(f'Image Downloaded: {image_name} successfully')
    except Exception as e:
        print(f"Error: {e}")


def main():
    image_url: str = input('Enter the image url: ')
    name: str = input('Enter the image name: ')
    download_image(image_url, name, folder='images')


if __name__ == '__main__':
    main()


# https://gale.udemy.com/course/great-python-projects/learn/lecture/37720358#overview