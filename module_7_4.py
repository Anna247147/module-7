# Задаем переменные
team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %
# Пример: "В команде Мастера кода участников: 5!"
formatted_str1 = "В команде Мастера кода участников: %d!" % team1_num
print(formatted_str1)

# Пример: "Итого сегодня в командах участников: 5 и 6!"
formatted_str2 = "Итого сегодня в командах участников: %d и %d!" % (team1_num, team2_num)
print(formatted_str2)

# Использование format()
# Пример: "Команда Волшебники данных решила задач: 42!"
formatted_str3 = "Команда Волшебники данных решила задач: {}!".format(score2)
print(formatted_str3)

# Пример: "Волшебники данных решили задачи за 18015.2 с!"
formatted_str4 = "Волшебники данных решили задачи за {:.1f} с!".format(team2_time)
print(formatted_str4)

# Использование f-строк
# Пример: "Команды решили 40 и 42 задач."
formatted_str5 = f"Команды решили {score1} и {score2} задач."
print(formatted_str5)

# Пример: "Результат битвы: победа команды Мастера кода!"
formatted_str6 = f"Результат битвы: {challenge_result}"
print(formatted_str6)

# Пример: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!"
formatted_str7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"
print(formatted_str7)