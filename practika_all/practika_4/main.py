from FullTimeStudent import FullTimeStudent
from PartTimeStudent import PartTimeStudent

student1 = FullTimeStudent(name="KOLA", age=24, prac_score=910, prac_count=10, exam_scr=95, attend_pct=85)
student2 = FullTimeStudent("Klavdia Petrivna", 19, 930, 10, 99, 20)

student3 = PartTimeStudent("Nazar", age=34, prac_score=760, prac_count=10, exam_scr=80)
student4 = PartTimeStudent("Petrivna", age=22, prac_score=840, prac_count=8, exam_scr=78)

print(f"""
      Студент 1:
      Ім'я: {student1.name}
      Вік: {student1.age}
      Загальний бал: {student1.total_score()}
      """)

print(f"""
      Студент 2:
      Ім'я: {student2.name}
      Вік: {student2.age}
      Загальний бал: {student2.total_score()}
      """)

print(f"""
      Студент 3:
      Ім'я: {student3.name}
      Вік: {student3.age}
      Загальний бал: {student3.total_score()}
      """)

print(f"""
      Студент 4:
      Ім'я: {student4.name}
      Вік: {student4.age}
      Загальний бал: {student4.total_score()}
      """)