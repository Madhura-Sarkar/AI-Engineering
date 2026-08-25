import os

print(os.getcwd())
print(os.listdir())

# os.mkdir("test_folder")
print(os.path.exists("test_folder"))

print(os.path.isfile("main.py"))
print(os.path.isdir("test_folder"))