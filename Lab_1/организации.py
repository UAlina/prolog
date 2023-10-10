from random import randint

org = ["Студ. совет", "Волонтерство", "Профсоюз", "КВН"]
for student in range(11301, 11331):
    print('студ_организации({}, "{}").'.format(student, org[randint(0, 3)]))
