import os
from PyQt5.QtWidgets import QFileDialog
from pathlib import Path

def create_data_folders():
    results = {}  # to store status of each folder
    base_dir = QFileDialog.getExistingDirectory(
        None, "Select Base Directory", str(Path.home() / "Documents")
    )

    if not base_dir:
        return None, {"error": "No directory selected."}

    folder_names = ["csv_files", "image_files", "json_files", "bundles"]

    for folder in folder_names:
        path = os.path.join(base_dir, folder) # Construct full path
        try:
            os.makedirs(path, exist_ok=True) # Create folder if it doesn't exist
            results[folder] = f"✅ Created at {path}"
        except Exception as e:
            results[folder] = f"❌ Failed: {e}"

    return base_dir, results
