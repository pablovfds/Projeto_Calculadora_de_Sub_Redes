__author__ = 'PabloVictor'
#coding: utf-8

import math
import random

def leituraDoEnderecoIP():
    erro = True

    while erro:
        erro=False
        try:
            enderecoIP = raw_input('Insira o endereco IP(Ex: 192.167.0.23): ')

            enderecoIPAux = enderecoIP.split(".")

            if(len(enderecoIPAux) != 4):
                print "Endereco IP invalido."
            else:
                for parteDoIP in enderecoIPAux:
                    if int(parteDoIP) > 192 or int(parteDoIP) < 0:
                        erro=True
                        print "Endereco IP invalido."
        except ValueError:
            erro = True
            print("Endereco IP invalido.")

    return enderecoIP

def leituraDoNumeroDeSubRedes(mascaraOriginal):
    erro = True

    numeroMaximoDeSubRedes = math.pow(2,32 - mascaraOriginal )

    while erro:
        erro = False
        try:
            numeroDeSubRedes = int(raw_input("Insira o numero de sub-redes(Ex: 4): "))

            if(numeroDeSubRedes < 0 or numeroDeSubRedes > numeroMaximoDeSubRedes):
                erro = True
                print "Numero de sub-redes invalido."
        except ValueError:
            erro = True
            print "Numero de sub-redes invalido."

    return numeroDeSubRedes

def leituraDaMascaraOriginal():
    erro = True

    while erro:
        erro=False
        try:
            mascaraOriginal = raw_input('Insira a mascara original da rede (Ex: 255.255.255.0): ')
            listaMascara = mascaraOriginal.split(".")

            if(len(listaMascara) != 4):
                erro = True
                print("Mascara invalida.Digite uma nova mascara.")

            mascaraOriginalAux = ""
            for index in range(len(listaMascara)):
                if(int(listaMascara[index]) > 255 or int(listaMascara[index]) < 0):
                    erro = True
                    print("Mascara invalida.Digite uma nova mascara.")
                elif (index > 0):
                    if (int(listaMascara[index]) > int(listaMascara[index-1]) or int(listaMascara[index-1] < 255)):
                        erro = True
                        print("Mascara invalida.Digite uma nova mascara.")

                binarioAux = (bin(int(listaMascara[index])))[2:]
                mascaraOriginalAux += ((8-len(binarioAux))*"0") + binarioAux

            numeroDeMascara = 0
            for index in range(32):
                if(mascaraOriginalAux[index] == "1"):
                    numeroDeMascara+=1

        except ValueError:
            erro = True
            print("Mascara invalida.Digite uma nova mascara.")

    return numeroDeMascara

def verificaClasseDoEnderecoIP(enderecoIPOriginal):
    lista = enderecoIPOriginal.split(".")

    if(int(lista[0]) < 128 and int(lista[0]) >= 10): print("A classe do endereço IP "+enderecoIPOriginal+ ": A")
    elif(int(lista[0]) < 192 and int(lista[0]) > 127): print("A classe do endereço IP "+enderecoIPOriginal+ ": B")
    elif(int(lista[0]) < 224 and int(lista[0]) > 191): print("A classe do endereço IP "+enderecoIPOriginal+ ": C")

def verificaRedePrivada(enderecoIP):
    enderecoIPLista = enderecoIP.split(".")
    if (int(enderecoIPLista[0]) == 10) or (int(enderecoIPLista[0]) == 172 and int(enderecoIPLista[1]) >= 16 and int(enderecoIPLista[1]) <= 31) or (int(enderecoIPLista[0]) == 192 and int(enderecoIPLista[1]) >= 168):
        print("O endereço IP "+enderecoIP+" é uma rede privada: sim")
    else: print("O endereço IP "+enderecoIP+" é uma rede privada: não")

def calculaNovaMascara(numeroDeSubRedes, mascaraOriginal):
    novaMascara = calculaQuantidadeDeBits(numeroDeSubRedes) + int(mascaraOriginal)
    binarioDeNovaMascara = transformaParaFormaIp("1"*novaMascara + (32-novaMascara)*"0")
    return (binarioDeNovaMascara + "/"+str(novaMascara))

