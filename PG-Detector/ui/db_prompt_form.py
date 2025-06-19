from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QPushButton,
    QVBoxLayout, QFormLayout, QMessageBox
)
from utils.db_connector import try_db_connection
from utils.folder_creator import create_data_folders
from ui.summary_screen import SummaryScreen
from utils.postgres_checker import find_postgres

# Define the DBPromptForm class for database connection input
class DBPromptForm(QWidget):
    # Initialize the DBPromptForm
    def __init__(self):
        super().__init__() # Initialize the QWidget
        # Set up the form properties
        self.setWindowTitle("Database Connection")
        self.setGeometry(350, 350, 400, 300)
        self.setup_ui()

    # Set up the UI components
    def setup_ui(self): 
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Create input fields for database connection details
        self.host_input = QLineEdit("localhost")
        self.port_input = QLineEdit("5432")
        self.db_input = QLineEdit()
        self.user_input = QLineEdit()
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)

        # Add labels and input fields to the form layout
        form_layout.addRow("Host:", self.host_input)
        form_layout.addRow("Port:", self.port_input)
        form_layout.addRow("Database:", self.db_input)
        form_layout.addRow("Username:", self.user_input)
        form_layout.addRow("Password:", self.pass_input)

        layout.addLayout(form_layout)

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.attempt_connection)
        layout.addWidget(self.connect_button)

        self.setLayout(layout)

    # Attempt to connect to the database with provided credentials
    def attempt_connection(self): 
        creds = {
            "host": self.host_input.text(),
            "port": self.port_input.text(),
            "dbname": self.db_input.text(),
            "user": self.user_input.text(),
            "password": self.pass_input.text(),
        }

        success = try_db_connection(creds)

        if success:
            QMessageBox.information(self, "Success", "Connected to database.")
            base, results = create_data_folders()
            self.show_summary(results)
        else:
            QMessageBox.warning(self, "Failed", "Connection failed. Please check details.")

    # Show the summary screen after successful connection and folder creation
    def show_summary(self, folder_status):
        pg_path = find_postgres()
        db_status = True  # since success already confirmed
        self.summary = SummaryScreen(pg_path, db_status, folder_status)
        self.summary.show()
        self.close()










