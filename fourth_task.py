import datetime as dt
from datetime import datetime as dtdt

def get_upcoming_birthdays(users): #повертає словник зіменами та датами привітання людей з днем народження на 7 днів вперед
    today = dtdt.today().date()
    coming_birthdays = []
    for user in users:
        user_birthday = dtdt.strptime(user["birthday"], "%Y.%m.%d").date()
        #змінює рік народження на сьогоднішній
        birthday_this_year = dtdt(today.year, user_birthday.month, user_birthday.day).date()

        #якщо др пройшов, додае до року 1
        if birthday_this_year < today:
            birthday_this_year = dtdt(birthday_this_year.year+1, birthday_this_year.month, birthday_this_year.day).date()
            
        
        days_before_birthday = (birthday_this_year - today).days

        if days_before_birthday <= 7:
            if birthday_this_year.weekday() >=5: #якщо др припав на вихідній, переносить привітання на наступний понеділок
                days_before_monday = 7 - birthday_this_year.weekday()
                greetings_day = birthday_this_year + dt.timedelta(days=days_before_monday)
            else:
                greetings_day = birthday_this_year
            coming_birthdays.append({"name":user["name"], "birthday greetings": greetings_day.strftime("%Y.%m.%d")})
    return(coming_birthdays)




users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.28"},
    {"name": "Sara Doe", "birthday": "1986.02.23"},
    {"name": "Stive Doe", "birthday": "1994.02.01"}
]
print(get_upcoming_birthdays(users))
