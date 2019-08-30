#
#
# Author: Thiago Dal Moro

# def main ():
    #N number os trips
# N = int(input("Enter number of Trips GotoMarket: "))
N = int(input())
# print  (N)

for j in range (N):
    M = {}

    # N_product = int(input("Enter number of procuts: "))
    N_product = int(input())
    # print  (N_product)

    for i in range(N_product):
        prt = (input()).split()
        vlr = float(prt[-1])
        name = prt[:-1]
        name = " ".join(name)

        #add dict
        M[name]= vlr

        # print(name, vlr)

    # print (M)


    # N_buy = int(input("Enter number of itens: "))
    N_buy = int(input())
    # print  (N_buy)

    valort = 0

#compra aqui

    for i in range(N_buy):
        prt = (input()).split()
        quant = int(prt[-1])
        name = prt[:-1]
        name = " ".join(name)

#acumula para calcular o valor

        if name in M.keys():
            valort+= M[name]*quant

    print ("R$ {:.2f}".format(valort))
