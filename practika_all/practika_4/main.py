from FullTimeStudent import FullTimeStudent
from PartTimeStudent import PartTimeStudent

student1 = FullTimeStudent(name="KOLA", age=24, prac_score=910, prac_count=10, exam_scr=95, attend_pct=85)
student2 = FullTimeStudent("Klavdia Petrivna", 19, 930, 10, 99, 20)

student3 = PartTimeStudent("Nazar", age=34, prac_score=760, prac_count=10, exam_scr=80)
student4 = PartTimeStudent("Petrivna", age=22, prac_score=840, prac_count=8, exam_scr=78)

unversity_students = [student1,student2,student3,student4]

for student in unversity_students:
    student.display_info()
    if isinstance(student, FullTimeStudent):
        print(f"Загальний бал (очно): {student.total_score()}")
    elif isinstance(student,PartTimeStudent):
        print(f"Загальний бал (заочно): {student.total_score()}")
