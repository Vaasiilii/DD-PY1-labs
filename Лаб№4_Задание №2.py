# TODO импортировать необходимые молули



import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Чтение содержимого CSV файла
    with open(INPUT_FILENAME, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]

    # Сериализация в JSON файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
