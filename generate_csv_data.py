import csv
import random
import os

def generate_csv_files():
    """Simple CSV test file generator"""
    
    # Create test_data folder if it doesn't exist
    if not os.path.exists('test_data'):
        os.mkdir('test_data')
    
    # Generate 2 valid CSV files
    for i in range(1, 3):
        filename = f"test_data/valid_{i}.csv"
        
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Write header
            writer.writerow(["ID", "Value"])
            
            # Write 5 simple data rows
            for _ in range(5):
                writer.writerow([
                    random.randint(1000, 9999),  # Random ID
                    round(random.random() * 10, 2)  # Random value 0-10
                ])
        print(f"Created valid file: {filename}")
    
    # Generate 2 invalid CSV files
    with open("test_data/invalid_missing_header.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([random.randint(1000, 9999), "no header"])  # No header row
    
    with open("test_data/invalid_bad_data.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Value"])  # Header
        writer.writerow(["text", "not a number"])  # Invalid data row
    
    print("Created invalid test files")

if __name__ == "__main__":
    generate_csv_files()