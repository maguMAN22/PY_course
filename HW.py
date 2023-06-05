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
    print(x, x*4, x)


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


def task10():
    coins = '100001'
    a = 0
    b = 0
    for i in coins:
        if int(i) < 1:
            a += 1
        else:
            b += 1
    if a < b:
        print(a)
    else:
        print(b)

def task12():
    summa = int(input())
    product = int(input())
    a = -1
    b = summa
    c = -product
    discriminant = b**2 - 4*a*c
    if discriminant == 0:
        x = -b / (2 * a)
        print(x)
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print(x1)
        print(x2)

def task14():
    a = int(input())
    b = 2
    while b * 2 < a:
        b = b * 2
        print(b)

def task16():
    print('Введите размер одномерного массива')
    arrayLength = int(input())
    print('Введите число для поиска его кол-ва в массиве')
    findNum = int(input())
    def genRandomArray(arrLength):
        arr = [0] * arrLength
        from random import randint
        for i in range(arrLength):
            arr[i]= randint(1,10)
        return arr
    def findNumQuantityInArray(arr, findNumber):
        counter = 0
        for i in arr:
            if i == findNumber:
                counter += 1
        return counter
    array = genRandomArray(arrayLength)
    print (array)
    print(findNumQuantityInArray(array,findNum))

def task18():
    def genRandomArray(arrLength):
        arr = [0] * arrLength
        from random import randint
        for i in range(arrLength):
            arr[i]= randint(1,10)
        return arr
    def findNumInArray(array, findNumber):
        counter = 0
        array.sort() 
        while counter < len(array):
            if array[counter] == findNumber:
                return array[counter]
            elif array[counter] > findNumber:
                return array[counter - 1]
            else:
                counter += 1
        return array[counter - 1]
    print('Введите размер одномерного массива')
    arrayLength = int(input())
    array = genRandomArray(arrayLength)
    print(array)
    print('Введите число для его поиска')
    findNum = int(input())
    print(findNumInArray(array,findNum))

def task20():
    print('Введите слово')
    word = str(input()).upper()
    summa = 0
    letters = {'AEIOULNSTR' : 1, 'DG' : 2, 'BCMP' : 3, 'FHVWY' : 4, 'K' : 5, 'JX' : 8, 'QZ' :10,
               'АВЕИНОРСТ' : 1, 'ДКЛМПУ' : 2, 'БГЁЬЯ' : 3, 'ЙЫ' :4, 'ЖЗХЦЧ' : 5, 'ШЭЮ' : 8, 'ФЩЪ' : 10}
    for key in letters:
        for letter in word:
            if letter in key:             
                summa = summa + letters.get(key)
    print(summa)



   


