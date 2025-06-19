from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class SummaryScreen(QWidget):
    # Initialize the summary screen with PostgreSQL path, database status, and folder creation status
    def __init__(self, pg_path, db_status, folder_status):
        super().__init__()
        # Set up the summary screen properties
        self.setWindowTitle("Setup Summary")
        self.setGeometry(400, 300, 500, 300)

        # Set up the UI components
        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"PostgreSQL Path: {pg_path or '❌ Not Found'}"))
        layout.addWidget(QLabel(f"Database Connection: {'✅ Successful' if db_status else '❌ Failed'}"))
        layout.addWidget(QLabel("Folder Creation Summary:"))

        for folder, status in folder_status.items():
            layout.addWidget(QLabel(f"- {folder}: {status}"))

        self.setLayout(layout)
