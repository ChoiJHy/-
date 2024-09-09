score = int(input())
grade = ''
match score:
    case score if 90 <= score <= 100:
        grade = 'A'
    case score if 80 <= score < 90:
        grade = 'B'
    case score if 70 <= score < 80:
        grade = 'C'
    case score if 60 <= score < 70:
        grade = 'D'
    case _:
        grade = 'F'

print(grade)