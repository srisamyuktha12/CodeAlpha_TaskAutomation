# 📧 Email Extractor — CodeAlpha Task 3

## 📌 About the Project

This project is a Python automation script developed as part of the CodeAlpha Python Programming Internship.

The program reads a text file, automatically identifies email addresses using a regular expression, removes duplicate addresses, and saves the extracted email addresses into a separate output file.

## ✨ Features

* Reads email content from a `.txt` file
* Automatically detects email addresses
* Uses regular expressions for extraction
* Removes duplicate email addresses
* Sorts extracted email addresses
* Saves results to a separate text file
* Handles missing files and other errors

## 🛠️ Technologies Used

* Python
* Regular Expressions (`re`)
* File Handling
* Functions
* Exception Handling

## 📂 Project Structure

```text
CodeAlpha_TaskAutomation/
│
├── email_extractor.py
├── input.txt
├── extracted_emails.txt
└── README.md
```

## ▶️ How to Run

1. Make sure Python is installed.
2. Open this project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python email_extractor.py
```

5. The program reads `input.txt`.
6. It extracts the email addresses.
7. The results are saved in `extracted_emails.txt`.

## 📊 Example

### Input

```text
Contact alice@example.com
Contact bob@gmail.com
Support: support@company.com
```

### Output

```text
alice@example.com
bob@gmail.com
support@company.com
```

## 🎯 Internship Task

This project was completed as **Task 3 — Task Automation with Python Scripts** for the CodeAlpha Python Programming Internship.

The selected automation task is extracting email addresses from a `.txt` file and saving them to another file.

## 👨‍💻 Author

Kanneedi Sri Samyuktha
