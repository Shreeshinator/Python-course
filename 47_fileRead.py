# python read file program
path = "output.txt"

try:
    with open(file = path, mode = "r") as file:
        content = file.read()
        print(f"Content of '{path}':\n{content}")

except FileNotFoundError:
    print(f"Error: The file '{path}' was not found.")
except Exception as e:
    print(f"Error: {e}") 