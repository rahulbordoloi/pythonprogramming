import re

#verifying an email
pattern="[a-zA-Z0-9]+@[a-zA-Z]+\.(com|in|org)"
print("\nEnter the Email ID:\n")
inp = input()
if(re.search(pattern,inp)):
    print("\nValid ID")
else:
    print("\nInvalid ID")

#removing hyphens
pattern="(\d\d\d)-(\d\d\d)-(\d\d\d\d)"   #set of parenthesis = group
new_pattern=r"\1\2\3"                    #each backslash numbers represents a group, we put r before the string for it to be interpreted as a raw string
inp=input()
new_user_ip=re.sub(pattern, new_pattern, inp)
print(new_user_ip)
