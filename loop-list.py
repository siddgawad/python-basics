list_num = input("Input a list of numbers seperated by space: \n") # 1 2 3 4 5

list_num = list(map(int,list_num.split()))







sum_value= sum(list_num)
max_value=max(list_num)
min_value=min(list_num)
avg=sum_value/(len(list_num))
sorted_list = sorted(list_num)
dict_number={}



for i in sorted_list:
    if i in dict_number:
        dict_number[i]+=1
    else:
        dict_number[i]=1

mode = None # we use none isntead of zero, as we do not want to assume user will not input 0
max_count = 0

for i in dict_number:
    if dict_number[i]>max_count:
        max_count=dict_number[i]
        mode=i
    





if len(sorted_list)%2==0:
    mid = len(sorted_list)//2 #double slash returns an integer, unlike single slash which returns float value
    median= (sorted_list[mid-1] + sorted_list[mid])/2

elif len(sorted_list)%2!=0:
    mid = sorted_list[len(sorted_list)//2]
    median = (sorted_list[mid])





print("max value:",max_value)
print("min value:",min_value)
print("Sum of the numbers is:\n",sum)
print("Average is: \n",avg)
print("Median is: \n",median)
print("Here is a list of numbers frequency: \n",dict_number)
print("mode of numbers is: \n",mode)

    