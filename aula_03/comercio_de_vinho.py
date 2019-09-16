
#autor: Thiago


# entrada do numero de habitantes

compra= []
venda = []
entrada = []



N = int(input("Enter number of Habitantes: "))
if N == 0:
    exit()

entrada = (input()).split()
print (entrada)

for x in range (N-1):
        #venda vinhos
    curr = int(entrada[x]) + int(entrada[x+1])
    print (curr)

    print('pos print curr')
    if (int(entrada [x]) > 0):
        compra = entrada[x]
        print (compra)
        print (int(entrada[x]))
