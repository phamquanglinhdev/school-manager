people = []
person = {
    "name": "Phạm Quang Linh",
    "age": 20,
    "address": "Hà Nội",
}
people.append(person)
people.append(person)

for person in people:
    for key in person.keys():
        print(key, ":", person[key])
    print("====================")
