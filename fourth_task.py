from datetime import datetime as dtdt

def get_upcoming_birthdays(users):
    for user in users:
        dtdt.strptime(user["birthday"], "%Y.%m.%d").date()
        




users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
print(dtdt.today().date())
