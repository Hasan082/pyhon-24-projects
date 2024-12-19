import platform
import requests
import os


def download_chrome():
    """Automate Chrome downloading based on the operating system."""
    system = platform.system().lower()

    if system == "windows":
        print("Chrome not found. Downloading for Windows...")
        chrome_download_url = "https://dl.google.com/chrome/install/latest/chrome_installer.exe"
        installer_path = "chrome_installer.exe"
    elif system == "darwin":  # macOS
        print("Chrome not found. Downloading for macOS...")
        chrome_download_url = "https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg"
        installer_path = "googlechrome.dmg"
    elif system == "linux":
        print("Chrome not found. Downloading for Linux...")
        chrome_download_url = "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
        installer_path = "google-chrome-stable_current_amd64.deb"
    else:
        raise Exception(f"Unsupported operating system: {system}")

    # Download the Chrome installer
    response = requests.get(chrome_download_url)
    with open(installer_path, "wb") as file:
        file.write(response.content)

    print(f"Chrome downloaded. Please install it manually from {installer_path}.")

    # Automate installation for certain OSes if possible
    if system == "windows":
        os.system(installer_path)  # Launch the installer (manual steps required)
    elif system == "darwin":
        print("Please open the DMG file and follow the instructions to install Chrome.")
        os.system(f"open {installer_path}")  # Open the DMG file
    elif system == "linux":
        print("Installing Chrome using dpkg...")
        os.system(f"sudo dpkg -i {installer_path}")
        os.system("sudo apt-get install -f")  # Fix any dependency issues


if __name__ == "__main__":
    download_chrome()
