# -*- coding: utf-8 -*-


#author: Thiago
main_str = str()
main_str = input()
print(len(main_str))
print (main_str)


str1 = str()
str1 = input()
print (str1)

equal = []

for i in range (len(main_str)):
    for j in range (len (str1)):

        if (main_str[i] == str1[j]):
            equal.append(1)
            print(main_str[i], str1[j])
        else:
            equal.append(0)

    print(equal, end=' ')

print (equal)




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
