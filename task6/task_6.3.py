import time


date_now = time.time()
f = input("Введите дату рождения в формате дд-мм-гггг: ")
date = time.mktime(time.strptime(str(f), "%d-%m-%Y"))
print("Прожито дней:", int((date_now - date) / 86400))

