# # a = list(range(0,5,1))
# # print(a)
# #
# # my_list = ["This","course","is","great"]
# # b = len(my_list)
# # print(my_list[3])
# # print(my_list[0:len(my_list)//2+1:len(my_list)])
# #
# # n=5
# # m=4
# # init_list = list(range(1, n))
# # final_list = init_list * m
# # print(init_list)
# # print(final_list)
#
# n=0
#
# test_string = "xxx" + " " * n + "xxx"
# split_list = test_string.split(" ")
# print(test_string)
# print(split_list)
# print(len(split_list))


# list1 = list(range(1, 10))
# list2 = list1
# print(list1)
# print(list2)
# list1.append(999)
# list2.append(888)
# print(list1)
# print(list2)

def strange_sum(numbers):
    sum = 0
    for i in numbers:
        if i%3!=0:
           sum+=i
        else:
            continue
    return sum

print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))
