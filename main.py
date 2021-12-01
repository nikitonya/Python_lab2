from FileReader import FileReader
from Validator import Validator
import argparse
import json

parser = argparse.ArgumentParser(description="Validation")
parser.add_argument('-input', default='27.txt')
parser.add_argument('-outputhe', default='output.txt')
args = parser.parse_args()

inputPath = args.input
outputPath = args.outputhe

read = FileReader(inputPath)
data = read.read_file()

valid = Validator(data)

file = open(outputPath, 'w')

json.dump(
            valid.parse_valid(),
            open(
                outputPath,
                "w",
                encoding="windows-1251"),
            indent=5,
            ensure_ascii=False,
)

print("Число невалидных записей по типам ошибок:\n", valid.parse_invalid())



