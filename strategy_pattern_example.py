class FilenameValidator:
    def validate(self, data):
        return data.startswith("data_") and data.endswith(".csv")

class HeaderValidator:
    def validate(self, data):
        return data == ["BatchID", "Value1", "Value2"]

class RowValidator:
    def validate(self, data):
        try:
            values = [float(x) for x in data[1:]]
            return all(0 <= v <= 9.9 for v in values)
        except:
            return False

class Validator:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def validate(self, data):
        return self.strategy.validate(data)

# Example 
validator = Validator(FilenameValidator())
print(validator.validate("data_20250430.csv"))  

validator.set_strategy(HeaderValidator())
print(validator.validate(["BatchID", "Value1", "Value2"]))  

validator.set_strategy(RowValidator())
print(validator.validate(["B001", "5.5", "8.3"]))  

