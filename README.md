
# PyQt5-Based PostgreSQL Detection & Data Folder Setup Utility

This is a Windows desktop utility built using PyQt5 and Python. 
The purpose of this tool is to help users detect whether PostgreSQL is installed on their system, verify database connection credentials, and automatically organize data files by type (CSV, JSON, images, ZIPs) into appropriate folders — all through a simple graphical user interface.

## Features

- Detects PostgreSQL installation (searches PATH and common directories)
- Displays the PostgreSQL path if found; shows an error if not
- Prompts user for PostgreSQL database credentials via PyQt5 form
- Attempts to connect to the database and notifies success/failure
- Upon success, creates data folders:
  - csv_files
  - json_files
  - image_files
  - bundles
- Bonus Features:
  - Lets the user choose where folders will be created (via folder dialog)
  - Displays a summary screen showing results of all operations

## Technologies Used

- Python 3.12
- PyQt5
- psycopg2 (PostgreSQL client for Python)
- Windows OS

## How to Run

1. Clone or download the project folder.
```bash
git clone https://github.com/AdityaDhanure/PG-Detector.git
```
2. Open a terminal or command prompt and navigate to the project directory.
3. (Optional but recommended) Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```
4. Install the required packages:
```bash
pip install PyQt5 psycopg2
```
5. Run the application:
```bash
python main.py
```

## Project Structure

```
biopan_pg_detector/
├── main.py                       # Main launcher
├── ui/
│   ├── main_window.py            # UI for PostgreSQL detection
│   ├── db_prompt_form.py         # UI for DB credentials entry
│   └── summary_screen.py         # Optional summary screen
├── utils/
│   ├── postgres_checker.py       # Checks if PostgreSQL is installed
│   ├── db_connector.py           # Tries DB connection with credentials
│   ├── folder_creator.py         # Creates the required data folders
|   ├── test_script.py            # CLI-based testing tool
|   └── design_notes.txt          # 1–2 page writeup on decisions + learning
│ 
└── README.md                     # This file
```

## Testing the Utility

To run a terminal-based test simulation of the project (bonus-supported):
```bash
python -m utils.test_script
```
This script will:
- Check for PostgreSQL
- Prompt for database credentials
- Ask for a folder location using a GUI file dialog
- Print out status of folder creation and DB connection

## Known Limitations

- Only tested and supported on Windows OS.
- Assumes psycopg2 works with local PostgreSQL or network-accessible DB.
- Passwords are entered in plain input (not masked in the test script).
- No logging or persistence implemented.

## License

This utility is built solely for learning and evaluation purposes as part of an internship assignment.
