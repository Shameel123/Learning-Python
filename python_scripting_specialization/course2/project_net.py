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
    if len(line1) > len(line2):
        for i in range(len(line2)):
            if line1[i] != line2[i]:
                return i
        # We've checked all the characters in the range and found no differences
        # but we know line1 is longer, so this is the position at which they differ
        return len(line2)
    elif len(line1) < len(line2):
        for i in range(len(line1)):
            if line1[i] != line2[i]:
                return i
        return len(line1)
    else:
        for i in range(len(line1)):
            if line1[i] != line2[i]:
                return i
        # They're the same length, and we've found no differences,
        # therefore the strings are identical
        return -1

line1="abc"
line2="abcd"
print(singleline_diff(line1,line2))


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if "\n" in line1 or "\n" in line2:
        return ""
    if idx < 0:
        return ""
    if len(line1) < len(line2):
        if idx > len(line1):
            return ""
    if len(line2) < len(line1):
        if idx >= len(line2):
            return ""

    return line1 + "\n" + "="*idx + "^" + "\n" + line2 + "\n"

IDENTICAL = -1


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    line_no = singleline_diff(lines1, lines2)

    len_lines1, len_lines2 = len(lines1), len(lines2)

    if len_lines1 == len_lines2:

        if (len_lines1 or len_lines2) == 0:
            if len_lines1 == len_lines2:
                return (IDENTICAL, IDENTICAL)
            idx = singleline_diff(lines1[line_no], lines2[line_no])
            return (line_no, idx)

        else:
            idx = singleline_diff(lines1[line_no], lines2[line_no])

            if line_no == IDENTICAL:
                return (IDENTICAL, IDENTICAL)
            elif line_no != IDENTICAL:
                return (line_no, idx)

    else:
        return (line_no, 0)
