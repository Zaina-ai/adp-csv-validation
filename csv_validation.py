import re

def is_valid_filename(filename):
    return re.match(r"^data_\d{8}\.csv$", filename) is not None

def validate_headers(actual, expected):
    return actual == expected

def validate_row_data(row):
    try:
        for value in row[1:]:  
            if value.strip() == "":
                return False
            number = float(value)
            if not (0 <= number <= 9.9):
                return False
        return True
    except:
        return False
