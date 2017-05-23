def main():
    input_name = input("Введите имя входного файла: ")
    output_name = input("Введите имя выходного файла: ")
    count(input_name, output_name)
    
def write(output_name,data,line,all_count):
    new_file = open(output_name, 'w')
    for i in range(line):
        string = str(100*data[i]/all_count)
        new_file.write(string+'\n')
    new_file.close
def count(input_name, output_name):
    data = [0]*100
    all_count = 0
    line = -1
    for i in open(input_name, 'r'):
        line += 1
        flag = True
        count_n = 1
        for j in range(len(i)):
            if i[j] == ' ' and flag:
                count_n += 1
                flag = False
            if (('a' <= i[j] <= 'z' or 'а' <= i[j] <= 'я') or
                ('A' <= i[j] <= 'Z' or 'А' <= i[j] <= 'Я')):
                   flag = True
        data[line] = count_n
        all_count += count_n
    write(output_name, data,line, all_count)
if __name__ == '__main__':
    main()
