from pathlib import Path

# folder1 = Path("documents")
# folder2 = Path("images")
# folder3 = Path("videos")

# folder1.mkdir(exist_ok=True)
# print("documents folder is ready to use")
# folder2.mkdir(exist_ok=True)
# print("images folder is ready to use")
# folder3.mkdir(exist_ok=True)
# print("videos folder is ready to use")

folders = ["documents", "images", "videos"]

for folder in folders:
    Path(folder).mkdir(exist_ok=True)
    print(f"{folder} folder is ready to use")