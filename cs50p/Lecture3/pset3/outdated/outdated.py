months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ")
        try:
            month, day, year = date.split('/')
            month, day, year = int(month), int(day), int(year)
            if 1 <= day <= 31 and 1 <= month <= 12:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except ValueError:
            try:
                month, day_year = date.split(' ', 1)
                day, year = day_year = day_year.split(',')
                day, year = int(day.strip()), int(year.strip())
                if month in months and 1 <= day <= 31:
                    month = months.index(month) + 1
                    newdate = f"{year}-{month:02}-{day:02}"
                    print(newdate)
                    break
            except ValueError:
                pass

main()
