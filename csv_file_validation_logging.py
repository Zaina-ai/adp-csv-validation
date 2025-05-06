import csv
import os
import uuid

def validate_csv(filepath):
    print(f"Validating file: {filepath}")
    errors = []
    batch_ids = set()

    try:
        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            expected_columns = ['BatchID', 'Date', 'PatientID', 'Score', 'Diagnosis']
            if reader.fieldnames != expected_columns:
                errors.append("Header mismatch: Expected " + ", ".join(expected_columns))

            for row_num, row in enumerate(reader, 2):
                if any(not val.strip() for val in row.values()):
                    errors.append(f"Row {row_num}: Missing values")
                try:
                    score = float(row['Score'])
                    if not (0.0 <= score <= 9.9):
                        errors.append(f"Row {row_num}: Score out of valid range (0–9.9)")
                except ValueError:
                    errors.append(f"Row {row_num}: Invalid score format")

                batch_id = row['BatchID']
                if batch_id in batch_ids:
                    errors.append(f"Row {row_num}: Duplicate BatchID: {batch_id}")
                else:
                    batch_ids.add(batch_id)

    except Exception as e:
        errors.append(f"File read error: {e}")

    if errors:
        log_errors(filepath, errors)
        print(f"{len(errors)} error(s) found — logged.")
    else:
        print("No errors found. File is valid.")

def log_errors(filename, error_list):
    guid = str(uuid.uuid4())
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", f"{guid}_error.log")
    with open(log_path, 'w') as f:
        f.write(f"Validation errors for file: {filename}\n\n")
        for error in error_list:
            f.write(error + "\n")
    print(f"Error log created: {log_path}")

if __name__ == "__main__":
    test_file = "C:\\Users\\ahmad\\OneDrive\\Desktop\\ADP Assignment-Zaina\\csv_test_file.txt"
    validate_csv(test_file)
