# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считываем содержимое CSV файла
    with open(INPUT_FILENAME, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Получаем заголовки (первую строку) и данные
        headers = next(reader)

        # Создаем список словарей
        data = []
        for row in reader:
            # Создаем словарь для текущей строки
            entry = {headers[i]: row[i] for i in range(len(headers))}
            data.append(entry)



    # Сериализуем в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
