#File Not Found

def read_file():
    try:
        with open("data.txt", "r") as file:
            print("File contents:")
            print(file.read())
    except FileNotFoundError:
        print("File not found, please check the filename!")
        
read_file()
