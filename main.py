from FileReader import FileReader
from Validator import Validator


read = FileReader("C:\\Users\\nikit\\PycharmProjects\\Python_lab2\\27.txt")
data = read.read_file()

valid = Validator(data)
valid.parse_valid()
print(valid.parse_invalid())

file = open("C:\\Users\\nikit\\PycharmProjects\\Python_lab2\\output.txt", 'w')
count = 0
for i in valid.parse_valid():
    count += 1
    file.write(str(i) + '\n')

print("Count of valid writes = ", count)



