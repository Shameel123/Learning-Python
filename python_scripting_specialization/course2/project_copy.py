"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.
Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import re
IDENTICAL = -1

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
    length = min(len(line1),len(line2))
    for index in range(length):
        if line1[index] != line2[index]:
            return index
    if len(line1)!=len(line2):
        return length
    else:
        return IDENTICAL


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
    if idx>len(line1) or idx>len(line2) or idx<0:
        return ""
    if line1.find("\n")!=-1 or line1.find("\r")!=-1 or line2.find("\n")!=-1 or line2.find("\r")!=-1:
        return ""
    else:
        return line1+"\n"+"="*idx+"^\n"+line2+"\n"

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
    length = min(len(lines1), len(lines2))
    for line in range(length):
        index = singleline_diff(lines1[line],lines2[line])
        if(index != IDENTICAL):
            return (line, index)
    if len(lines1)==len(lines2):
        return (IDENTICAL,IDENTICAL)
    else:
        return (length, 0)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.
      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file1 = open(filename,'rt')
    lst1 = []
    for line in file1:
        lst1.append(line.strip("\n"))
    file1.close()
    return lst1


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.
      If the files are identical, the function instead returns the
      string "No differences\n".
      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    tuple1 = multiline_diff(lines1,lines2)
    if tuple1 ==(IDENTICAL,IDENTICAL):
        return "No differences\n"
    else:
        line_index = tuple1[0]
        string_index = tuple1[1]
        if(lines1!=[] and lines2!=[]):
            line1 = lines1[line_index]
            line2 = lines2[line_index]
            return "Line "+str(line_index)+":\n"+singleline_diff_format(line1,line2,string_index)
        elif lines1==[]:
            line2 = lines2[line_index]
            return "Line 0:\n\n^\n" + line2+"\n"
        else:
            line1 = lines1[line_index]
            return "Line 0:\n"+line1+"\n^\n\n"
