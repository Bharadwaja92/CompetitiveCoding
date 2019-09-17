""""""
"""
https://www.techgig.com/practice/question/dlA4ZjNCTE1kNmdtbzlybWwwRzNkZz09

Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be 
used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.
You are given a data containing test results of class. The dataset consists of two columns namely : 'marks' and 'name'. 
These two Columns can be in any order i.e. ('name' followed by 'marks' or vice versa).
You have to find the average marks for the whole class.

Input Format
First line will contain an Integer N, denoting the number of students.
Next line will contain two string denoting the column heading.
Next N lines will contain marks and name of the students respective of column headings.

Constraints
1 <= N <= 10^3
0 <= Marks <= 100

Output Format: Output the average marks of the class rounded off to two decimal places.

Sample TestCase 1
Input
3
marks names
10 arpit
20 anushka
35 rakshita
Output
21.67

"""
from collections import namedtuple


def main1():
    n = int(input())
    l1 = input().split()
    total_marks = 0

    for i in range(n):
        l2 = input().split()
        total_marks += int(l2[0])

    print('{0:.2f}'.format(total_marks / n))


def main():
    n = int(input())
    l1 = input().split()
    student = namedtuple(l1[1], ['marks', 'name'])
    marks = []
    if l1[0] == 'marks':
        marks = [int(student._make(input().split()).marks) for _ in range(n)]
    else:
        marks = [int(student._make(input().split()).name) for _ in range(n)]
    print('{0:.2f}'.format(sum(marks) / n))


main()


"""
def main():
    n = int(input())
    l1 = input().split()
    student = namedtuple(l1[1], ['marks', 'name'])
    marks = [int(student._make(input().split()).marks) for _ in range(n)]
    print('{0:.2f}'.format(sum(marks) / n))
"""