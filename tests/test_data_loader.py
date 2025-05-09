from src.data_loader import load_data

def test_load_data():
    data = load_data('data/train/data.csv')
    assert data is not None
    assert len(data) > 0
