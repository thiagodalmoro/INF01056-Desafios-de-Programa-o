# -*- coding: utf-8 -*-

#author: Thiago
main_str = str()
main_str = input()
print (main_str)


str1 = str()
str1 = input()
print (str1)

equal = []
mat = []

for l in range (len(main_str)):
    for c in range (len (str1)):
        if (main_str[l] == str1[c]):
            equal.insert(c,1)
        else:
            equal.insert(c,0)
    print()
    print(equal)

#
# print(f'[{equal}]', end = '')








## print(dif)
#ldif.insert(x-1,dif)
#
#
#
#menor = ldif[0]
#ind = 0
##revisar
#for j in range (len(ldif)-1):
#
#    if menor > ldif[j]:
#        menor = ldif[j]
#        # print (menor)
#        ind = j
#        # print(ind)
#
#if menor > n:
#    print ("-1")
#    exit()
#else:
#    print(ind+1)
#    print(menor)
