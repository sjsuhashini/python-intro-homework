activity = True

while True:
    day = input("Enter a day of the week: ").strip().lower()
    if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]: #or time_of_day not in ["morning", "afternoon", "evening"]:
        print("Sorry, we don't recognize the day!")
        continue
    break

while True:
    time_of_day = input("Enter a time (morning, afternoon, evening): ").strip().lower()
    if time_of_day not in ["morning", "afternoon", "evening"]:
        print("Sorry, we don't recognize the time!")
        continue
    break

if day in ("monday","thursday"):
    if time_of_day == "morning":
        activity = "Go for a morning walk."
    elif time_of_day == "afternoon":
        activity = "Visit the library."
    elif time_of_day == "evening":
        activity = "Watch a movie."

elif day in ("tuesday" ,"wednesday" ,"friday"):
    if time_of_day == "morning":
        activity = "Practice yoga."
    elif time_of_day == "afternoon":
        activity = "Meet a friend for lunch."
    elif time_of_day == "evening":
        activity = "Read a book."

elif day in ( "saturday" , "sunday"):
    if time_of_day == "morning":
        activity = "Go cycling and Have fun!."
    elif time_of_day == "afternoon":
        activity = "Work on a hobby and Have fun!."
    elif time_of_day == "evening":
        activity = "Play a board game and Have fun!."

print(f"Suggested activity for {day.capitalize()} {time_of_day} is: {activity}")
