from pathlib import Path

folder = Path("documents")

# if not folder.exists():
#     folder.mkdir()
#     print("Folder Created")
# else:
#     print("Folder already exists.")

folder.mkdir(exist_ok=True)

print("Documents folder is ready.")