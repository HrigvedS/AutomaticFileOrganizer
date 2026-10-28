# 📁 Automatic File Organizer using Python

## 📌 Project Description

The **Automatic File Organizer** is a Python-based utility that automatically organizes files into separate folders based on their file extensions.

Instead of manually sorting files, this program scans a specified directory, identifies file types, creates category folders, and moves files into their respective folders. Unsupported file types are moved into an `Other` folder.

This project demonstrates the practical use of Python for file handling, directory management, loops, conditional statements, functions, and exception handling.

## ✨ Features

- Automatically organizes files based on their extensions.
- Creates category folders if they do not already exist.
- Supports multiple file formats.
- Moves unsupported file types into an `Other` folder.
- Skips directories during file processing.
- Checks whether the specified directory exists.
- Handles empty folders and invalid paths.
- Avoids overwriting files when a file with the same name already exists in the destination.
- Provides console messages to track file movements and execution status.

## 🗂️ Supported File Types

| Category | Supported Extensions |
|---|---|
| Image | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| Text | `.txt` |
| PDF | `.pdf` |
| Document | `.doc`, `.docx` |
| Excel | `.xls`, `.xlsx`, `.csv` |
| Video | `.mp4`, `.mkv`, `.avi` |
| Audio | `.mp3`, `.wav` |
| Other | All unsupported file types |

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Modules:** `os`, `shutil`, `sys`
- **Concepts:** Functions, loops, conditional statements, dictionaries, file handling, directory management, and exception handling.

## 📋 Prerequisites

Before running this project, ensure that you have:

1. Python installed on your computer.
2. A code editor such as Visual Studio Code (optional).
3. A folder containing files that you want to organize.
4. Access to a terminal or command prompt.

No external Python packages are required because the program uses built-in Python modules.

## ⚙️ Installation and Execution

### Step 1: Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

During installation on Windows, select **Add Python to PATH**.

To verify the installation, open Command Prompt or a terminal and run:

```bash
python --version
```

If that command does not work on Windows, try:

```bash
py --version
```

You should see the installed Python version.

### Step 2: Download or Clone the Repository

If the project is hosted on GitHub, open its repository and download the ZIP file, then extract it.

Alternatively, clone the repository using Git:

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

Navigate to the project directory:

```bash
cd YOUR_PROJECT_FOLDER
```

### Step 3: Create the Python File

If the project does not already contain the Python script, create a file named:

```text
file_organizer.py
```

Paste the complete Automatic File Organizer Python code into this file and save it.

### Step 4: Prepare a Test Folder

Create a separate folder for testing. For example:

```text
C:\Users\YourUsername\Desktop\Project testing
```

Place some sample files inside it, such as:

- `sample.pdf`
- `notes.txt`
- `report.docx`
- `photo.jpg`
- `song.mp3`
- `archive.zip`

**Important:** Use a test folder or a backup of your files because the program moves files from their original locations.

### Step 5: Run the Program

Open a terminal in the directory containing `file_organizer.py`.

Execute the following command:

```bash
python file_organizer.py
```

On Windows, you can also use:

```bash
py file_organizer.py
```

### Step 6: Enter the Folder Path

When prompted, enter the complete path of the folder containing the files you want to organize.

Example:

```text
Enter folder path or type Exit to quit:
```

Enter:

```text
C:\Users\YourUsername\Desktop\Project testing
```

Replace `YourUsername` with your actual Windows username.

Press Enter to start organizing the files.

### Step 7: Verify the Results

After execution, the program creates folders based on the file extensions and moves the corresponding files into them.

For example, the original folder:

```text
Project testing/
├── sample.pdf
├── notes.txt
├── report.docx
├── photo.jpg
├── song.mp3
└── archive.zip
```

After execution:

```text
Project testing/
├── PDF/
│   └── sample.pdf
├── Text/
│   └── notes.txt
├── Document/
│   └── report.docx
├── Image/
│   └── photo.jpg
├── Audio/
│   └── song.mp3
└── Other/
    └── archive.zip
```

Your console will display messages indicating which files were moved and when the organization process is complete.

### Step 8: Exit the Program

After the organization process finishes, the program prompts you for another folder path.

To close the program, enter:

```text
Exit
```

The program will terminate.

## 🧪 Testing Scenarios

The following scenarios can be used to verify the program's functionality:

| Test Scenario | Expected Result |
|---|---|
| Enter a valid folder path | The program processes the folder. |
| Enter an invalid folder path | An error message is displayed. |
| Enter an empty folder | The program reports that there are no files to organize. |
| Provide files with supported extensions | Files are moved into their respective category folders. |
| Provide unsupported file types | Files are moved into the `Other` folder. |
| Run the program when category folders already exist | Existing folders are reused. |
| Encounter a duplicate filename in the destination | The existing destination file is preserved, and the duplicate is skipped. |
| Enter `Exit` | The program terminates. |

## 🔍 How It Works

1. The program accepts a directory path from the user.
2. It validates the path and checks whether the directory contains files.
3. It scans the directory using `os.listdir()`.
4. It skips subdirectories and examines the extensions of files.
5. It identifies the category for each supported file type.
6. It creates the required destination folder using `os.makedirs()`.
7. It moves files using `shutil.move()`.
8. It places unsupported files into the `Other` folder.
9. It displays messages describing the results.

## 🚀 Future Enhancements

Potential improvements include:

- Add support for more file extensions.
- Provide a preview or dry-run mode before moving files.
- Allow users to select categories interactively.
- Add logging to a separate log file.
- Support recursive organization of subdirectories.
- Add a graphical user interface (GUI).
- Provide configurable duplicate-file handling options.

## 🎯 Learning Outcomes

Through this project, I practiced:

- Working with files and directories in Python.
- Using built-in modules such as `os`, `shutil`, and `sys`.
- Creating and calling reusable functions.
- Applying loops, dictionaries, and conditional statements.
- Handling invalid paths and runtime exceptions.
- Building a practical automation utility to solve a real-world problem.

## 👨‍💻 Author

**Hrigved Sharma**

This project was developed as part of my Python learning journey to strengthen my programming fundamentals and practical automation skills.
