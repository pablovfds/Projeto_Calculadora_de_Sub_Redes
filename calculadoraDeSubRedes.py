__author__ = 'PabloVictor'

#coding: utf-8

import math

def leituraDoEnderecoIP():
    erroNaEntradaDeDados = True

    while erroNaEntradaDeDados:
        erroNaEntradaDeDados=False
        try:
            enderecoIP = raw_input('Insira o endereco IP: ')

            enderecoIPAux = enderecoIP.split(".")

            if(len(enderecoIPAux) != 4):
                print "Endereco IP invalido."
            else:
                for parteDoIP in enderecoIPAux:
                    if int(parteDoIP) > 192 or int(parteDoIP) < 0:
                        erroNaEntradaDeDados=True

                if(erroNaEntradaDeDados):
                    print "Endereco IP invalido."
        except ValueError:
            erroNaEntradaDeDados = True
            print("Endereco IP invalido.")

    return enderecoIP

def leituraDoNumeroDeSubRedes(mascaraOriginal):
    erroNaEntradaDeDados = True

    numeroMaximoDeSubRedes = math.pow(2,32 - mascaraOriginal ) #calcula o numero maximo de sub redes disponiveis

    while erroNaEntradaDeDados:
        erroNaEntradaDeDados = False
        try:
            numeroDeSubRedes = int(raw_input("Insira o numero de sub-redes: "))

            if(numeroDeSubRedes < 0 or numeroDeSubRedes > numeroMaximoDeSubRedes):
                erroNaEntradaDeDados = True
                print "Numero de sub-redes invalido."
        except ValueError:
            erroNaEntradaDeDados = True
            print "Numero de sub-redes invalido."

    return numeroDeSubRedes

def leituraDaMascaraOriginal():
    erronaentradadedados = True

    while erronaentradadedados:
        erronaentradadedados=False
        try:
            mascaraOriginal = int(raw_input('Insira a mascara original da rede: '))

            if(mascaraOriginal >= 30  and mascaraOriginal < 8):
                erronaentradadedados = True
                print("Mascara invalida.Digite uma nova mascara.")
        except ValueError:
            erronaentradadedados = True
            print("Mascara invalida.Digite uma nova mascara.")

    return mascaraOriginal

def verificaClasseDoEnderecoIP(enderecoIPOriginal):
    msgResposta = ""

    lista = enderecoIPOriginal.split(".")

    if(int(lista[0]) < 128 and int(lista[0]) >= 10): msgResposta = "A"
    elif(int(lista[0]) < 192 and int(lista[0]) > 127): msgResposta = "B"
    elif(int(lista[0]) < 224 and int(lista[0]) > 191): msgResposta = "C"

    return msgResposta

def verificaRedePrivada(enderecoIP):
    enderecoIPLista = enderecoIP.split(".")
    if (int(enderecoIPLista[0]) == 10) or (int(enderecoIPLista[0]) == 172 and int(enderecoIPLista[1]) >= 16 and int(enderecoIPLista[1]) <= 31) or (int(enderecoIPLista[0]) == 192 and int(enderecoIPLista[1]) >= 168):
        msgResposta = "pertence"
    else: msgResposta = "nao pertence"
    return msgResposta

def calculaNovaMascara(numeroDeSubRedes, mascaraOriginal): return (calculaQuantidadeDeBits(numeroDeSubRedes) + int(mascaraOriginal))

def calculaQuantidadeDeBits(numeroDeSubRedes): return int(math.ceil(math.log(numeroDeSubRedes)/math.log(2)))

def transformaEnderecoIpParaBinario(enderecoIP):
    listaBinariaDoEnderecoIP = []

    for parteDoIP in enderecoIP.split("."):
        octetoAux = bin(int(parteDoIP))[2:]
        octetoAux = (8-len(octetoAux))*"0" + octetoAux
        listaBinariaDoEnderecoIP.append(octetoAux)

    return "".join(listaBinariaDoEnderecoIP)

def calculaNovoOctetoEmBinario(posicaoDoOcteto, enderecoIP):
    listaBinariaDoEnderecoIP = transformaEnderecoIpParaBinario(enderecoIP)
    numeroDeBits = calculaQuantidadeDeBits(numeroDeSubRedes)
    listaBinariaDoEnderecoIPNovoOcteto = []

    for octeto in range(numeroDeSubRedes):
        novoOcteto = bin(octeto)[2:] + listaBinariaDoEnderecoIP[posicaoDoOcteto][numeroDeBits:]
        novoOcteto = (8-len(novoOcteto))*"0" + novoOcteto
        listaBinariaDoEnderecoIPNovoOcteto.append(novoOcteto)

    return listaBinariaDoEnderecoIPNovoOcteto

def transformaParaFormaIp(listaIP):
    listaIPAux = []
    num = 0
    for s in range(4):
        listaIPAux.append(str(int(listaIP[num:num+8], 2)))
        num+=8

    return ".".join(listaIPAux)

def transformaBinarioEmDecimal(ipBinario):
    return str(int(ipBinario, 2))

def calculaSubRedes(enderecoIPOriginal, mascaraOriginal, numeroDeSubRedes):
    binarioDoIP = transformaEnderecoIpParaBinario(enderecoIPOriginal)
    ipOriginal = binarioDoIP[:mascaraOriginal]

    print("Endereco IP         - Forma Binaria                    - Forma Decimal")
    for i in range(numeroDeSubRedes):
        a = (calculaQuantidadeDeBits(numeroDeSubRedes)-len(bin(i)[2:]))*"0" + bin(i)[2:]

        ipR = ipOriginal + a + (32-(len(ipOriginal)+len(a)))*"0"
        ipB = ipOriginal + a + (32-(len(ipOriginal)+len(a)))*"1"
        print(str(i+1) + " - Sub rede")
        print("Inicial: " + transformaParaFormaIp(ipR) + " - " + ipR + " - " + transformaBinarioEmDecimal(ipR))
        print("Final: " + transformaParaFormaIp(ipB) + " - " + ipB + " - " + transformaBinarioEmDecimal(ipB))

#-------Main--------

enderecoIPOriginal = leituraDoEnderecoIP()
mascaraOriginal = leituraDaMascaraOriginal()
numeroDeSubRedes = leituraDoNumeroDeSubRedes(mascaraOriginal)

calculaSubRedes(enderecoIPOriginal, mascaraOriginal, numeroDeSubRedes)