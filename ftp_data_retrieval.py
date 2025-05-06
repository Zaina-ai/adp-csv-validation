import ftplib 
import os
import json

FTP_SERVER = 'ftp.example.com'
FTP_USER = 'username'
FTP_PASSWORD = 'password'
FTP_DIRECTORY = '/csvfiles/'
LOCAL_DOWNLOAD_DIR = 'downloads/'
TRACKING_FILE = 'processed_files.json'

os.makedirs(LOCAL_DOWNLOAD_DIR, exist_ok=True)

# Initialize tracking file if it doesn't exist
if not os.path.exists(TRACKING_FILE):
    with open(TRACKING_FILE, "w") as f:
        json.dump([], f)

def load_processed_files():
    with open(TRACKING_FILE, 'r') as f:
        return json.load(f)

def save_processed_file(filename):
    processed = load_processed_files()
    processed.append(filename)
    with open(TRACKING_FILE, 'w') as f: 
        json.dump(processed, f)

def download_new_files():
    try:
        files = [
            'MED_DATA_20250425120000.csv',
            'MED_DATA_20250425130000.csv',
            'MED_DATA_20250425140000.csv'
        ]
        processed_files = load_processed_files()

        for file in files:
            if file not in processed_files: 
                print(f"Downloading new file: {file}")
                with open(os.path.join(LOCAL_DOWNLOAD_DIR, file), 'w') as f:
                    f.write('Simulated file content')
                save_processed_file(file)
            else: 
                print(f"Skipping already processed file: {file}")

    except Exception as e: 
        print(f"FTP connection failed: {e}")

if __name__ == "__main__":
    download_new_files()


