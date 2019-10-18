
#autor: Thiago


# entrada do numero de habitantes

compra= []
venda = []
entrada = []


while True:

    N = int(input())
    if N == 0:
        exit()

    entrada = input().split()

    for i in range(len(entrada)):
        entrada[i] = int(entrada[i])

    # print (entrada)

    cv = 0
    trab = 0

    for x in range(len(entrada)-1):
        if (x == 0):
            cv += entrada[x]
            trab += abs(entrada[x])
        else:
            cv += entrada[x]
            trab += abs(cv)

    print (trab)
