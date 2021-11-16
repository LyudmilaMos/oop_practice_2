# Задание № 4. Полевые испытания

# Создайте по 2 экземпляра каждого класса, вызовите
# все созданные методы, а также реализуйте две функции:

# для подсчета средней оценки за домашние задания по всем
# студентам в рамках конкретного курса 
# (в качестве аргументов принимаем список студентов
# и название курса);

# для подсчета средней оценки за лекции всех лекторов
# в рамках курса (в качестве аргумента принимаем список
# лекторов и название курса).

# Решение № 4:

class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_score = 0
        students_list.append(self.__dict__)  

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.grades += [grade]
            lecturer.average_score = round(sum(lecturer.grades) / len(lecturer.grades), 2)
    
    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.average_score} \n' \
               f'Курсы в процессе изучения: {self.courses_in_progress} \n' \
               f'Завершенные курсы: {self.finished_courses}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.average_score < other.average_score

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        self.courses_attached = []
        self.grades = []
        self.courses_in_progress = []
        self.average_score = 0
        super().__init__(name, surname)
        lecturers_list.append(self.__dict__)

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.average_score}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.average_score < other.average_score

class Reviewer(Mentor):

    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(name, surname)     
            
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                sum_hw = 0
                counter = 0
                for key, value in student.grades.items():
                    sum_hw += sum(value) / len(value)
                    counter += 1
                student.average_score = round(sum_hw / counter, 2)

            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname}'

students_list = []
lecturers_list = []

def average_grade_hw(students, courses):
    sum_gs = 0
    counter = 0
    for student in students:
        for key, value in student['grades'].items():
            if courses in key:
                sum_gs += sum(value) / len(value)
                counter += 1
    return round(sum_gs / counter, 2)

def average_grade_lecturer(lecturers, courses):
    sum_gl = 0
    counter = 0
    for lecturer in lecturers:
        if courses in lecturer["courses_attached"]:
           sum_gl += sum(lecturer["grades"]) / len(lecturer["grades"])
           counter += 1
    return round(sum_gl / counter, 2)

petrova = Student('Елена', 'Петрова', 'ж')
petrova.courses_in_progress += ['Python']
petrova.finished_courses += ['Git']

ivanov = Student('Иван', 'Иванов', 'м')
ivanov.courses_in_progress += ['Python']
ivanov.courses_in_progress += ['Git']

sidorov = Lecturer('Сергей', 'Сидоров')
sidorov.courses_attached += ['Python']

chizikov = Lecturer('Николай', 'Чижиков')
chizikov.courses_attached += ['Git']

sorokin = Reviewer('Артем', 'Сорокин')
sorokin.courses_attached += ['Python']

popova = Reviewer('Ольга', 'Попова')
popova.courses_attached += ['Git']

sorokin.rate_hw(petrova, 'Python', 9)
sorokin.rate_hw(petrova, 'Python', 10)
sorokin.rate_hw(petrova, 'Python', 9)

popova.rate_hw(petrova, 'Git', 4)
popova.rate_hw(petrova, 'Git', 6)
popova.rate_hw(petrova, 'Git', 5)

sorokin.rate_hw(ivanov, 'Python', 7)
sorokin.rate_hw(ivanov, 'Python', 8)
sorokin.rate_hw(ivanov, 'Python', 8)

popova.rate_hw(ivanov, 'Git', 8)
popova.rate_hw(ivanov, 'Git', 6)
popova.rate_hw(ivanov, 'Git', 4)

petrova.rate_lecturer(sidorov, 'Python', 9)
petrova.rate_lecturer(sidorov, 'Python', 10)
petrova.rate_lecturer(sidorov, 'Python', 10)

ivanov.rate_lecturer(sidorov, 'Python', 10)
ivanov.rate_lecturer(sidorov, 'Python', 10)
ivanov.rate_lecturer(sidorov, 'Python', 10)

petrova.rate_lecturer(chizikov, 'Git', 10)
petrova.rate_lecturer(chizikov, 'Git', 9)
petrova.rate_lecturer(chizikov, 'Git', 9)

ivanov.rate_lecturer(chizikov, 'Git', 7)
ivanov.rate_lecturer(chizikov, 'Git', 6)
ivanov.rate_lecturer(chizikov, 'Git', 7)

print('Список студентов с показателями:')
print(f'')
print(petrova)
print(f'')
print(ivanov)
print(f'')
print('Список преподавателей с показателями:')
print(f'')
print(sidorov)
print(f'')
print(chizikov)
print(f'')
print('Список экспертов:')
print(f'')
print(sorokin)
print(f'')
print(popova)
print(f'')
print(f'Статистика:')
print(f'')
print('Средний балл за домашние задания по курсу "Python":', average_grade_hw(students_list, 'Python'))
print(f'')
print('Средний балл за домашние задания по курсу "Git":', average_grade_hw(students_list, 'Git'))
print(f'')
print('Средний балл за лекции по курсу "Python":', average_grade_lecturer(lecturers_list, 'Python'))
print(f'')
print('Средний балл за лекции по курсу "Git":', average_grade_lecturer(lecturers_list, 'Git'))
