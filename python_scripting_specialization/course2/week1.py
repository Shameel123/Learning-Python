# a = "shameeluddin"
# print(a[len(a)-1])
#
# b = "Castle Anthrax"
# print(b[7:])
# c=b.find("z")
# print(c)
#
# d = "abracadabra"
# print("{2}{1}{0}".format("abra","cad","abra"))


# def count_vowels(word):
#     count=0
#     for i in word:
#         if "a" in i:
#            count +=1
#         elif "e" in i:
#             count +=1
#         elif "i" in i:
#             count +=1
#         elif "o" in i:
#             count +=1
#         elif "u" in i:
#             count +=1
#
#     return count
# print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
# print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))


def demystify(l1_string):
    string = str()
    for i in l1_string:
        if "l" in i:
            string += "a"
        elif "1" in i:
            string += "b"
    return  string

print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
