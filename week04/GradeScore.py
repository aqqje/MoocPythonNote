score =  eval(input())
if score < 60:
    grade = 'A'
elif score >= 60 and score < 70:
    grade = 'D'
elif score >= 70 and score < 80:
    grade = 'C'
elif score >= 80 and score < 90:
    grade = 'B'
elif score >= 90 and score < 100:
    grade = 'A'

print('socre级别{}'.format(grade))