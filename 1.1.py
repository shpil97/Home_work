seconds = int(input('Введите число: '))
minutes = seconds // 60
hours = seconds // 3600
day = seconds // 86400
duration = f'{day} дн, {hours % 24} ч, {minutes % 60} мин, {seconds % 60} сек '
print(duration)
