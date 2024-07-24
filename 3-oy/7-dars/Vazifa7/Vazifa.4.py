import os


class FindFile:

    @staticmethod
    def check_file():
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        file_name = "product_list.docx"
        file_path = os.path.join(downloads_path, file_name)

        return os.path.isfile(file_path)

file_exists = FindFile.check_file()
print(file_exists)
