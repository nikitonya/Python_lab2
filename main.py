from FileReader import FileReader
from Validator import Validator

read = FileReader("C:\\Users\\nikit\\PycharmProjects\\Python_lab2\\27.txt")
data = read.read_file()

valid = Validator(data)

print(data[0])
