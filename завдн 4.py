from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming = []

    for user in users:
        # Перетворення рядка дати на об'єкт дати
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Заміна року на поточний
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув у цьому році, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця в днях між сьогодні і днем народження
        days_diff = (birthday_this_year - today).days

        if 0 <= days_diff <= 7:
            # Якщо день народження у вихідний — переносимо на понеділок
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Неділя
                congratulation_date += timedelta(days=1)

            # Додаємо результат у список
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming
