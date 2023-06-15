def count_variables(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    variable_count = 0
    lines = content.split("\n")

    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            continue

        words = line.split()

        for word in words:
            if word.isidentifier() and not word.isdigit():
                variable_count += 1

    return variable_count


file_path = r'C:\Users\user\Desktop\Python\PYTHON_COURSE\Week12\Week12_3\TicTacToe.py'
variable_count = count_variables(file_path)
print(f"The number of variables in the file is: {variable_count}")
