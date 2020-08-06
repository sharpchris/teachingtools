from pathlib import Path

def create_page(content):
    filename = "page.html"
    data_folder = Path("refresh_uf_teaching_tools/")
    file_to_write = data_folder / filename
    with open(file_to_write, "w") as index:
        index.write(content)
