import os

print("Hello system!")

file_name = "./src/assets/a.txt"

with open(file_name, 'r') as f:
    content = f.read()
  
print(content)


input("Enter any key to continue...")