# s=15
# x=0
# try:
#     print(s/x)
# except:
#     print("Error")

# s=15
# x=2
# try:
#     r=s/x
# except ZeroDivisionError as error:
#     r=0
#     print(error)
# else:
#     print(r)
# finally:
#     print("Finally")

# try:
#     f=open("test.json","r")
# except FileNotFoundError as error:
#     print(error)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("Finally")

# try:
#   f=open("test.json","r")
# except FileNotFoundError as error:
#   print(error)
# else:
#   print(f.read())
#   f.close()
# finally:
#   print("Finally")

# # try except dan xatolik olishimiz mumkin bo'lganda foydalanamiz.
# # try ga xato bo'lishi mumkin bo'lgan kodni yozamiz.
# # except kodlar xato bo'lsa dasturga xos javob chiqaradi.

# import json
# def add_user(name:str, surname:str) -> None:
#   try:
#     f=open("data.json","r")
#     data=json.load(f)
#     print("File exists")
#     data.append({"name":name, "surname":surname})
#     json.dump(data, f, indent=4)
#   except FileNotFoundError as error:
#     print(error)
#     f=open("data.json","w")
#     data=[{"name":name, "surname":surname}]
#     json.dump(data, f, indent=4)
# if __name__=="__main__":
#   name=input("Enter a name: ")
#   surname=input("Enter a surname: ")
#   add_user(name, surname)