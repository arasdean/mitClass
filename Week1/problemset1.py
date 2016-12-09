'''Problem 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained
in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
 For example, if s = 'azcbobobegghakl', your program should print:

 Number of vowels: 5

 '''
s = 'azcbobobegghakl'
vowels = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels += 1
print('Number of vowels: %d' % (vowels))

#
#
#
'''
Problem 2
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2 '''
#use for loop to find in
#use regex lol
#
bob_count = 0
s = 'azcbobobegghakl'
for i in range(len(s)-2):
    if s[i] == 'b' and s[i+1] == 'o' and s[i + 2] == 'b':
        bob_count += 1
print(bob_count) 
