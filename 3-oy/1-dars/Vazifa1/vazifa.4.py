try:
    f=open("data.json", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")