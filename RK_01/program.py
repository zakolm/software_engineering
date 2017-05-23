def main():
    input_name = input("Введите имя файла: ")
    #data, count_all, count_lines
    #output_name = input("Введите имя файла: ")
    count()
    
def count():
    data = [0]*100
    all_count = 0
    for i in open("test.txt", 'r'):
        flag = True
        count_n = 1
        print(i)
        for j in range(len(i)):
            if i[j] == ' ' and flag:
                count_n += 1
                flag = False
            if 'a' <= i[j] <= 'z' or 'а' <= i[j] <= 'я' or 'A' <= i[j] <= 'Z' or 'А' <= i[j] <= 'Я':
                   flag = True
    data[i] = count_n
    all_count += count_n
    #input_array(all_count,data, i, count_n)
    #print(all_count,data, i, count_n)
    #print(count_n)
#def input_array(all_count,data, i, znach):
#    data[i] = znach
#    all_count += znach
if __name__ == '__main__':
    main()
