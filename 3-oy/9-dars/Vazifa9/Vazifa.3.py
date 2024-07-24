import csv


class LoadCsv:
    def __init__(self, filename):
        self.filename = filename

    def reader(self):
        try:
            with open(self.filename, mode='r', encoding='utf-8') as file:
                file = csv.reader(file)
                for line in file:
                    print(line)
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

csv_obj = LoadCsv('user.csv')
csv_obj.reader()
