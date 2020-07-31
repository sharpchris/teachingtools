def create_page(content):
    filename = "myfile.html"
    with open(filename, "w") as index:
        index.write(content)
