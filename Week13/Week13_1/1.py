with open('C:\Users\user\Desktop\Python\PYTHON_COURSE\Week1\Lesson1.txt', 'r',  encoding = 'ascii') as file:
    text = file.read()
    lines = file.readlines()
    print(text)
    print(lines)
