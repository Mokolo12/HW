duration = int(input("Введите продолжительность в секундах: "))
if duration <= 60:
    print(f"{duration} cек")
elif duration <= 3600:
    m, s = duration // 60 % 60, duration % 60
    print(f"{m} мин {s} cек")
elif duration <= 86400:
    h, m, s = duration // 3600, duration // 60 % 60, duration % 60
    print(f"{h} час {m} мин {s} cек")
elif duration >= 86400:
    d, h, m, s = duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60
    print(f"{d} дней {h} час {m} мин {s} cек")
