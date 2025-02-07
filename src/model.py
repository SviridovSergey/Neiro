from src.dataset import Dataset
from googletrans import Translator  # Для перевода текста
import numpy as np
import wikipedia
'''import torch
import transformers
import sentence_transformers'''
# src/model.py



# src/model.py


class QAModel:
    def __init__(self, data_file):
        self.dataset = Dataset(data_file)
        self.translator = Translator()  # Инициализация переводчика

    def answer_question(self, question):
        # Проверяем, есть ли вопрос в базе
        answer = self.dataset.get_answer(question)
        if answer:
            return answer

        # Если нет, пытаемся найти ответ на Wikipedia
        return self.generate_answer(question)

    def generate_answer(self, question):
        try:
            # Простая логика генерации ответа для известных запросов
            if "создать папку" in question.lower():
                return "Для создания папки используйте: os.makedirs('название_папки')"
            elif "открыть файл" in question.lower():
                return "Для открытия файла используйте: open('путь_к_файлу', 'r')"

            print("Не знаю ответ на этот вопрос. Сейчас попробую найти его на Wikipedia...")

            # Ищем ответ на Wikipedia
            wiki_answer = wikipedia.summary(question, sentences=2)  # Берем первые 2 предложения

            # Сохраняем новый вопрос в quests.txt
            self.save_new_question(question)

            return f"Вот что я нашел на Wikipedia:\n{wiki_answer}"
        except wikipedia.exceptions.PageError:
            return "Не удалось найти информацию на Wikipedia."
        except wikipedia.exceptions.DisambiguationError:
            return "Найдено несколько вариантов. Пожалуйста, уточните свой вопрос."
        except Exception as e:
            return f"Произошла ошибка при поиске: {str(e)}"

    def save_new_question(self, question):
        with open("data/quests.txt", "a", encoding="utf-8") as f:
            f.write(f"{question}\n")
        print(f"Новый вопрос '{question}' сохранен в quests.txt")

    def add_new_question(self, question, answer):
        self.dataset.questions[question] = answer

    def save_data(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            for q, a in self.dataset.questions.items():
                f.write(f"{q}|{a}\n")