from pathlib import Path

folder = Path(".")

for file in folder.glob("*.py"):
    print(file.name)
    

for file in folder.glob("*practice*.py"):
    print(file.name)
    
