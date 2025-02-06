from src.model import QAModel   
from src.utilits import setup_logging, log_message
from src.utilits import get_path
import sys

if __name__ == "__main__":
    a=sys.path.append(get_path("src"))  # Добавляем текущую директорию в путь поиска модулей
    print(a)
    setup_logging("logs/training.log")

    # Инициализация модели
    model = QAModel("data/initial_qa.txt")

    print("Добро пожаловать в систему вопросов и ответов!")
    while True:
        user_input = input("Задайте вопрос (или напишите 'выход' для завершения): ")
        if user_input.lower() == "выход":
            break

        answer = model.answer_question(user_input)
        print(f"Ответ: {answer}")

        if answer == "Не знаю ответ на этот вопрос.":
            correct_answer = input("Введите правильный ответ: ")
            model.add_new_question(user_input, correct_answer)
            model.save_data("data/updated_qa.txt")
            log_message(f"Новый вопрос добавлен: {user_input} -> {correct_answer}")

    print("Программа завершена.")