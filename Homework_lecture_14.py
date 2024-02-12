import json
chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

'''1.	დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით 
პარამეტრად მიიღებს ფაილის მისამართს, სახელს და შემქნის მას.'''

def create_file(path, name):
    filepath = f"{path}/{name}.json"

    try:
        file = open(filepath, mode = "x", encoding="utf-8")
        file.close
    except FileExistsError as ex:
        print(f"File exists: '{filepath}'")
    
    return filepath

Filepath = create_file("/users/mac/desktop/test", "test")

def write_file(path,data):  
    with open(path, mode='w', encoding='utf-8') as fout:
        fout.write(json.dumps(data))

write_file(Filepath,chess_players)

'''2.	დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს'''

def read_file(path):
  with open(path, mode='r', encoding='utf-8') as fin:
    return json.loads(fin.read())

'''3.	დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს'''

def uptade_file(path,data):
    data1 = read_file(path)
    print(data1)
    data1.append(data)
    print(data1)
    write_file(path,data1)


'''4.	დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict)
 და ჩაწერს/გაანახლებს ფაილის კონტენტს. ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია'''

new_data = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]
def add_data(path,data):
    for i in data:
        uptade_file(path, i)
    return data
    
add_data(Filepath,new_data)    