sec = int(input("Введите число секунд: "))
if sec > 3600:
    hours = sec // 3600
else: hours = 0
minutes = (sec-hours * 3600) // 60
seconds = sec % 60
print(f"{hours}:{minutes}:{seconds}")
