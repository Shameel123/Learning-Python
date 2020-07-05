def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.


      Returns IDENTICAL if the two lines are the same.
    """

    lst1 = line1.split(" ")
    lst2 = line2.split(" ")
    if len(lst1) < len(lst2):
        counter = len(lst1)
    else:
        counter = len(lst2)
    print(counter)
    print(lst1)
    # print(lst1.index("This"))
    print(lst2)
    for i in range(0,counter):
        print(lst1[i][0],lst2[i][0])
        if lst1[i][0] == lst2[i][0]:
            print(lst1[i][0],lst2[i][0],"match")
        else:
            print(lst1[i][0],lst2[i][0],"not matches")
            print(line1)
            print(line2)
            print(lst1[i],lst2[i])
            print(line1.index(lst1[i]))
            print(line2.index(lst2[i]))
            return line2.index(lst2[i])
            # return lst1.index()
    return -1

line1 = "abc"
line2 = "abc"
print(singleline_diff(line1,line2))
