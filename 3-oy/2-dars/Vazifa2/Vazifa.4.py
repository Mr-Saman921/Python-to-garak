class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name
    def reader(self):
        f=open(self.file_name, "r")
        print(f.read())
filereader=FileReader(file_name="index.txt")
filereader.reader()