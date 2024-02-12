import csv, sys


"""
Dictionary for storing the student name as key and the value of each key is another dict of subject names and corresponding scores
and also the total marks obtained by the student
"""
students = {}

with open(f"{sys.argv[1]}", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students[row["Name"]] = {
            "Biology": int(row["Biology"]),
            "Chemistry": int(row["Chemistry"]),
            "Maths": int(row["Maths"]),
            "Physics": int(row["Physics"]),
            "Hindi": int(row["Hindi"]),
            "English": int(row["English"]),
            "Total": int(row["Biology"])
            + int(row["Chemistry"])
            + int(row["Maths"])
            + int(row["English"])
            + int(row["Hindi"])
            + int(row["Physics"]),
        }

# Dictionary for storing the topper in each subject ,list is used as there are multiple topper in each subject
high_scorers = {
    "Biology": [],
    "Chemistry": [],
    "Hindi": [],
    "Maths": [],
    "English": [],
    "Physics": [],
}

# Dictionary for storing the highest marks in each subject
high_scores = {
    "Biology": 0,
    "Chemistry": 0,
    "Maths": 0,
    "English": 0,
    "Physics": 0,
    "Hindi": 0,
}

# Finding the topper in each subject
for key, value in students.items():
    for subject in high_scores:
        if value[subject] > high_scores[subject]:
            high_scores[subject] = value[subject]
            high_scorers[subject] = [key]
        elif value[subject] == high_scores[subject]:
            high_scorers[subject].append(key)


# Sorting the students in terms of the total marks obtained by them
ranked_student_names = sorted(
    students, key=lambda student: students[student]["Total"], reverse=True
)

# Printing the topper in each subject
for sub in high_scorers:
    print(f"the topper in {sub}:  {high_scorers[sub]}")


# Printing the top 3 students
print("The top 3 students in class are: ", end="")
print(ranked_student_names[:3])
