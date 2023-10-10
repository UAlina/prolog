from random import randint as rand
# rand(3, 5)
# оценка(id_предмета, ст.б, оценка)

# группа = [ст.б_студентов]
gr1 = [11303, 11308, 11311, 11312, 11313] # экон. 1 
gr2 = [11307, 11309, 11314, 11315, 11316] # экон. 2
gr3 = [11305, 11317, 11318, 11319, 11320] # диз. 2
gr4 = [11302, 11321, 11322, 11323, 11324] # диз. 3
gr5 = [11306, 11325, 11326, 11327, 11328] # строй. 2
gr6 = [11301, 11304, 11310, 11329, 11330] # прогр. 2

# предметы_№группы = [id_предметов]
sub_1 = [1, 14, 15, 18]
sub_2 = [2, 3, 16, 17]
sub_3 = [4, 6, 19, 20]
sub_4 = [5, 7, 21]
sub_5 = [8, 9, 10, 22, 23, 24, 25]
sub_6 = [11, 12, 13, 26, 27, 28, 29]

mark = ["a", "b", "c", "d"]

for student in gr1:
    for subject in sub_1:
        print('оценка({}, {}, {}).'.format(subject, student, mark[rand(0, 3)]))

for student in gr2:
    for subject in sub_2:
        print('оценка({}, {}, {}).'.format(subject, student, mark[rand(0, 3)]))
        
for student in gr3:
    for subject in sub_3:
        print('оценка({}, {}, {}).'.format(subject, student, mark[rand(0, 3)]))

for student in gr4:
    for subject in sub_4:
        print('оценка({}, {}, {}).'.format(subject, student, mark[rand(0, 3)]))

for student in gr5:
    for subject in sub_5:
        print('оценка({}, {}, {}).'.format(subject, student, mark[rand(0, 3)]))

for student in gr6:
    for subject in sub_6:
        print('оценка({}, {}, {}).'.format(subject, student, mark[rand(0, 3)]))
