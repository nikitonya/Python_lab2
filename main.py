from FileReader import FileReader
from Validator import Validator
import argparse

parser = argparse.ArgumentParser(description="Validation")
parser.add_argument('-input', default='27.txt')
parser.add_argument('-outputhe', default='output.txt')
args = parser.parse_args()

inputPath = args.input
outputPath = args.outputhe

read = FileReader(inputPath)
data = read.read_file()

valid = Validator(data)
valid.parse_valid()
print(valid.parse_invalid())

file = open(outputPath, 'w')
count = 0
for i in valid.parse_valid():
    count += 1
    file.write(str(i) + '\n')

print("Count of valid writes = ", count)



