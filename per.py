import random
 
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