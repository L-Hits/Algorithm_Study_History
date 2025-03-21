str = input()
list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in list:
    str = str.replace(i, ' ')
print(len(str))