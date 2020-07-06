# def c_f(c):
#     f=(c*(9/5))+32
#     return f
# answer = int(input("Enter value in Celsius : "))
# print("Answer in Fahrenheit is : ",c_f(answer))
#---------------------------------------------------#
def length_string(value):
    if type(value)==int:
        print("Sorry, int doesn't have length")
    elif type(value)==float:
        print("Sorry, float doesn't have length")
    else:
        print(len(value))

# str1 = int(input("Enter String : "))
# print("Length of the string is : ",length_string(str1))
length_string("shameel")
