# p = False
# q = False
# print(not (p or not q))


# bool1 = True
# bool2 = False
#
# a = not bool1
#
# print(a)


# def nand(bool1, bool2):
#     """
#     Take two Boolean values bool1 and bool2
#     and return the specified Boolean values
#     """
#
#     if bool1:
#         if bool2:
#             return False
#         else:
#             return True
#     else:
#         return True
#
# a = nand(True,True)


def f(n):
    return n // 2 if n % 2 == 0 else 3*n + 1


print(f(f(f(f(f(f(f(1071))))))))
