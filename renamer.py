import os

filename = input('Filename: ')
increment = int(input('Increment: '))

file_list = os.listdir()
del file_list[file_list.index('renamer.py')]

try:
    for i in range(len(file_list)):
        if '.' in file_list[i]:
            extension = file_list[i].split('.')
            if extension[-1] != 'py':
                os.rename(file_list[i], 'kjajaþeývnwýnýowjpþga' + str(i) + '.' + extension[-1])

    file_list = os.listdir()
    for i in range(len(file_list)):
        if '.' in file_list[i]:
            extension = file_list[i].split('.')
            
            inc = ''
            if increment + i < 10:
                inc = '000' + str(increment + i)
            elif increment + i < 100:
                inc = '00' + str(increment + i)
            elif increment + i < 1000:
                inc = '0' + str(increment + i)
            else:
                inc = str(increment + i)
            if extension[-1] != 'py':
                os.rename(file_list[i], filename + ' ' + inc + '.' + extension[-1])
except:
    print('Congratulations! You have achieved 1*e-9999 probability!')
