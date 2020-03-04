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

if NofEx == 6:
      k=0
      human = ['Проверяйкина Елена','Честный Олег','Ревизоров Дмитрий','Злобина Василиса','Добрякова Татьяна']
      places = ['д. Большие Пупсы','г. Верхние васюки','д. Михайлючка','с. Гадюкино','пгт. Мамай','д. Бороденка',
                  'г. Бобрик','с. Весёлая жизнь','д. Кошки','г. Хохотуй','с. Похлёбкино','пгт. Цаца','с. Бабаево']
      # h1=[]; h2=[]; h3=[]; h4=[]; h5=[]
      # h1.append(random.choice(human)); h1.append(random.sample(places, k = random.randint(1, 3)))
      # print(h1)
      # h2.append(random.choice(human)); h2.append(random.sample(places, k = random.randint(1, 3)))
      # print(h2)
      # h3.append(random.choice(human)); h3.append(random.sample(places, k = random.randint(1, 3)))
      # print(h3)
      # h4.append(random.choice(human)); h4.append(random.sample(places, k = random.randint(1, 3)))
      # print(h4)
      # h5.append(random.choice(human)); h5.append(random.sample(places, k = random.randint(1, 3)))
      # print(h5)
      for i in range(len(human)):
            human[i] = random.sample(places, k = random.randint(1,3))
      print(human)

if NofEx == 7:
      auto = ['Nissan','Toyota','Honda','Audi']
      colors = ['Аквамарин(сине-зеленый)','Амазонка(ярко-зелёный)','Борнео (серебристо-тёмно-серый)','Звёздная Пыль (бежево-сиреневый)',
                  'Красный перец (серебристо-вишнёвый)','Магия (серебристо-ярко-фиолетовый)','Посейдон (тёмно-синий)',
                  'Франкония (тёмно-вишнёво-малиновый)','Черника(тёмно-синий)']
      res = []
      res.append(random.sample(auto, k=1) + random.sample(colors, k=1))
      res.append(random.sample(auto, k=1) + random.sample(colors, k=1))
      res.append(random.sample(auto, k=1) + random.sample(colors, k=1))
      print(res)

if NofEx == 8:
      students = {'Агатьева Арина','Алексеева Пальмира','Алексеев Феликс','Борисова Екатерина','Васильев Иван',
                  'Григорьева Елена','Данилов Александр','Жидова Анастасия','Исаков Константин','Иванов Иван',
                  'Клементьева Екатерина','Николаева Анжелика','Николаева Анна','Николаев Кирилл','Родионова Елена',
                  'Семёнова Анна','Терентьев Юрий','Фёдоров Владимир'}
      boys = ['Алексеев Феликс','Васильев Иван','Данилов Александр','Исаков Константин','Иванов Иван',
            'Терентьев Юрий','Фёдоров Владимир']
      girls = ['Агатьева Арина','Алексеева Пальмира','Борисова Екатерина','Григорьева Елена','Жидова Анастасия',
            'Родионова Елена','Семёнова Анна']
      print('----------1-я неделя месяца----------')
      print('В понедельник дежурят',random.choice(boys),'и', random.choice(girls));print('В вторник дежурят',random.choice(boys),'и', random.choice(girls));print('В среду дежурят',random.choice(boys),'и', random.choice(girls))
      print('В четверг дежурят',random.choice(boys),'и', random.choice(girls));print('В пятницу дежурят',random.choice(boys),'и', random.choice(girls));print('В субботу дежурят',random.choice(boys),'и', random.choice(girls))
      print('----------2-я неделя месяца----------')
      print('В понедельник дежурят',random.choice(boys),'и', random.choice(girls));print('В вторник дежурят',random.choice(boys),'и', random.choice(girls));print('В среду дежурят',random.choice(boys),'и', random.choice(girls))
      print('В четверг дежурят',random.choice(boys),'и', random.choice(girls));print('В пятницу дежурят',random.choice(boys),'и', random.choice(girls));print('В субботу дежурят',random.choice(boys),'и', random.choice(girls))
      print('----------3-я неделя месяца----------')
      print('В понедельник дежурят',random.choice(boys),'и', random.choice(girls));print('В вторник дежурят',random.choice(boys),'и', random.choice(girls));print('В среду дежурят',random.choice(boys),'и', random.choice(girls))
      print('В четверг дежурят',random.choice(boys),'и', random.choice(girls));print('В пятницу дежурят',random.choice(boys),'и', random.choice(girls));print('В субботу дежурят',random.choice(boys),'и', random.choice(girls))
      print('----------4-я неделя месяца----------')
      print('В понедельник дежурят',random.choice(boys),'и', random.choice(girls));print('В вторник дежурят',random.choice(boys),'и', random.choice(girls));print('В среду дежурят',random.choice(boys),'и', random.choice(girls))
      print('В четверг дежурят',random.choice(boys),'и', random.choice(girls));print('В пятницу дежурят',random.choice(boys),'и', random.choice(girls));print('В субботу дежурят',random.choice(boys),'и', random.choice(girls))
      # k = 0
      # k1 = 0
      # for i in range(len(students)):
      #       a = ','.join(students)
      # print(a)
      # for i in range(len(a)):
      #       if a[i] == ' ':
      #             if a[i-1] == 'а':
      #                   k+=1
      #                   print('девушка ',k)
      #             else: 
      #                   k1+=1
      #                   print('парень ',k1) 
      