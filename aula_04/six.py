
#author: Thiago
main_str = str()
main_str = input()
# print(len(main_str))

n = int(input())

x = 1
ldif = []

while x<=5:

    str1 = str()
    str1 = input()
    dif = 0

    for i in range (len(main_str)):

        if (main_str[i] != str1 [i]):
            # print(main_str[i], str1[i])
            dif= dif +1
    # print(dif)
    ldif.insert(x-1,dif)
    x+=1

menor = ldif[0]
ind = 0
#revisar
for j in range (len(ldif)-1):

    if menor > ldif[j]:
        menor = ldif[j]
        # print (menor)
        ind = j
        # print(ind)

if menor > n:
    print ("-1")
    exit()
else:
    print(ind+1)
    print(menor)
