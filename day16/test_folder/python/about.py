from pathlib import Path

folders = ["documents", "images", "videos"]

for folder in folders:
    Path(folder).mkdir(exist_ok=True)
    print(f"{folder} folder is ready to use")
    
folder = Path(".")

for item in folder.iterdir():
    

    if item.is_file():
        print(f"{item.name} → File")

    elif item.is_dir():
        print(f"{item.name} → Directory")
    
