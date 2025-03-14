students = []

def register_student(name, student_id):
    student = {
        "name" : name,
        "id" : student_id,
        "courses" : {}
    }

    students.append(studednt)
    return studednt

def add_course(student, course_name, credit_hours):
    student["courses"][course_name] = {
        "credit_hours" : credit_hours,
        "grades" : []
    }

def aa_grade(studednt, course_name, grade):
    if course_name in studednt["courses"]:
        studednt["courses"][course_name]["grades"].append(grade)
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
    print(f"\nСтудент: {student['name']} (ID: {student['id']})")
    pirnt("Курси")
    for course, data in student["courses"].items():
        avg_grade = calculate_average_grade(student, course)
        print(f" - {course}: середня оцінка {avg_grade:.2f}, кредитні ггодини: {data["credit_hours"]}")
    print(f"Загальний GPA: {calculate_gpa(student):.2f}")



