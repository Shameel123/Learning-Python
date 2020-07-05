#------------------this is best to learn that a+=['word'] and a = a+['word'] are different
#-----------------------------------------------------------------------------------------
#-----conclusion given as : Y
# es, the behavior of obj = obj + object_two is different than obj += object_two when obj is a list. The first version makes a new object entirely and reassigns to obj. The second version changes the original object so that the contents of object_two are added to the end of the first.
#-------------------------------------------

# x = ["dogs", "cats", "birds", "reptiles"]
# print("this is x", x)
# y = x
# print("this is y", y)
#
# x += ['fish', 'horses']
# print("-------------after adding fish and horses in x---------------")
# print("this is x", x)
# print("this is y", y)
# print("-------------after adding sheep in y---------------")
# y = y + ['sheep']
# print("this is x", x)
# print("this is y", y)

#--------------------
#--------------------
#--------------------
#--------------------
# sent = "The mall has excellent sales right now."
# wrds = sent.split()
# wrds[1] = 'store'
# new_sent = " ".join(wrds)



a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")
print(a)
