my_dict = {
  "students": [
    {"id": 20, "name": "giorgi", "age": 25},
    {"id": 25, "name": "giorgi", "age": 23},
    {"id": 100, "name": "nika", "age": 22},
    {"id": 56, "name": "nika", "age": 25},
    {"id": 1232, "name": "dato", "age": 22},
    {"id": 846723, "name": "archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}


st_id = []
for student in my_dict.get('students'):
    st_id.append(student.get("id"))

id_list = ', '.join(map(str,st_id))
print(f"Studentebis ID: {id_list}")
id_num = input("airchiet id: ")

id_num_int = int(id_num)
list_num = st_id.index(id_num_int)
student_info = my_dict["students"][list_num]
name = student_info["name"]
ids = student_info["id"]
age = student_info["age"]

print(f'id: {ids}, name: {name}, age: {age}')

for subject in my_dict.get("subjects"):
    sub_name = subject.get("name")
    grade = subject["grades"][id_num]
    print(f'Subject: {sub_name}, grade: {grade} ')

