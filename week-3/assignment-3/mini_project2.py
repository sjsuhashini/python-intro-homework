days = ("monday", "tuesday", "wednesday", "thursday",
        "friday", "saturday", "sunday")

times = ("morning", "afternoon", "evening")

activities = {
    "monday": {
        "morning": "Go for a morning walk.",
        "afternoon": "Visit the library.",
        "evening": "Watch a movie."
    },
    "tuesday": {
        "morning": "Practice yoga.",
        "afternoon": "Meet a friend for lunch.",
        "evening": "Read a book."
    },
    "wednesday": {
        "morning": "Go cycling.",
        "afternoon": "Work on a hobby.",
        "evening": "Play a board game."
    },
    "thursday": {
        "morning": "Try a new breakfast recipe.",
        "afternoon": "Visit a museum.",
        "evening": "Listen to your favorite music."
    },
    "friday": {
        "morning": "Do some gardening.",
        "afternoon": "Explore a new place.",
        "evening": "Enjoy a family game night."
    },
    "saturday": {
        "morning": "Go hiking.",
        "afternoon": "Visit a farmers market.",
        "evening": "Have dinner with friends."
    },
    "sunday": {
        "morning": "Enjoy a relaxing breakfast.",
        "afternoon": "Go for a picnic.",
        "evening": "Plan your upcoming week."
    }
}



while True:
    userDay = input("Enter a day of the week: ").strip().lower()
    if userDay not in days:
        continue
    break

while True:
    time_of_day = input("Enter a time (morning, afternoon, evening): ").strip().lower()
    if time_of_day not in times:
        print("Sorry, we don't recognize the time!")
        continue
    break

print(f"Suggested activity for {userDay.capitalize()} {time_of_day} is: {activities[userDay][time_of_day]}")
