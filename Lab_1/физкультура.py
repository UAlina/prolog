from random import randint

pe = ["Теннис", "Волейбол", "Футбол", "Баскетбол"]
for student in range(11301, 11331):
    print('физкультура({}, "{}").'.format(student, pe[randint(0, 3)]))
