# Задание № 3. Полиморфизм и магические методы

# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:

# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy

# У лекторов:

# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9

# А у студентов так:

# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

# Реализуйте возможность сравнивать (через операторы сравнения)
# собой лекторов по средней оценке за лекции и 
# студентов по средней оценке за домашние задания.

# Решение № 3:

class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_score = 0

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

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_lecturer = Lecturer('Ruoy', 'Eman')
best_lecturer.courses_in_progress += ['Python']

best_student.rate_lecturer(best_lecturer, 'Python', 10)

print(best_student.grades)
print(best_lecturer.grades)