#1
##1)
n1=int(input('정수를 입력하세요 > '))
if '-' in str(n1):
    print(str(n1)[1:])
else:
    print(n1)

##2)
number = int(input("정수를 입력하세요 > "))
if number > 0:
    print(number)
else:
    print(number * -1)
    
#2
number_list = [1, 2, 3, 4, 5]
i=0
for number in number_list:
    i+=1
print(i)

#3
number_list = [1, 2, 3, 4, 5]

total=0
for number in number_list:
    total+=number
print(total)

#4
number_list = [2, 4, 6]

total_sum=0
total_len=0
for number in number_list:
    total_sum+=number
    total_len+=1
print(total_sum/total_len)

#5
number_list = [-1, -2, 3]

total_ave=1
for number in number_list:
    total_ave*=number

print(total_ave)

#6
number_list = [1, 1, 1]

top=number_list[0]

for number in number_list:
    if number > top :
        top=number
print(top)

#7
number_list = [5, 5, 5, 2]

bottom=number_list[0]

for number in number_list:
    if number < bottom :
        bottom=number
print(bottom)