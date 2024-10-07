import json

def save(path: str) -> dict:
	with open(path, 'r') as file:
		data = json.load(file)
	return data

def load(data: dict, path: str) -> None:
	with open(path, 'w') as file:
		json.dump(data, file)
  
  
  
if __name__ == '__main__':
    # 