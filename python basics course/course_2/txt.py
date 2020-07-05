# with open("travel_plans.txt","r") as file:
#     a = file.read()
#     print(a)
#     counter = 0
#     for i in a:
#         #print(i)
#         counter += 1
# num = counter
# print(counter)

# with open("emotion_words.txt","r") as file:
#     counter = 0
#     a = file.readlines()
#     print(a)
#     for i in a:
#         print(i)
#         wordList = i.split(" ")
#         for i in wordList:
#             print(counter)
#             print(i)
#             counter += 1
#
# print(counter)

# with open("school_prompt.txt","r") as file:
#     num_lines = 0
#     read = file.readlines()
#     for i in read:
#         print(i)
#         num_lines +=1
#
# print(num_lines)
# c=0
# with open("school_prompt.txt","r") as file:
#     read = file.readlines()
#     beginning_chars = str()
#     for i in read:
#         for j in i:
#             beginning_chars += j
#             print(beginning_chars)
#             print(c)
#             c+=1
#             if len(beginning_chars) >=30:
#                 break
#
# beginning_chars = beginning_chars[0:30]


# three = list()
# with open("school_prompt.txt") as file:
#     read = file.readlines()
#     for i in read:
#         print(i)
#         list = i.split()
#         try:
#             three.append(list[2])
#         except:
#             continue
#
# print(three)


# emotions  = list()
# with open("emotion_words.txt") as file:
#     read = file.readlines()
#     for i in read:
#         print(i)
#         list = i.split()
#         try:
#             emotions.append(list[0])
#         except:
#             continue
#
# print(emotions)


# with open("travel_plans.txt") as file:
#     read = file.readline()
#     print(len(read))
#     read = read[0:33]
#     print(len(read))
#     first_chars = read
#     print(len(first_chars))
#
# print(read)
# print(first_chars)



with open("school_prompt.txt","r") as file:
    a = file.read()
    p_words=list()
    #print(a)
    line = a.split("\n")
    print(line)
    for i in line:
        word = i.split(" ")
        for j in word:
            # print(j)
            if "p" in j:
                p_words.append(j)

print(p_words)
