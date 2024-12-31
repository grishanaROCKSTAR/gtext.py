# Gtext.py V alpha 0.2
# Free and open-source program by grishanya
# GitHub: https://github.com/grishanaROCKSTAR/gtext.py/

#Goodies:

for i in range (1,100):
    print('~ ')
for i in range (1,10):
    print('.Welcome to Gtext!    .    alpha 0.2    .     .What do you want to do?')

gds= input(':')

# help

if gds == ('help'):
    for i in range(1,100):
        print('~ ')
    print('n - create new file\no - open file\n˄C - exit without changes\nabout - about the program\ngoodies - print a goodies page')
    gds= input(':')


# Goodies(startpage):

if gds== ('goodies'):
    for i in range (1,100):
        print('~ ')
    for i in range (1,10):
         print('.Welcome to Gtext!    .    alpha 0.2    .     .What do you want to do?')
    gds= input(':')


# About the program:

if gds == ('about'):
    for i in range(1,100):
        print('~ ')
    print("This program has been created by grishanya in 2024.\nThis program works on Python3 and full cross-platform.\n\ngrishanya's social networks:\ntelegram: grishanya1499")
    gds= input(':')


# Open file:

if gds == ('o'):
    for i in range(1,100):
        print('~ ')
    print("ALL FILES SAVES IN ~/'Рабочий стол'/gtext/gtext.autosave")
    openf= input('INPUT FILE: ')

else:
    print('INCORRECT ARGUMENT\nEXIT')


# New file:

if gds == ('n'):
    for i in range(1,100):
        print('~ ')
    for i in range(1,100):
        text= input('~ ')
    for i in range (1,100):
        print('~ ')
    for i in range (1,10):
        print('.FILE CLOSED AND SAVED    .    alpha 0.2    .     .What do you want to do?')
    gds= input(':')


# help2

if gds == ('help'):
    for i in range(1,100):
        print('~ ')
    print('n - create new file\no - open file\n˄C - exit without changes\nabout - about the program\ngoodies - print a goodies page')
    gds= input(':')


# Open file2:

if gds == ('o'):
    for i in range(1,100):
        print('~ ')
    print("ALL FILES SAVES IN ~/'Рабочий стол'/gtext/gtext.autosave")
    openf= input('INPUT FILE: ')

else:
    print('INCORRECT ARGUMENT\nEXIT')


# New file2:

if gds == ('n'):
    for i in range(1,100):
        print('~ ')
    for i in range(1,10):
        text= input('~ ')
    for i in range (1,100):
        print('~ ')
    for i in range (1,10):
        print('.FILE CLOSED AND SAVED    .    alpha 0.2    .     .What do you want to do?')
    gds= input(':')

