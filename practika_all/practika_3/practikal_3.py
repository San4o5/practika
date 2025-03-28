students = []

def register_student(name, student_id):
    student = {
        "name" : name,
        "id" : student_id,
        "courses" : {}
    }

    students.append(student)
    return student

def add_course(student, course_name, credit_hours):
    student["courses"][course_name] = {
        "credit_hours" : credit_hours,
        "grades" : []
    }

def add_grade(student, course_name, grade):
    if course_name in student["courses"]:
        student["courses"][course_name]["grades"].append(grade)
    else:
        print(f"Курс {course_name} не знайдено!")

def calculate_average_grade(student,course_name):
    if course_name in student["courses"]:
        grades = student["courses"][course_name]["grades"]
        if grades:
            return sum(grades) / len(grades)
        return 0.0
    print(f"Курс {course_name} не знайдено!")
    return None
    
def calculate_gpa(student):
    total_points = 0
    total_credits = 0
    
    for course,data in student["courses"].items():
        avg_grade = calculate_average_grade(student, course)
        total_points += avg_grade * data["credit_hours"]
        total_credits += data["credit_hours"]
    return total_points / total_credits if total_credits else 0.0

def print_student_info(student):
    print(f"Студент: {student['name']} (ID: {student['id']})")
    print("Курси: ")
    for course, data in student["courses"].items():
        avg_grade = calculate_average_grade(student, course)
        print(f" - {course}: середня оцінка {avg_grade:.2f}, кредитні ггодини: {data["credit_hours"]}")
    print(f"Загальний GPA: {calculate_gpa(student):.2f}")

def main():
    while True:
        show_menu()    
        choise = input("Оберіть опцію: ")
        if choise == "1":
            handle_register_student()
        elif choise == "2":
            hanlde_add_course()
        elif choise == "3":
            handle_add_grade()
        elif choise == "4":
            handle_show_student_info()
        elif choise == "5":
            break
        else:
            print("Невірний вибір!")        
        
def show_menu():
    print('''
          Меню:
          1. Зареєструвати студента
          2. Додати курс
          3. Додати оцінку
          4. Показати інформацію про студента
          5. Вийти
          ''')    

def handle_register_student():
    name = input("Ім'я студента: ")
    student_id = input("ID студента: ")
    student = register_student(name, student_id)
    print(f"Студента {name} зареєстровано!")
    
def hanlde_add_course():
    student_name = input("Ім'я студента: ")
    course = input("Назва курсу: ")
    credit_hours = int(input("Кредитні години: "))
    for s in students:
        if s["name"] == student_name:
            add_course(s, course, credit_hours)
            print(f"Курс {course} додано студенту {student_name}")
    
def handle_add_grade():
    student_name = input("Ім'я студента: ")
    course = input("Назва курсу: ")
    grade =  float(input("оцінка: "))
    for s in students:
        if s["name"] == student_name:
            add_grade(s, course, grade)
            print(f"Оцінку {grade} додано для курсу {course}")
    
def handle_show_student_info():
    student_name = input("Ім'я студента: ")
    for s in students:
        if s["name"] ==  student_name:
            print_student_info(s)

main()