import os
class FileRenamer:
    def __init__(self, directory, old_filename, new_filename):
        self.directory = directory
        self.old_filename = old_filename
        self.new_filename = new_filename

    def rename_file(self):
        old_file_path = os.path.join(self.directory, self.old_filename)
        new_file_path = os.path.join(self.directory, self.new_filename)

        try:
            os.rename(old_file_path, new_file_path)
            print(f"'{old_file_path}' fayli '{new_file_path}' ga o'zgartirildi.")
        except FileNotFoundError:
            print(f"{old_file_path} fayli topilmadi.")
        except Exception as e:
            print(f"Fayl nomini o'zgartirishda xatolik yuz berdi: {e}")

renamer = FileRenamer(r"C:\Users\ПОЛЬЗОВАТЕЛЬ\Desktop\Python to'garak\3-oy\10-dars\Vazifa10", 'file', 'n_file')
renamer.rename_file()
