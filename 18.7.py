import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']

students.sort()

classes = ['Математика', 'Русский язык', 'Информатика']

students_marks = {}

for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1,5) for i in range(3)]
        students_marks[student][class_] = marks

print('Студенты и их оценки по каждому предмету: ')
for student in students:
    print(f'{student} {students_marks[student]}')

print('''Список команд:
        1. Добавить оценки ученика по предмету
        2. Редактировать оценки ученика по предмету
        3. Удалить оценки ученика по предмету
        4. Добавить нового ученика
        5. Редактировать имя ученика
        6. Удалить ученика
        7. Добавить новый предмет
        8. Редактировать предмет
        9. Удалить предмет
        10. Вывести средний балл по всем предметам по каждому ученику
        11. Вывести средний балл по всем предметам для определенного ученика
        12. Вывести средний балл по определенному предмету по каждому ученику
        13. Вывести средний балл по определенному предмету для определенного ученика
        14. Вывести все оценки по всем ученикам
        15. Вывести все оценки ученика
        16. Вывести имена всех учеников
        17. Вывести названия всех предметов
        18. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))

    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        if student in students:
            class_ = input('Введите предмет: ')
            if class_ in students_marks[student].keys():
                mark = int(input('Введите оценку: '))
                if mark in range(1,6):
                    students_marks[student][class_].append(mark)
                    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                    print()
                else:
                    print('ОШИБКА: некорректное значение оценки')
            else:
                print('ОШИБКА: неверное название предмета')
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 2:
        print('2. Редактировать оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        if student in students:
            class_ = input('Введите предмет: ')
            if class_ in students_marks[student].keys():
                students_marks[student][class_].clear()
                for i in range(3):
                    mark = int(input('Введите оценку: '))
                    if mark in range(1, 6):
                        students_marks[student][class_].append(mark)
                        print()
                    else:
                        print('ОШИБКА: некорректное значение оценки')
                print(f'Для {student} по предмету {class_} оценки изменены на {students_marks[student][class_]}')
            else:
                print('ОШИБКА: неверное название предмета')
        else:
            print('ОШИБКА: неверное имя ученика')


    elif command == 3:
        print('3. Удалить оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        if student in students:
            class_ = input('Введите предмет: ')
            if class_ in students_marks[student].keys():
                students_marks[student][class_].clear()
                print(f'Для {student} по предмету {class_} оценки удалены')
                print()
            else:
                print('ОШИБКА: неверное название предмета')
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 4:
        print('4. Добавить нового ученика')
        student = input('Введите имя нового ученика: ')
        students.append(student)
        print()

    elif command == 5:
        print('5. Редактировать имя ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            new_student = input('Введите новое имя ученика: ')
            students[students.index(student)] = new_student
            print()
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 6:
        print('6. Удалить ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            students.remove(student)
            print()
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 7:
        print('7. Добавить новый предмет')
        class_ = input('Введите имя нового предмета: ')
        classes.append(class_)
        print()

    elif command == 8:
        print('8. Редактировать предмет')
        class_ = input('Введите предмет: ')
        if class_ in classes:
            new_class = input('Введите новый предмет: ')
            classes[classes.index(class_)] = new_class
            print()
        else:
            print('ОШИБКА: неверное название предмета')

    elif command == 9:
        print('9. Удалить предмет')
        class_ = input('Введите предмет: ')
        if class_ in classes:
            classes.remove(class_)
            print()
        else:
            print('ОШИБКА: неверное название предмета')

    elif command == 10:
        print('10. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()

    elif command == 11:
        print('11. Вывести средний балл по всем предметам для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 12:
        print('12. Вывести средний балл по определенному предмету по каждому ученику')
        class_ = input('Введите предмет: ')
        if class_ in classes:
            for student in students:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{student} - {marks_sum // marks_count}')
            print()
        else:
            print('ОШИБКА: неверное название предмета')

    elif command == 13:
        print('13. Вывести средний балл по определенному предмету для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            class_ = input('Введите предмет: ')
            if class_ in students_marks[student].keys():
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'Средний балл - {marks_sum // marks_count}')
                print()
            else:
                print('ОШИБКА: неверное название предмета')
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 14:
        print('14. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 15:
        print('15. Вывести все оценки по определенному ученику')
        student = input('Введите имя ученика: ')
        if student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 16:
        print('16. Вывести имена всех учеников')
        students.sort()
        print(students)

    elif command == 17:
        print('17. Вывести названия всех предметов')
        print(classes)

    elif command == 18:
        print('18. Выход из программы')
        break

    else:
        print('ОШИБКА: такой команды не существует')



