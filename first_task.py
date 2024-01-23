from datetime import datetime as dtdt


def get_days_from_today(date):
    try:
        date = dtdt.strptime(date, "%Y-%m-%d")
        tdelta = date.toordinal() - dtdt.today().toordinal()
        return(tdelta)
    except Exception:
        print("please enter the date in the format: YYYY-MM-DD")
        


print(get_days_from_today('2021-10-09'))

