from random import randint

lang = ["Английский", "Немецкий", "Французский"]
for student in range(11301, 11331):
    print('иностранный_язык({}, "{}").'.format(student, lang[randint(0, 2)]))
