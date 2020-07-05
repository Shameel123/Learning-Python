# # scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
# #
# # a_scores = int()
# #
# # individual = scores.split(" ")
# # print(individual)
# #
# # for i in individual:
# #     i = int(i)
# #     if i >= 90:
# #         a_scores+=1
# #
# # print(a_scores)
# #_------------
#
#
# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
# org = "The organization for health, safety, and education"
# acro = str()
# list1 = org.split(" ")
# print(list1)
#
# for i in list1:
#     #print(i)
#     if i in stopwords:
#         continue
#     else:
#         print(i)
#         print(i[0].upper())
#         acro += i[0].upper()
#
# print(acro)
#------------------------------

# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
# sent = "The water earth and air are vital"
# acro = str()
# list1 = sent.split(" ")
# print(list1)
# for i in list1:
#     if i in stopwords:
#         continue
#     else:
#         print(i[0].upper()+i[1].upper()+".")
#         acro+=i[0].upper()+i[1].upper()+". "
#
# acro = acro[0:-2]
# print(acro)

#------------------------
#expected result --> was I tac a ro rac a ti saw
#
# p_phrase = "was it a car or a cat I saw"
# r_phrase = p_phrase[::-1]
#
# print(r_phrase)
#----------------------------------------

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
#first --> item
#second--> how much in stock
#third---> how much it costs
#For example, the first print statment should read The store has 12 shoes, each for 29.99 USD



for i in inventory:
    #print(i)
    a = i.split(", ")
    #print(a)
    print("The store has {} {}, each for {} USD.".format(a[1],a[0],a[2]))
