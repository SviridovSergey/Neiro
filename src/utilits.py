import code
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import logging
import os
'''import numpy as np'''


# Настройка логирования
def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def log_message(message):
    logging.info(message)

def get_path(filename):
    script_dir=os.path.dirname(os.path.abspath(__file__))
    code_dir=os.path.join(script_dir,"src")
    return os.path.join(script_dir,code_dir)