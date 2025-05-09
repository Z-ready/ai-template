from src.model import SimpleModel
import torch

def test_model():
    model = SimpleModel()
    input_data = torch.randn(1, 10)
    output = model(input_data)
    assert output.shape == (1, 2)
