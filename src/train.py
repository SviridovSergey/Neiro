from tqdm import tqdm
from src.model import QAModel
import numpy as np

def train_model(data_file, output_file):
    model = QAModel(data_file)
    # Здесь можно добавить логику периодического обучения
    model.save_data(output_file)
    print("Модель успешно обучена и сохранена.")