# Using loops and data structure operations, your script must:
# Find the top scorer — loop through the list and track the highest score and the name that goes with it. Do not use Python's built-in max() on the list directly.
# Calculate the class average — accumulate the total score in a loop, then divide.
# List all unique subjects — use a set to collect subjects as you loop, then print them.
# List high scorers — use a loop and .append() to get the names of all students who scored above 75.
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

uniqueSubject_set = set()
topScorer_List = []
totalScore = 0
maxScore = students[0]["score"]
topScorers_Dict = {}

#Max score
for student in students:
    totalScore += student["score"]
    uniqueSubject_set.add(student["subject"])
    if student["score"] >= 75:
        topScorer_List.append(student["name"])
    if student["score"] > maxScore:
        maxScore = student["score"]
        topScorers_Dict.clear()
        #topStudent = student["name"]
    if student["score"] == maxScore:
        topScorers_Dict[student["name"]] = student["score"]

averageScore = totalScore / len(students)
print(f"Class average: {averageScore}")   
print(f"Unique subjects list : {uniqueSubject_set}")
print(f"List of students who got scores above 75 : {topScorer_List}")
print(f"Top Student: {topScorers_Dict}")  

