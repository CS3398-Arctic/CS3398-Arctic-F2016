# Ignore this test

def main():
    avg = 0
    for exam in range (5):
        test = int(input('Please enter the test grade: '))
        letter_grade = determine_grade(test)
        print('The letter grade for that test is:',letter_grade)
        avg = calc_average(test, avg)
    print('The average of each test is:',avg)
    
def determine_grade(exam):
    if exam >= 90:
        letter_grade = 'A'
    elif exam >= 80:
        letter_grade = 'B'
    elif exam >= 70:
        letter_grade = 'C'
    elif exam >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return letter_grade

def calc_average(exam, avg):
    avg = avg + exam/5
    return avg

main()
