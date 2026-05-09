

import module2 
import module1
def display_result():
    name=module1.get_student_data()
    grade,score=module2.cal_gradescore()
    
    return f"{name} you {grade} your score is {score}"