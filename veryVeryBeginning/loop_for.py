# var = input("Enter the variable : ")
# print("Length of the string is {} ".format(len(var)))
# for i in var:
#     print(i)
#-----------------------------------------------------------
# abc = input("Enter anything : ")
# abc = abc.lower();
# print("Length is {} ".format(len(abc)))
# count = 0
# for i in abc:
#     if i=='a':
#         count += 1
#     elif i=='e':
#         count += 1
#     elif i=='i':
#         count += 1
#     elif i=='o':
#         count += 1
#     elif i=='u':
#         count += 1
# print("vowels are",count)
#-----------------------------------------------------------
# var = input("Enter : ")
# rev = ''.join(reversed(var))
# for i in rev:
#     print(i)
#-----------------------------------------------------------
# digit = input("Enter digits only :) : ")
# list1 = []
# for i in digit:
#     list1.append(int(i))
#
# print(list1)
# even = []
# odd  = []
# for i in list1 :
#     if i/2==1:
#         even += [i];
#     elif i/4==1:
#         even += [i];
#     elif i/6==1:
#         even += i;
#     elif i/8==1:
#         even += i;
#     elif i/1==1:
#         odd += i;
#     elif i/3==1:
#         odd += i;
#     elif i/5==1:
#         odd += i;
#     elif i/7==1:
#         odd += i;
#     elif i/9==1:
#         odd += i;
# print("Even number : ",even)
# print("Odd number  :",odd)
# --------------------------------UPPER METHOD DIDNT WORK SO TRYING DIFFERENT ONE ------------------------------------#
# digit = input("Enter a number please : ")
# hello = set(digit)
# even = []
# odd  = []
# for i in hello:
#     if int(i)%2==0:
#         even.append(int(i))
#     else:
#         odd.append(int(i))
# print("Even are : ",even)
# print("Odd are :  ",odd)
#---------------------------------------------------------------------------------------------------------------------#
# var = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,2,1,0],
#     [3,4,5,1],
#       ]
# for i in var:
#     st = ""
#     for j in i:
#         st = st + " " + str(j)
#     print(st)
#----------------------------------------------------------------------------------------------------------------------#
# length = int(input("Enter the length of MD list : "))
# height = int(input("Enter the height of MD list : "))
# list1 = []
# for i in range(0,length):
#     list2 = []
#     for j in range(0,height):
#         a = input("Enter the element {} of line {} in list {}".format(j+1,i+1,j+1))
#         list2.append(a)
#     list1.append(list2)
# print(list1)
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
#                                                Different Tutorials
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
# myList = [1,2,3,4,5]
# for i in range(0,len(myList)):
#     if myList[i]>2:
#         print(myList[i])
#----------------------------------------#
# names = ['shameel','uddin']
# num   = [1,2]
# for i,j in zip(names,num):
#     print(j)
#----------------------------------------#

