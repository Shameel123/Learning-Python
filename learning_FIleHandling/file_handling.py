# file = open('example.txt','r')
# file.seek(0) #always start file from very beginning, it is because when program runs 2nd time, the cursor is at the end
# content=file.readlines()
# print(content)
# content=[i.rstrip("\n") for i in content]
# print(content)
# file.close() #this is the crucial thing. If this file is opened in python then we won't be able to write in it so it is must for to close it after we're done operating in it
#-----------------------------------------------------------------------------------------------------------------------
# file = open("fruits.txt","r")
# file.seek(0)
# content = file.readlines()
# content = [i.rstrip('\n') for i in content]
# for i in content:
#     print(i,len(i))
# file.close()
#-----------------------------------------------------------------------------------------------------------#
#--------------------------------------------------Writing--------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------#
# file=open("example.txt",'w')
# myList = ["shameel","uddin"]
# for i in myList:
#     file.write(str(i))
#     file.write("\n")
# file.close()
#---------------------------------------#
    # with open("example.txt","a"):
    #     file.seek(0)
    #     content = file.read()
    #      file.write("\nLine6")
#-----------------I DID NOT GET THIS WITH STATEMENT---------------------------------------------------------#


# def c_to_f(c):
#     if c<-273.14:
#         return "this temp doesn't make sense"
#     else:
#         f=c*9/5+32
#         return f
#
# #-----Function ends here
#
# temp = [10,-20,-289,100]
# file = open("temperature.txt","w")
#
# for i in temp:
#     if i>-273.15:
#         file.write(str(c_to_f(i)))
#         file.write("\n")
