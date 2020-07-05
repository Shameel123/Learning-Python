# var = input("Enter a two-digit number : ")
# if var[0]<var[1] :
#     print("{} is less than {}".format(var[0],var[1]))
# else :
#     print("{} is less than {}".format(var[1],var[0]))
# ---------------------------------------------------------
palindrome = input("Enter a palindrome : ")
reverse = ''.join(reversed(palindrome))
if palindrome == reverse:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
