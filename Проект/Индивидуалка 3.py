# Начальные данные
initial_distance = 10  # начальное расстояние в км
daily_increase_rate = 0.1  # увеличение на 10%
total_days = 7  # количество дней

# Суммируем общее расстояние
total_distance = 0

# Расчет расстояний за каждый день
for day in range(total_days):
    total_distance += initial_distance
    initial_distance *= (1 + daily_increase_rate)  # увеличиваем на 10%

print("Суммарный путь пробежит спортсмен за 7 дней:", total_distance)
