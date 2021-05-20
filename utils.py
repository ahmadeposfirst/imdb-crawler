import json

def write(data):
    file = 'movie_list.json'

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(" "*70, end='\r', flush=True)
    print(f"{len(data)} records saved to file {file}")


def read():
    try:
        with open('movie_list.json', encoding='utf-8') as file:
            movie_list = json.load(file)
        return movie_list
    except Exception as e:
        print(f"Unable to read from json: {e.__str__()}")


def return_ele(x, i):
    if len(x) > i: 
        return x[i]
    else:
        return 0