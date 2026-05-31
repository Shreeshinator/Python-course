def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

op_result = add(1, 2, 3)  # takes any number of positional arguments 
print(op_result)

def display_name(*args):
    fullname = ""
    for name in args:
        fullname += name + " "
    return fullname.strip()
result = display_name("Shreesh", "Raj", "Tripathi")  # takes any number of positional arguments and concatenates them
print(result)

#----------Kwargs----------
def display_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += f"{key}: {value}\n"
    return info.strip()

result_info = display_info(Name="Shreesh", Age=25, City="New York")  # takes any number and any type of keyword arguments and formats them
print(result_info)