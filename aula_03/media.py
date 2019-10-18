#
# Author: Thiago Dal Moro

entrada = (input()).split()
print (entrada)

# #quantos motoristas
n = int (entrada[0])
print (n)
# #parking fit
k= int (entrada[-1])
print (k)


notas = input().split()

for i in range (len(notas)):
    notas[i] = int(notas[i])

print(notas)

media = []
soma = 0
key = 0


tam = len(notas)-1

for i in range (len(notas)-1):
    if (i == 0):
        soma += notas[i]
        media.append(soma)



print (media)
print (soma)


    # for j in range (k-2):
    #     if (j == 1):
    #         key2 = notas[j]
    #         soma += notas [j]
    #         media[j] = soma /3
    #
    #     for x in range (k-2):
    #
    #         if (x==0):
    #             key = notas[k]
    #         if (x == 2):
    #             soma += notas[k]
    #             media [x] = (soma + key) /3
    #
    #         else:
    #             soma = (notas[-1] + key + key2)
    #             media [k+1] = soma /3
