student = {"Name": "Carlos", "Grade": "A", "Subjects": ["Math", "Science","Computer Science"]}
for key, value in student.items():
    print(f"{key}: {value}")
student["Graduated"] =False
print("Updated dictionary with graduation status:")
for key, value in student.items():
    print(f"{key}: {value}")