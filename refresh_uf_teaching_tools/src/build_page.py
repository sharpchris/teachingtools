from pathlib import Path

def create_page(content):
    filename = "index.html"
    data_folder = Path("../docs/")
    file_to_write = data_folder / filename
    with open(file_to_write, "w") as index:
        index.write(content)

    
