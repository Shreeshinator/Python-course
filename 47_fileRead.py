# python read file program
path = "output.txt"

with open(file = path, mode = "r") as file:
    content = file.read()
    print(f"Content of '{path}':\n{content}")