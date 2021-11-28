from FileReader import FileReader
from Validator import Validator
import json

read = FileReader("C:\\Users\\nikit\\PycharmProjects\\Python_lab2\\27.txt")
data = read.read_file()

valid = Validator(data)
valid.parse_valid()

file = open("C:\\Users\\nikit\\PycharmProjects\\Python_lab2\\output.txt", 'w')
for i in valid.parse_valid():
    file.write(str(i) + '\n')




