from Person import Person

class FullTimeStudent(Person):
    def __init__(self, name, age, prac_score, prac_count, exam_scr, attend_pct):
        super().__init__(name,age,prac_score,prac_count,exam_scr)
        self.attend_pct = attend_pct

    def total_score(self):
        S_pr = self.avg_practice_score()
        S_ex = self.exam_scr
        S_att = self.attend_pct
        
        S = 0.6 * S_pr + 0.3 * S_ex + 0.1 * S_att
        
        return S

