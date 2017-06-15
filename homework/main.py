## @mainpage Преобразование числа в зависимости от его четности/нечетности
# @section intro_sec Описание программы
#
# В текстовом файле содержатся целые числа.
# Найти сумму цифр каждого числа и если она четная, то перевести его в двоичную систему счисления, а если нечетная, то преобразовать число в обратном порядке следования цифр.
# Результат записать в другой файл.

import os

MAX_STRING = 100
OK = 0 ## All ok
NOT_OK = -1 ## Something not ok
FILE_EMPTY = -2 ## File is empty
EOF = -3 ## End of file
FILE_NE = -4 ## File is not exist
STRING_COR = 0 ## String is correct
STRING_INCOR = -6 ## String isn't correct

## Вход в программу
#
# @throw STRING_COR Строка корректна
# @throw STRING_INCOR Строка некорректна
# @throw FILE_EMPTY Файл пустой
# @throw EOF Конец файла
# @throw OK Все хорошо
# @throw NOT_OK Что-то не хорошо

def main():
    rc = OK ## The error code of the main function
    rc_t = OK ## The error code of the called function

    ## Open result file for writing
    f_out = open('f_out.txt', 'w')
    rc, array, len_array = Work_My_Program(f_out)
    if (not rc):
        WorkArray(f_out, array, len_array)
    f_out.close()
    
    return rc

def Work_My_Program(FILE):
    rc = OK
    ## Check for existence of source file
    if os.path.exists('f_in.txt'):
        ## Open source file for reading
        f_inp = open('f_in.txt', 'r')
        i = 0; array = [[0 for i in range(MAX_STRING)] for i in range(MAX_STRING)]
        rc_t = OK
        ## Until the end of the file
        while (i <= MAX_STRING):
            array[i][0],array[i][1] = ReadString(f_inp, i)
            #print(array[i][0], array[i][1], i, EOF, FILE_EMPTY)
            if (array[i][1] == FILE_EMPTY or array[i][1] == EOF):
                break
            i += 1
        f_inp.close()
    else:
        print('File does not exist\n')
        FILE.write('File does not exist\n')
        rc = FILE_NE
        
    return rc, array, i
def WorkArray(FILE, array, len_array):
    rc = OK
    for i in range(len_array):
        if (not array[i][1]):
            x_s = SumNum(array[i][0])
            x_t = TypeSum(x_s)
            if x_t == True: # Num is even
                x_n = TransformEvenNum(array[i][0])
            else: # Num is uneven
                x_n = TransformUnevenNum(array[i][0])                    
            FILE.write('{:d}\n'.format(x_n))
        else:
            if array[i][1] == STRING_INCOR:
                FILE.write('incorrect data\n')
            elif array[i][1] == FILE_EMPTY:
                print('File is empty')
                FILE.write('File is empty\n')
                rc = FILE_EMPTY
            else:
                print('Success!')
    return rc
            

#def CheckString  ():         

## Преобразовываем строку в файл
#
# @throw STRING_COR Строка корректна
# @throw STRING_INCOR Строка некорректна
# @throw FILE_EMPTY Файл пустой
# @throw EOF Конец файла
# @param f_inp - файловая переменная
# @param i - номер текущей строки
# @return x - число
# @return rc - код ошибки

def ReadString(f_inp, i):
    assert f_inp != None, 'input file not exist'
    
    rc = STRING_COR
    x = 0 ## The current number

    ## Read the current line
    string = f_inp.readline() 

    ## If not the end of the file, then
    if string:
        ## Array of num
        num_ch = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

        ## Check for incorrect string
        for i in range(len(string)):
            if (string[i] not in num_ch):
                condition_1 = (i == 0 and string[i] == '-')
                condition_2 = (i == len(string) - 1 and string[i] == '\n')
                condition_3 = (i == 0 and string[i] == '\n')

                if not (condition_1 or condition_2) or condition_3:
                    rc = STRING_INCOR
                    break
                
        ## If the string correct, then transform it into a number
        if rc == STRING_COR:                                
            x = int(string)

        ## Check for membership once the number
        ## range described in assumptions
        if x >= 128 or x < -128:
            rc = STRING_INCOR
    else:
        rc = EOF
        if i == 0:
            rc = FILE_EMPTY

    return x, rc

## Считаем сумму цифр числа
#
# @param x current num
# @return x_s sum of num in x

def SumNum(x):
    assert x - int(x) == 0, 'current num not int'
    
    x_l = abs(x)

    ## @var x_l
    # local clone of 

    x_s = 0
    while x_l != 0:
        x_s = x_s + (x_l % 10)
        x_l = x_l // 10

    assert x_s >= 0, 'sum of num < 0'
        
    return x_s

## Определяем код ошибки
#
# @param x_s - сумма цифр числа
# @return x_t - признак четности/нечетности суммы цифр числа

def TypeSum(x_s):
    assert x_s - int(x_s) == 0, 'num not int'
    
    if x_s % 2 == 0:
        x_t = True
    else:
        x_t = False

    return x_t

## Переводим в двоичную форму число
#
# @param x - число
# @return x_n - преобразованное число

def TransformEvenNum(x):
    assert x - int(x) == 0, 'current num not int'
    assert x >= -128 and x < 128, 'x not signed int 2^8'
    
    x_l = abs(x)

    x_n = 0
    h = 1
    while x_l != 0:
        if x_l % 2 == 1:
            x_n = x_n + h
        h = h*10
        x_l = x_l // 2

    if x < 0:
        k = 0
        h = 1
        while k != 8:
            if x_n % (h*10) < h:
                x_n = x_n + h
            else:
                x_n = x_n - h
            k = k + 1
            h = h*10

        k = 0
        h = 1
        flag = True
        while flag and k != 8:
            if x_n % (h*10) < h:
                x_n = x_n + h
                flag = False
            else:
                x_n = x_n - h
            k = k + 1
            h = h*10
            
    assert x_n >= 0, 'incorrect transform'
    assert x_n - int(x_n) == 0, 'num not int'

    return x_n

## Перезаписываем число в обратном порядке
#
# @param x - число
# @return x_n - преобразованное число

def TransformUnevenNum(x):
    assert x - int(x) == 0, 'current num not int'
    assert x >= -128 and x < 128, 'x not signed int 2^8'
    x_l = abs(x)

    x_n = 0
    
    while x_l != 0:
        x_n = x_n*10 + x_l % 10
        x_l = x_l // 10
        
    if x < 0:
        x_n = -x_n
        
    assert x_n - int(x_n) == 0, 'num not int'

    return x_n

if __name__ == '__main__':
    main()
