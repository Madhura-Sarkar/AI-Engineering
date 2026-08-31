categories = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Spreadsheets": [".csv", ".xlsx"]
}

from pathlib import Path

folder = Path("test_files")

# Create category folders
for category in categories:
    category_folder = folder / category
    category_folder.mkdir(exist_ok=True)

# Organize files
for item in folder.iterdir():

    if item.is_file():

        for category, extensions in categories.items():

            if item.suffix in extensions:

                # print(f"{item.name} → {category}")
                    
                destination = folder / category / item.name
                item.rename(destination) 
                       