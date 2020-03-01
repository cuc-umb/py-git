import random
from math import *

NofEx = int(input('Введите номер задания: '))

if NofEx == 1:
      a = []; k0=0; k1=0
      for i in range(100):
            a.append(random.randint(-25, 25))
      print('num: ',a)
      for i in a:
            if i % 2 == 0:
                  k0+=1
            else: 
                  k1+=1
      print('четных: ',k0)
      print('нечетных: ',k1)

if NofEx == 2:
      a = 0.0; b = 0.0; c = 0.0
      a = random.uniform(1, 10)
      print('Катет a: ', a)
      b = random.uniform(1, 10)
      print('Катет b: ', b)
      c = sqrt((a ** 2)+(b ** 2))
      print('Гипотенуза: ',c)
            
if NofEx == 3:
      a = 0; b = 0; c = 0
      sum = ''
      a = random.randint(1, 6)
      b = random.randint(1, 6)
      c = random.randint(1, 6)
      sum= str(a) + str(b) + str(c) 
      print(sum)     

if NofEx == 4:
      actors = ['Смычкова Татьяна','Скрипкина Светлана','Саксофонова Ирина',
            'Трубников Олег','Баянов Святослав','Балалайкин Валентин',
            'Басов Рустем','Песняр Ярослав','Музычко Игорь','Альтова Елена']
      str1 = ''; str2 = ''; str3 = ''
      print('Первый этап')
      random.shuffle(actors); str1 = ''.join(actors)+ "\n"; print(str1)
      print('Второй этап')
      random.shuffle(actors); str2 = ''.join(actors)+ "\n"; print(str2)
      print('Третий этап')
      random.shuffle(actors); str3 = ''.join(actors)+ "\n"; print(str3)

if NofEx == 5:
      n = int(input('Промежуток n: '))
      m = int(input('Колличество m: '))
      a = []
      if(m<n):
            for i in range(m):
                  a.append(random.randint(0, n)) 
            print(a)
      else: 
            print('неправильное m')