```
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```

if __name__ == '__main__':
    
    arr = []
    
    for i in range(int(input())):
        s = input().split()
        for i in range(1, len(s)):
            s[i] = int(s[i])
            
        if s[0] == "append":
            arr.append(s[1])
        elif s[0] == "extend":    
            arr.extend(s[1:])
        elif s[0] == "insert":
            arr.insert(s[1],s[2])
        elif s[0] == "remove":
            arr.remove(s[1])
        elif s[0] == "pop":
            arr.pop()
        elif s[0] == "index":
            print(arr.index(s[1]))
        elif s[0] == "count":
            print(arr.count(s[1]))
        elif s[0] == "sort":
            arr.sort()
        elif s[0] == "reverse":
            arr.reverse()
        elif s[0] == "print":
            print(arr)