import sys 
import ast

def fib_num(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2 
    return fib_num(n-1) + fib_num(n-2) 

print(fib_num(20))

fib_num_file = "fib_num_file.text"
with open(fib_num_file,"w") as weird_file:
    for i in range(1,22):
        fib_number = fib_num(i)
        fib_index = i
        weird_file.write(str({fib_number:fib_index})+'\n')
    weird_file.close()

dict_information = []
with open(fib_num_file,"r") as weird_file:
    for line in weird_file.readlines():
        line = line.strip()
        line = str(line)
        line = ast.literal_eval(line)
        dict_information.append(line)
        weird_file.close()

def fib_nums_adder(dict_information):
    list_length = len(dict_information)
    fb_sub_n_minus_1 = dict_information[-1]  
    fb_sub_n_minus_2 = dict_information[-2]
    temp_list = [fb_sub_n_minus_1,fb_sub_n_minus_2]
    next_fb_num = 0
    for i in temp_list:
        next_fb_num += list(i)[0]
    dict_information.append({next_fb_num:list_length+1})

while int(list(dict_information[-1])[0]) < 4000000:
    with open('fib_num_file.text','a') as weird_file:
        fib_nums_adder(dict_information)
        weird_file.write(str(dict_information[-1]) + '\n')

sum = 0
for i in dict_information:  
    if int(list(i)[0]) % 2 == 0:
        sum += int(list(i)[0])
print(sum)


