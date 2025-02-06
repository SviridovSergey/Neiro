from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
'''import numpy as np
import pandas as pd
import nltk
import sklearn'''
import os

class Dataset:
    def __init__(self, file_path):
        self.questions = {}
        self.load_data(file_path)

    def load_data(self, file_path):
        if not os.path.exists(file_path):
            print(f"Файл {file_path} не найден!")
            return
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                q, a = line.strip().split('|')
                self.questions[q] = a

    def get_questions(self):
        return list(self.questions.keys())

    def get_answer(self, question):
        return self.questions.get(question, None)