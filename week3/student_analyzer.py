students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]
score = 56

def validate_score(score):
    if 0 < score <= 100:
        return True
    else:
        return False

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_average(students):
    total = 0 
    count = 0

    for student in students:
        total += student["score"]
        count += 1

    return total / count

def highest_lowest(students):
    highest = students[0]["score"]
    lowest = students[0]["score"]

    for student in students:
        score = student["score"]

        if score > highest:
            highest = score

        if score < lowest:
            lowest = score

    return highest, lowest



def passed_failed(students):
    passed = 0
    failed = 0

    for student in students:
        if student["score"] >= 50:
            passed += 1
        else:
            failed += 1
    return passed , failed 

def above_average_students(students):
    average = calculate_average(students)
    result = []

    for student in students:
        if student["score"] > average:
            result.append(student)

    return result



def generate_report(students):
    valid_students = []

    for student in students:
        score = student["score"]
        if validate_score(score):
            valid_students.append(student)
        else:
            print("Invalid score for:", student["name"])

    if len(valid_students) == 0:
        print("NO valid student results to analyze.")

    average = calculate_average(valid_students)
    highest , lowest = highest_lowest(valid_students)
    passed , failed = passed_failed(valid_students)
    above_average = above_average_students(valid_students)

    for student in valid_students:
        name = student["name"]
        score = student["score"]
        grade = calculate_grade(score)

        print(
            f"Name: {name:10}"
            f"Score: {score:3}" ," "
            f"Grade: {grade}"
        )
    print(f"Class average: {average:.2f}")
    print(f"Highest score: {highest}")
    print(f"Lowest score:  {lowest}")
    print(f"Passed:        {passed}")
    print(f"Failed:        {failed}")

    print("\nStudents above class average:")
    for student in above_average:
        print(f"{student['name']} - {student['score']}")

generate_report(students)    