from random import randint

hobbies = ["Рисование", "Пение", "Рукоделие", "Спорт", "Сон"]
for student in range(11301, 11331):
    print('хобби({}, "{}").'.format(student, hobbies[randint(0, 4)]))
