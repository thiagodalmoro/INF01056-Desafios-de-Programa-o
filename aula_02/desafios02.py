#
#
# Author: Thiago Dal Moro

cont = 0

while True:

    entrada = (input()).split()
    # print (entrada)

    # #quantos motoristas
    n_drive = int (entrada[0])
    # print (n_drive)
    # #parking fit
    k_car= int (entrada[-1])
    # print (k_car)


    cont+=1


    if not (n_drive >= 3 and n_drive <= 10**4):
        for x in range (cont-1):
            print (saida[x])

        exit()

    else: #se for dentro da faixa

        p_chegada = []
        p_saida = []
        p_temp = []
        saida = []

        for i in range (n_drive):
        #pilha de chegada e pilha de saida

            entrada = (input()).split()
            # print (entrada)

            # #quantos motoristas
            c = int (entrada[0])
            s = int (entrada[-1])


    # # Controle da lista de chegada
    #         #insere elemento na lista chegada // tempo chegada
            if not p_chegada:
                #list is empty
                p_chegada.append(c)
                # print ('a lista tava vazia chegada')
    #
            elif c > p_chegada[-1]:
                # ci+1 > ci
                p_chegada.append(c)
                # print (p_chegada[-1])
                # print ('inserido na lista chegada com sucesso')

    # # Controle da lista de saida
    #
            if not p_saida:
                #list is empty
                p_saida.append(s)
                # print ('a lista saida tava vazia')

            elif s < p_saida[-1]:
                # print ('a lista saida ja tinha elementos')
                #passa no testes
                #o Si+1 tem tempo de saida menor que o primeiro

                #adiciona o item correto em uma lista alternativa
                p_temp.append(s)
                saida.append('Sim')

            else:

                # S eh maior que o ultimo item (S > p_saida) // condicao errada // tem que dar nao
                #condiçao de quebra ... não passa no teste
                #si+1 tem tempo maior que o primeiro

                p_saida.append(s)
                saida.append('Nao')
                #adiciona o s (que nao pode) na pilha temp.
