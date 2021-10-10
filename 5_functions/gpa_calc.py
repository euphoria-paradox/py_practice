# GPA Calculator

def convertGrade(grade):
    if grade == 'F':
        return 0
    else:
        return 4 - (ord(grade) - ord('A'))
    
    
def getGrades():
    semester_info = []
    more_grades = True
    empty_str =''
    while more_grades:
        course_grade = input('Enter the grade(hit Enter if done): ')
        while course_grade not in ('A','B','C','D','F',empty_str):
            course_grade = input('Enter letter grade recieved:')
        if course_grade == empty_str:
            more_grades = False
        else:
            num_credits = int(input('Enter the number of credits: '))
            semester_info.append([num_credits,course_grade])
    
    return semester_info


def calculateGPA(sem_grades_info, cumm_gpa_info):
    sem_quality_points = 0
    sem_credits = 0
    current_cumm_gpa, total_credits = cumm_gpa_info
    
    for k in range(len(sem_grades_info)):
        num_credits, letter_grade = sem_grades_info[k]
        
        sem_quality_points = sem_quality_points + \
                            num_credits * convertGrade(letter_grade)
        
        sem_credits = sem_credits + num_credits
        
    sem_gpa = sem_quality_points/ sem_credits
    new_cumm_gpa = (current_cumm_gpa * total_credits + sem_gpa * \
                    sem_credits) /(total_credits + sem_credits)
    
    return (sem_gpa, new_cumm_gpa)



# -- main

#greet
print('This program calculates new semester and cumulative GPAs\n')

#get current GPA info
total_credits = int(input('Enter the total number of credits earned: '))
cumm_gpa = float(input('Enter your current cumulative GPA: '))
cumm_gpa_info = (cumm_gpa, total_credits)

# get current semester grade
print()
semester_grades = getGrades()

#calculate sem GPA and new cumulative GPA
semester_gpa, cumm_gpa = calculateGPA(semester_grades, cumm_gpa_info)


# display semester gpa and new cumulative gpa
print('\n Your semester GPA is', format(semester_gpa,'.2f'))
print('Your new cumulative GPA is', format(cumm_gpa, '.2f'))