# Type casting

'''
1. Implicit: done by Compiler
2. Explicit: done by programmer using build-in function.

'''

#Example 1 of implicit type casting

a = 10
print(a,type(a))
b = 5
print(b,type(b))
result = a/b
print(result, type(result)) # float

# whenever we are performing division opration the reslut will always be in float data type

#----------------------------------------------------------------

#Example 1 of implicit type casting

x = input('enter a number')
print(x,type(x)) # str

# All the types of value that enter into user input() is getting converted inti 'str' internally

#-----------------------------------------------------------------