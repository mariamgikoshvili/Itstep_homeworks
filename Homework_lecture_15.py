import os, csv

def create_folder(name):
    try:
        os.mkdir(name)
        print(f"Folder {name} created!")
    except FileExistsError as ex:
        print(f"Folder {name} already exists")


def create_file(path, name):
    file_path = f"{path}/{name}.csv"
    try:
        file = open(file_path, 'x', encoding="utf-8")
        file.close
    except FileExistsError as ex:
        print(f"File exists: '{file_path}'")
    return file_path


def read_file(path):
    with open(path, mode='r', encoding='utf-8', newline='') as file:
        reader = list(csv.DictReader(file))
    return reader

def write_file(path,data):
    fields = ["id", "name", "age", "grade", "subject_name", "marks"]
    with open(path, mode='w', encoding='utf-8',newline='') as file:
        writer = csv.DictWriter(file, fieldnames = fields)
        writer.writeheader()
        writer.writerows(data)


create_folder("Test")
filepath = create_file("Test", "file")


'''დაწერეთ პითონის ფუნქცია , სადაც მომხარებელი შეიყვანს ინფომრაციას
 (id,name,age,grade,subject_name,marks) და თქვენ სტუდენტს დაამატებთ csv ფაილში.'''

def input_info(path):
    st_list = read_file(path)
    print(st_list)
    st_id = int(input("Enter Student id: "))
    st_name = input("Enter Student name: ")
    st_age = int(input("Enter Student age: "))
    st_grade = input("Enter Student grade: ")
    sub_name = input("Enter Student subject name: ")
    st_mark = int(input("Enter Student mark: "))
    student_data = {"id" : st_id, "name": st_name, "age" : st_age, "grade" : st_grade, "subject_name" : sub_name, "marks": st_mark}
    st_list.append(student_data)
    write_file(path, st_list)

input_info(filepath)

'''დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, 
როგორც ყველა, ასევე კონკრეტული სტუდენტის ინფომრაციის წაკითხვა ფაილიდან.'''

def info_reader(path):
    info = read_file(path)
    count = 0
    w1 = 10
    w2 = 20
    info_type = input("Please enter id or all: ")
    if info_type == "all":
        for i in info:
            if count == 0:
                header = list(i.keys())
                print(f'{header[0]:<{w1}}{header[1]:<{w1}}{header[2]:<{w1}}{header[3]:<{w1}}{header[4]:<{w2}}{header[5]}')
                print("="*70)
                count += 1
            print(f'{i["id"]:<{w1}}{i["name"]:<{w1}}{i["age"]:<{w1}}{i["grade"]:<{w1}}{i["subject_name"]:<{w2}}{i["marks"]}')
            print("-"*70)
    elif info_type.isdigit():
        for i in info:
            if i["id"] == info_type:
                header = list(i.keys())
                print(f'{header[0]:<{w1}}{header[1]:<{w1}}{header[2]:<{w1}}{header[3]:<{w1}}{header[4]:<{w2}}{header[5]}')
                print("="*70)
                print(f'{i["id"]:<{w1}}{i["name"]:<{w1}}{i["age"]:<{w1}}{i["grade"]:<{w1}}{i["subject_name"]:<{w2}}{i["marks"]}')
                print("-"*70)
    else:
        print("Wrong input, please enter all or valid id")
info_reader(filepath)

'''დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის 
ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის აიდს, საგანს და განახლებულ ქულას.'''

def uptade_info(path):
    info = read_file(path)
    st_id = input("Enter id: ")
    sub_name = input("Enter subject name: ")
    new_mark = int(input("Enter new mark: "))
    for i in info:
        if i["id"] == st_id and i["subject_name"]== sub_name:
            i["marks"] = new_mark
    write_file(path, info)

uptade_info(filepath)