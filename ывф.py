russ = int(input('Введите кол-во баллов по русскому языку: '))
mat = int(input('Введите кол-во баллов по математики: '))
info = int(input('Введите кол-во баллов по информатики: '))
if russ + mat + info >= 270:
  print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет.')

