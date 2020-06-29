'''
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students. 
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
'''

n=int(input())
arr=[[input(),float(input())] for _ in range(0,n)]
arr.sort(key=lambda x: (x[1],x[0]))
names = [i[0] for i in arr]
marks = [i[1] for i in arr]
min_val=min(marks)
while marks[0]==min_val:
    marks.remove(marks[0])
    names.remove(names[0])    
for x in range(0,len(marks)):
    if marks[x]==min(marks):
        print(names[x])

'''if __name__ == '__main__':

    name = [] ; score = []

    for _ in range(int(input())):
        #name = input()
        name.append(input())
        #score = input()
        score.append(float(input()))

    z = sorted(score) #, reverse = True)
    #print(z)
    z = z[2]
    #print(name, type(name))   
        
    x = dict(zip(name, score))'''
    #print(x)
    #score = list(score)
        
    #score.sort(reverse = True)
    #z = score[1]
    #print(type(name), type(score))
    #print(x)'''

    #s = [key for key,val in x.items() if val is z]
    '''res = []
    res.append(key for key,val in x.items() if val is z)
    for i in res:
        print(res)'''

    '''y = list(x.keys())[list(x.values()).index(37.21)] 
    print(y)'''

    '''y = [name for name, age in x.items() if age == z]
    y = y[::-1]
    for x in y:
        print(x)'''


    '''for x,y in x.items():
        if x[y] is z:
            print(x)'''