list_number=list(map(int,input("Enter list of numbers seperated by space:\n").split()))

sum_value=0
dict_num={}
mode=None
count_num=0


for i in list_number:

    sum_value= sum_value+i


    if i in dict_num:
       dict_num[i]+=1
    else:
       dict_num[i]=1

for i in dict_num:
   if dict_num[i]>count_num:
      count_num=dict_num[i]
      mode=i

sorted_list=sorted(list_number)
mid = len(sorted_list)//2
if len(sorted_list)%2 == 0:
    
    median=(sorted_list[mid]+sorted_list[mid-1])/2
else:
    median=sorted_list[mid]



    

average_value=(sum_value)/(len(list_number))

max_value=max(list_number)
min_value=min(list_number)






print("Sum of numbers is: \n",sum_value)
print("Average of numbers is: \n",average_value)
print("Maximum of numbers is:\n",max_value)
print("Minimum value is",min_value)
print("Median is:\n",median)
print("Mode is:\n",mode)
print("Dictionary is:\n",dict_num)