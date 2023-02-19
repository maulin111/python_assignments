def oldest_person(people):
    age = [person[1] for person in people]
    age.sort()
    new_list = []
    for i in range(len(people)):
        if age[i] == people[i][1]:
            new_list.append(people[i][0])
    print(("youngest age is", new_list))

p1 = ("smith", 10)
p2 = ("John", 20)
p3 = ("henry", 30)
people = [p1, p2, p3]
oldest_person(people)
