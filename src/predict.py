import torch
from model import SimpleModel

def predict(input_data):
    model = SimpleModel()
    # 推理代码
    return model(input_data)

if __name__ == "__main__":
    sample_input = torch.randn(1, 10)
    print(predict(sample_input))
