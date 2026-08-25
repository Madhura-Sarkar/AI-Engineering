import os

print(os.getcwd())

print(os.listdir())

print(os.path.exists("main.py"))

print(os.path.exists("practice"))

print(os.path.isfile("main.py"))
print(os.path.isdir("main.py"))

print(os.path.isfile("practice"))
print(os.path.isdir("practice"))

# os.mkdir("practice")

# print(os.path.exists("practice"))
# print(os.path.isdir("practice"))

if not os.path.exists("practice"):
    os.mkdir("practice")
    print("Practice folder created.")
else:
    print("Practice folder already exists.")
    
from pathlib import Path

path = Path("main.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())

path1 = Path("practice")
print(path1.exists())
print(path1.is_dir())
print(path1.name)