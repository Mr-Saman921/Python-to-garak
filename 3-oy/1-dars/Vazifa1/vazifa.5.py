def write_to_file(filename, l):
    with open(filename, 'w') as f:
        for i in l:
            f.write(f"{i}\n")
if __name__ == "__main__":
    l= ["My name is Samandar", 14]
    write_to_file("index.txt", l)
    print("Ma'lumotlar faylga yozildi.")
