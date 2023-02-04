def Season(mon):
    if mon in (12, 2, 1):
        return "Зима"
    elif mon in (3, 4, 5):
        return "Весна"
    elif mon in (6, 7, 8):
        return "Лето"
    elif mon in (9, 10, 11):
        return "Осень"


print(Season(int(input("Введите номер месяца: "))))
