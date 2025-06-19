from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
from utils.postgres_checker import find_postgres
from ui.db_prompt_form import DBPromptForm

# Main application window for PostgreSQL detection
class MainWindow(QWidget):
    # Initialize the main window
    def __init__(self): 
        super().__init__() # Initialize the QWidget
        # Set up the main window properties
        self.setWindowTitle("PostgreSQL Detector")
        self.setGeometry(300, 300, 400, 200)
        self.setup_ui()

    # Set up the UI components
    def setup_ui(self): 
        layout = QVBoxLayout()

        self.label = QLabel("Click to check for PostgreSQL installation.")
        layout.addWidget(self.label)

        self.check_button = QPushButton("Check PostgreSQL")
        self.check_button.clicked.connect(self.check_postgres)
        layout.addWidget(self.check_button)

        self.setLayout(layout)

    # Check for PostgreSQL installation
    def check_postgres(self): 
        path = find_postgres()
        if path:
            QMessageBox.information(self, "PostgreSQL Found", f"PostgreSQL found at:\n{path}")
            self.goto_db_form()
        else:
            QMessageBox.critical(self, "Not Found", "PostgreSQL not found on this system.")

    # Navigate to the database connection form
    def goto_db_form(self): 
        self.db_form = DBPromptForm()
        self.db_form.show()
        self.close()
