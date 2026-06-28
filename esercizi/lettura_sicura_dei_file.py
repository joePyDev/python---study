def read_file_contents(file_path):
    try:
        with open(file_path, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")


read_file_contents("/Users/Example/Documents/my_file.txt")
