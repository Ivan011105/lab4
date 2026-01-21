# TODO решите задачу
def task() -> float:
    def task() -> float:
        # Читаем данные из файла
        with open('data.json', 'r') as file:
            data = json.load(file)

        total_sum = 0.0

        # Проходим по каждому элементу в загруженных данных
        for item in data:
            score = item.get("score", 0)  # Получаем значение по ключу "score"
            weight = item.get("weight", 0)  # Получаем значение по ключу "weight"

            # Вычисляем произведение и добавляем к общей сумме
            total_sum += score * weight

        # Возвращаем сумму, округленную до трех знаков после запятой
        return round(total_sum, 3)
print(task())
