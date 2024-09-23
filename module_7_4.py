def num(team1_num, team2_num):
    print('В команде %s участников: %s!' % (team1, team1_num))
    print('Итого сегодня в командах участников: %s и %s!' %
          (team1_num, team2_num))


# Использование format:


def time(team1, score1, team1_time):
    print('Команда {} решила задач: {}!'.format(team1, score1))
    print('{} решили задачи за {} cекунд!'.format(team1, team1_time))


# Использование f-строк:

def challenge_result(tasks_total, time_avg):
    print(f'Команды решили {score1} и {score2} задач')
    if score1 > score2 or score1 == score2 and team1_time < team2_time:
        result = f'Результат битвы: победа команды {team1}!'
    elif score1 < score2 or score1 == score2 and team1_time > team2_time:
        result = f'Результат битвы: победа команды {team2}!'
    else:
        result = f'Результат битвы: Ничья!'

    print(result)
    print(
        f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунд на одну задачу')


score1 = 50
score2 = 50
team1 = 'Волшебники данных'
team2 = 'Мастера кода'
team1_time = 1500
team2_time = 1500
time_avg = int((team1_time + team2_time) / (score1 + score2))
team1_num = 6
team2_num = 7
tasks_total = score1 + score2
num(team1_num, team2_num)
time(team1, score1, team1_time)
challenge_result(tasks_total, time_avg)
