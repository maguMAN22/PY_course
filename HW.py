def task2v1():
    print('Введите натуральное, трёхзначное число:')
    num = input()
    a = int(num[0])+int(num[1])+int(num[2])
    print(a)

def task2v2():
    print('Введите натуральное число:')
    num = input()
    a = 0
    for i in num:
        a = a + int(i)
    print(a)

def task4():
    print('Введите натуральное число:')
    num = int(input())
    x = int(num / 6)
    print(x , x*4 , x)

def task8():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if num3 < num1*num2 and (num3 % num1 == 0 or num3 % num2 == 0):
        print('yes')
    else: 
        print('no')

def task6():
    print('Введите натуральное, шестизначное число:')
    num = input()
    counter = 0
    a = 0
    b = 0
    while counter < 3:
        a = a + int(num[counter])
        b = b + int(num[counter + 3])
        counter += 1
    if a == b:
        print('yes')
    else:
        print('no')