def calculaQuantidadeDeBits(numeroDeSubRedes): return int(math.ceil(math.log(numeroDeSubRedes)/math.log(2)))

def transformaEnderecoParaBinario(endereco):
    listaBinariaDoEnderecoIP = []

    for parteDoIP in endereco.split("."):
        octetoAux = bin(int(parteDoIP))[2:]
        octetoAux = (8-len(octetoAux))*"0" + octetoAux
        listaBinariaDoEnderecoIP.append(octetoAux)

    return "".join(listaBinariaDoEnderecoIP)

def transformaParaFormaIp(listaIP):
    listaIPAux = []
    num = 0
    for s in range(4):
        listaIPAux.append(str(int(listaIP[num:num+8], 2)))
        num+=8

    return ".".join(listaIPAux)

def transformaBinarioEmDecimal(ipBinario): return str(int(ipBinario, 2))

def calculaSubRedes(enderecoIPOriginal, mascaraOriginal, numeroDeSubRedes):
    binarioDoIP = transformaEnderecoParaBinario(enderecoIPOriginal)
    ipOriginal = binarioDoIP[:mascaraOriginal]
    listaDeIpDeRede = []

    formatacao = '{0:10s} {1:10s} {2:20s} {3:39s} {4:15s}'
    formatacaoTitulo = '{0:10s} {1:10s} {2:21s} {3:39s} {4:15s}'
    print(formatacaoTitulo.format("","Sub Rede", "Endereço IP", "Forma Binaria", "Forma Decimal"))
    for i in range(numeroDeSubRedes):
        aux = (calculaQuantidadeDeBits(numeroDeSubRedes)-len(bin(i)[2:]))*"0" + bin(i)[2:]

        ipR = ipOriginal + aux + (32-(len(ipOriginal)+len(aux)))*"0"
        ipB = ipOriginal + aux + (32-(len(ipOriginal)+len(aux)))*"1"
        formaIPRede = transformaParaFormaIp(ipR)
        formaIPBroadCast = transformaParaFormaIp(ipB)
        listaDeIpDeRede.append(formaIPRede)
        subRede = str(i+1)
        print(formatacao.format("Inicial",subRede, formaIPRede, ipR, transformaBinarioEmDecimal(ipR)))
        print(formatacao.format("Final",subRede, formaIPBroadCast, ipB, transformaBinarioEmDecimal(ipB)))



    calculaRotas(listaDeIpDeRede, numeroDeSubRedes, mascaraOriginal)

def calculaRotas(listaDeIpDeRede, numeroDeSubRedes, mascaraOriginal):
    print

    formatacao = '{0:16s} {1:16s} {2:19s} {3:7s} {4:10s}'
    formatacaoTitulo = '{0:16s} {1:16s} {2:19s} {3:7s} {4:10s}'

    print(formatacaoTitulo.format("Destinion", "Gateway", "Mascara", "Option", "Interface"))
    for index in range(len(listaDeIpDeRede)):
        ipRedeAtual = listaDeIpDeRede[index][:-1] + str (int(listaDeIpDeRede[index][-1])+1)
        novaMascara = calculaNovaMascara(numeroDeSubRedes, mascaraOriginal)
        if index == 0:
            print(formatacao.format("0.0.0.0", ipRedeAtual, "0.0.0.0", "UG", "ETH"+str(index)))
            print(formatacao.format(listaDeIpDeRede[index], "0.0.0.0", novaMascara, "U", "ETH"+str(index)))
        else:
            print(formatacao.format(listaDeIpDeRede[index], ipRedeAtual, novaMascara, "U", "ETH"+str(index)))
#-------Main--------

enderecoIPOriginal = leituraDoEnderecoIP()
mascaraOriginal = leituraDaMascaraOriginal()
numeroDeSubRedes = leituraDoNumeroDeSubRedes(mascaraOriginal)

verificaClasseDoEnderecoIP(enderecoIPOriginal)
verificaRedePrivada(enderecoIPOriginal)
print("Nova mascara: " + calculaNovaMascara(numeroDeSubRedes, mascaraOriginal))
print
calculaSubRedes(enderecoIPOriginal, mascaraOriginal, numeroDeSubRedes)