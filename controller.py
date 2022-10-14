import database
import django


def inputSize():
    try:
        size = int(input("Nhập vào số người:"))
        return size
    except:
        inputSize()


def makePerson():
    from model import Person
    person = Person()
    person.input()
    return person


def printData(table):
    for row in table:
        row.output()
        print("=========================")


def sortByAge():
    from database import people

    for index in range(0, len(people) - 1):
        for sub in range(1, len(people)):
            if people[sub].getAge() < people[index].getAge():
                temp = people[index]
                people[index] = people[sub]
                people[sub] = temp
    printData(people)


def process():
    import database
    for index in range(0, inputSize()):
        database.addPerson(makePerson())
    sortByAge()
    # printData(database.people)
