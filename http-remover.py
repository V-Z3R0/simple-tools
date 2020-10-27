x = input("input list : ")
y = input("save as : ")
with open((x), "r") as list:
 with open((y), "w") as ress:
  for line in list:
   if "http://" in line:
    ress.write(line.replace('http://',''))
   elif "https://" in line:
    ress.write(line.replace('https://',''))
