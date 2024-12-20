# File Sorting Tool

A Python script to organize files in a specified folder by their file extensions. The script creates separate folders for each file type (based on extension) and moves files into their respective folders. Additionally, it cleans up empty directories after sorting.

---

## Features
- Automatically creates folders for different file types.
- Moves files into folders based on their extensions.
- Removes any empty folders after sorting.
- Simple and user-friendly.

---

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of how to run Python scripts.

---

## How to Use

1. **Clone or Download the Repository**:
   Download the script or clone the repository to your local machine.

2. **Run the Script**:
   Open a terminal or command prompt and navigate to the script's directory.

   ```bash
   python file_sorting_tool.py
   ```

3. **Provide the Source Path**:
   Enter the path to the folder containing the files you want to organize when prompted.

4. **Watch the Magic Happen**:
   The script will:
   - Create folders for each file type.
   - Move files into the appropriate folders.
   - Remove empty folders after sorting.

---

## Example

Suppose you have the following files in a folder `/Users/YourName/Downloads`:
```
document.pdf
image.jpg
script.py
notes.txt
```

After running the script with `/Users/YourName/Downloads` as the source path, the folder structure will look like this:
```
Downloads/
├── pdf/
│   └── document.pdf
├── jpg/
│   └── image.jpg
├── py/
│   └── script.py
├── txt/
│   └── notes.txt
```

Empty folders (if any) will be removed automatically.

---

## Code Explanation

### Functions

1. **`create_folder(path: str, extension: str)`**:
   - Creates a folder based on the file extension (e.g., `.pdf` → `pdf/`).
   - Returns the folder path.

2. **`sort_files(source_path: str)`**:
   - Walks through the source folder and organizes files by their extensions.
   - Moves files into their respective folders.

3. **`remove_unwanted_folder(source_path: str)`**:
   - Removes empty folders in the source path.

4. **`main()`**:
   - Entry point of the script.
   - Takes user input for the source path and calls the necessary functions.

---

## Error Handling
- If the specified path does not exist, the script will print: `Invalid path`.
- Handles missing extensions and skips files without extensions.

---

## Limitations
- Does not handle files with multiple extensions (e.g., `.tar.gz`).
- Files with no extensions are ignored.

---

## Contributing
If you would like to contribute to this script, feel free to fork the repository and create a pull request.

---

## License
This project is licensed under the MIT License.
