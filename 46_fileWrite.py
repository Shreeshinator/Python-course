txt = "Hello, World!\r\n"

path = "output.txt"

with open(file = path,mode = "a") as file:
    file.write(txt)
    print(f"The text has been written to '{path}'.")