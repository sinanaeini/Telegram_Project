import json
from src.data import data_dir
def read_json(path=(data_dir / 'result.json')):
    with open(path) as f:
        data = json.load(f)
    return data
def read_file(path=(data_dir / 'stop_word.txt')):
    with open(path) as f:
        file = f.read()
    return file
        