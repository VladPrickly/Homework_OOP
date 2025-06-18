# Класс студент

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {average_grade(self.grades)}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )

# Класс преподаватель


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Класс лектор


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
        self.grades = {}

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {average_grade(self.grades)}'
        )

# Класс проверяющий


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}'
        )

# Вычисление средней оценки


def average_grade(grades):
    if len(grades) > 0:
        len_grades = 0
        sum_grades = 0
        for i in grades:
            sum_grades += sum(grades[i])
            len_grades += len(grades[i])
        return sum_grades / len_grades
    return 'пока оценок нет'

# Сравнение оценок


def comparison(first, second):
    if type(first) == float and type(second) == float:
        if first == second:
            result = f'Средняя оценка студента = средней оценке преподавателя.'
        elif first > second:
            result = f'Средняя оценка студента > средней оценки преподавателя.'
        else:
            result = f'Средняя оценка студента < средней оценки преподавателя.'
    else:
        result = f'Средняя оценка студента (или преподавателя) отсутствует. Сравнить не представляется возможным.'
    return result


# Создание по 2 экземпляра каждого класса

student = Student('Ольга', 'Алёхина', 'Ж')
student.courses_in_progress += ['Python', 'Java', 'SQL']
student.finished_courses += ['Введение в программирование']

student_2 = Student('Сергей', 'Сергеев', 'М')
student_2.courses_in_progress += ['Python', 'C++', 'Java']
student_2.finished_courses += ['Git']

lecturer = Lecturer('Иван', 'Иванов')
lecturer.courses_attached += ['Python', 'Java', 'C++']

lecturer_2 = Lecturer('Николай', 'Сидоров')
lecturer_2.courses_attached += ['Python', 'C++', 'Go', 'SQL']

reviewer = Reviewer('Пётр', 'Петров')
reviewer.courses_attached += ['Python', 'C++', 'Java']

reviewer_2 = Reviewer('Анна', 'Григорьева')
reviewer_2.courses_attached += ['Python', 'Go', 'SQL', 'Java']

# Выставляем оценки

student.rate_lecture(lecturer, 'Python', 9)
student.rate_lecture(lecturer, 'С++', 8)
student.rate_lecture(lecturer, 'Java', 10)
student_2.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_2, 'SQL', 9)
student_2.rate_lecture(lecturer_2, 'C++', 10)
student.rate_lecture(lecturer_2, 'SQL', 9)
reviewer.rate_hw(student, 'Python', 8)
reviewer_2.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student, 'Java', 10)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Go', 7)
reviewer_2.rate_hw(student, 'SQL', 10)
reviewer.rate_hw(student_2, 'Java', 7)

# Вывод на печать данных экземпляров

print('СТУДЕНТ 1:', student, ' ', sep='\n')
print('СТУДЕНТ 2:', student_2, ' ', sep='\n')
print('ЛЕКТОР 1:', lecturer, ' ', sep='\n')
print('ЛЕКТОР 2:', lecturer_2, ' ', sep='\n')
print('ПРОВЕРЯЮЩИЙ 1:', reviewer, ' ', sep='\n')
print('ПРОВЕРЯЮЩИЙ 2:', reviewer_2, ' ', sep='\n')

# print(
#     f'СРАВНЕНИЕ: Сравниваем оценки {student.name} {student.surname} и {lecturer.name} {lecturer.surname}. {comparison(average_grade(student.grades), average_grade(lecturer.grades))}'
# )


# Вычисление средней оценки за курс

def average_grade_for_course(grades_list):
    new_dict = {}
    for i in grades_list[0].grades:
        for j in grades_list[1].grades:
            if j == i:
                res = grades_list[0].grades[i] + grades_list[1].grades[j]
            new_dict[i] = res
    new_dict = {**grades_list[0].grades, **grades_list[1].grades, **new_dict}
    result = ''
    for k in new_dict:
        result += f'{k} - {sum(new_dict[k]) / len(new_dict[k])}\n'
    return result


lecturer_lst = [lecturer, lecturer_2]
student_lst = [student, student_2]

print(
    f'Средняя оценка студентов по курсам:\n{average_grade_for_course(student_lst)}')
print(
    f'Средняя оценка преподавателей по курсам:\n{average_grade_for_course(lecturer_lst)}')
