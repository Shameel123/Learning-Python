# rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
# rainfall_mi = rainfall_mi.split(",")
# print(rainfall_mi)
# num_rainy_months = list()
#
# for i in rainfall_mi:
#     i = float(i)
#     if i > 3.0:
#         num_rainy_months.append(i)
#
# num_rainy_months = len(num_rainy_months)

# same_letter_count = 0
# sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
# word = sentence.split(" ")
# print(word)
# for i in word:
#
#     if i[0] == i[-1]:
#         same_letter_count +=1
#
# print(same_letter_count)



# items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
#
# acc_num = 0
# for i in items:
#     if "w" in i:
#         print("w found in",i)
#         acc_num+=1
# print(acc_num)

# sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
# list = sentence.split(" ")
# num_a_or_e = 0
# for i in list:
#     if ("a") in i:
#         print("a found in",i)
#         num_a_or_e+=1
#     elif ("e") in i:
#         print("e found in",i)
#         num_a_or_e+=1
# print(num_a_or_e)



s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
word = s.split(" ")
print(word)
vowels = ['a','e','i','o','u']

# Write your code here.


num_vowels = 0

# for i in word:
#     print(i)
#     for j in vowels:
#         #print(j)
#         if j in i:
#             print("{} is found in {}".format(j,i))
#             num_vowels +=1
# print(num_vowels)


# for i in word:
#     print(i)
#     if vowels[0] in i:
#             num_vowels +=1
#             print("{} found in {}".format(vowels[0],i))
#     if vowels[1] in i:
#             num_vowels +=1
#             print("{} found in {}".format(vowels[1],i))
#     if vowels[2] in i:
#             num_vowels +=1
#             print("{} found in {}".format(vowels[2],i))
#     if vowels[3] in i:
#             num_vowels +=1
#             print("{} found in {}".format(vowels[3],i))
#     if vowels[4] in i:
#             num_vowels +=1
#             print("{} found in {}".format(vowels[4],i))
# print(num_vowels)

def count(s, c) :

    # Count variable
    res = 0

    for i in range(len(s)) :

        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res


for i in vowels:
    print(i)
    for j in word:
        if i in j:
            num_vowels += 1
            print("{} found in {}".format(i,j))
            print("count -->" , count(j,i))
            if count(j,i) == 2:
                num_vowels+=1
            print(num_vowels)

print(num_vowels)
