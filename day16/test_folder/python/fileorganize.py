from pathlib import Path

file = Path("test.txt")
destination = Path("documents/test.txt")

file.rename(destination)