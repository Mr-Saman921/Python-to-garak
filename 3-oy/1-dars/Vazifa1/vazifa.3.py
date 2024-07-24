import json

name=input("Enter name: ")
cost=int(input("Enter cost: "))
color=input("Enter color: ")
n=int(input("Enter number: "))
try:
  f=open("data.json", "r")
  data=json.load(f)
  data={"name": name, "cost": cost, "color": color, "number": n}
  json.dump(data, f, indent=4)
except FileNotFoundError as error:
  f=open("data.json", "w")
  data={"name":name,"cost":cost,"color":color,"number":n}
  json.dump(data,f,indent=4)
  f.close()
