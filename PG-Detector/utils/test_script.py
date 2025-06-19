from PyQt5.QtWidgets import QApplication
import sys
from utils.postgres_checker import find_postgres
from utils.db_connector import try_db_connection
from utils.folder_creator import create_data_folders

def run_tests():
    print("📦 Running Test Script with Bonus Features...\n")

    print("🔍 Checking PostgreSQL installation...")
    pg_path = find_postgres()
    if pg_path:
        print(f"✅ PostgreSQL found at: {pg_path}")
    else:
        print("❌ PostgreSQL not found.")
        return

    print("\n🔐 Testing database connection...")
    creds = {
        "host": input("Enter DB host (default: localhost): ") or "localhost",
        "port": input("Enter port (default: 5432): ") or "5432",
        "dbname": input("Enter DB name: "),
        "user": input("Enter DB username: "),
        "password": input("Enter password: ")
    }

    connected = try_db_connection(creds)
    print("✅ Database connection successful!" if connected else "❌ Connection failed.")

    print("\n📂 Creating folders (choose a directory from dialog)...")

    app = QApplication(sys.argv)  # ✅ Required before using QFileDialog
    base_dir, folder_results = create_data_folders()
    app.exit()  # ✅ Exit right after dialog
    del app     # ✅ Ensure full cleanup

    if base_dir is None:
        print("❌ Folder setup cancelled by user.")
        return

    print(f"\n📁 Base directory selected: {base_dir}")
    print("🧾 Folder creation summary:")
    for folder, result in folder_results.items():
        print(f" - {folder}: {result}")

if __name__ == "__main__":
    run_tests()
