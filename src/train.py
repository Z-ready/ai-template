import torch
from model import SimpleModel
from data_loader import load_data

def train():
    data = load_data('data/train/data.csv')
    model = SimpleModel()
    # 训练代码
    print("Training the model...")

if __name__ == "__main__":
    train()
