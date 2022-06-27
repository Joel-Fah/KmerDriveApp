# Imports

# Take number of cases from user
try:
    T = int(input('Enter the number of cases: '))
    while T <= 0 or T > 100:
        print('Number of cases must be a positive integer')
        T = int(input('Re-enter the number of cases >>> '))
except ValueError:
    T = int(input('Enter a positive number of cases: '))
    while T <= 0 or T > 100:
        print('Number of cases must be a positive integer')
        T = int(input('Enter an integer >>> '))
        

# Dynamically create lists
cases = [[] for i in range(T)]

# for D in cases:
#     length = int(input('Enter the number of elements for case ' + str(cases.index(D)+1) + ' >>> '))
#     max_z = length - 2
#     while length < 2 or length > 8:
#         length = int(input('Enter a number between 2 and 8 inclusive for case ' + str(cases.index(D)+1) + ' >>> '))
#     max_z = length - 2
#     for i in range(length):
#         x = int(input('Enter element ' + str(i+1) + ' of case ' + str(cases.index(D)+1) + ' >>> '))
#         if x == 0 and max_z != 0:
#             D.append(x)
#             max_z -= 1
#         elif x == 0 and max_z == 0:
#             x = int(input('Re-nter element ' + str(i+1) + ' of case ' + str(cases.index(D)+1) + ' different from 0 >>> '))
#             while x == 0:
#                 x = int(input('Re-enter element ' + str(i+1) + ' of case ' + str(cases.index(D)+1) + ' different from 0 >>> '))
#             D.append(x)
#         else:
#             D.append(x)
        

liste = [[1,2,3], [5,6,7,8,9], [0,0,1,1]]