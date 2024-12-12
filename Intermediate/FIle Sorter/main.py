# https://gale.udemy.com/course/great-python-projects/learn/lecture/39178218#overview

import os
import shutil


def create_folder(path: str, extension: str):
    """
    :param path:
    :param extension:
    :return: Folder path
    """
    folder_name = extension[1:]
    folder_path = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def sort_files(source_path: str):
    """
    :param source_path:
    :return: None, Move Folder
    """
    for root, dirs, files in os.walk(source_path):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1]

            if extension:
                target_folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, file)

                shutil.move(file_path, target_path)


def remove_unwanted_folder(source_path: str):
    """
    :param source_path:
    :return: None, Remove Unwanted Directory
    """
    for root, dirs, files in os.walk(source_path, topdown=False):
        for subdir in dirs:
            folder_path = os.path.join(root, subdir)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)


def main():
    source_path: str = input("Enter source path: ")
    if os.path.exists(path=source_path):
        sort_files(source_path)
        remove_unwanted_folder(source_path)
        print("File Sorted Successfully")
    else:
        print("Invalid path")


if __name__ == '__main__':
    main()
