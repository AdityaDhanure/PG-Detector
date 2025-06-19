import os
import shutil

def find_postgres():
    # Try checking PATH
    psql_path = shutil.which("psql")
    if psql_path:
        return psql_path

    # Try common Windows install paths
    common_paths = [
        r"C:\Program Files\PostgreSQL\17\bin\psql.exe",
        r"C:\Program Files\PostgreSQL\16\bin\psql.exe",
        r"C:\Program Files\PostgreSQL\15\bin\psql.exe",
        r"C:\Program Files\PostgreSQL\14\bin\psql.exe",
        r"C:\Program Files\PostgreSQL\13\bin\psql.exe",
    ]

    for path in common_paths:
        if os.path.exists(path):
            return path

    return None
