import random

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