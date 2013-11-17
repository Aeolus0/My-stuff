lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
 
def average(li):
    total = 0.0
    for i in li:
        total += i
    total = total / len(li)
    return total
def get_average(student):
    final = 0.0
    final = average(student["homework"]) * 0.1
    final += average(student["quizzes"]) * 0.3
    final += average(student["tests"]) * 0.6
    return final
def get_letter_grade(score):
    if score >=90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"
        
print get_letter_grade(get_average(lloyd))
