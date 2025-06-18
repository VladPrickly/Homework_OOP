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


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Ольга', 'Алёхина', 'Ж')

student.courses_in_progress += ['Python', 'Java']
student.finished_courses += ['Введение в программирование']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

student.rate_lecture(lecturer, 'Python', 7)
student.rate_lecture(lecturer, 'Java', 8)
student.rate_lecture(lecturer, 'С++', 8)
student.rate_lecture(reviewer, 'Python', 6)

print('СТУДЕНТ:', student, ' ', sep='\n')
print('ЛЕКТОР:', lecturer, ' ', sep='\n')
print('ПРОВЕРЯЮЩИЙ:', reviewer, ' ', sep='\n')

print(
    f'СРАВНЕНИЕ: Сравниваем оценки {student.name} {student.surname} и {lecturer.name} {lecturer.surname}. {comparison(average_grade(student.grades), average_grade(lecturer.grades))}'
)
