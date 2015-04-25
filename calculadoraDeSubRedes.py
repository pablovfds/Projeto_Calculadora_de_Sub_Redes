__author__ = 'PabloVictor'
#coding: utf-8
import math
# Leitura do endereço ip
def leituraDoEnderecoIP():
    erro = True
    while erro:
        erro=False
        try:
            enderecoIP = raw_input('Insira o endereco IP (Ex: 192.167.0.23): ')
            enderecoIPAux = enderecoIP.split(".")
            if(len(enderecoIPAux) != 4):
                erro = True
                print ("Endereço IP invalido.")
            else:
                for parteDoIP in enderecoIPAux:
                    if int(parteDoIP) > 255 or int(parteDoIP) < 0:
                        erro=True
                        print ("Endereço IP invalido.")
        except ValueError:
            erro = True
            print("Endereço IP invalido.")

    return enderecoIP
# Leitura do numero de sub redes
def leituraDoNumeroDeSubRedes(mascaraOriginal):
    erro = True
    numeroMaximoDeSubRedes = math.pow(2,32 - mascaraOriginal )
    while erro:
        erro = False
        try:
            numeroDeSubRedes = int(raw_input("Insira o numero de sub-redes(Ex: 4): "))
            if(numeroDeSubRedes < 0 or numeroDeSubRedes > numeroMaximoDeSubRedes):
                erro = True
                print ("Numero de sub-redes invalido.")
        except ValueError:
            erro = True
            print ("Numero de sub-redes invalido.")
    return numeroDeSubRedes
# leitura da mascara original
def leituraDaMascaraOriginal():
    erro = True
    while erro:
        erro=False
        try:
            mascaraOriginal = raw_input('Insira a mascara original da rede (Ex: 255.255.255.0): ')
            listaMascara = mascaraOriginal.split(".")
            if(len(listaMascara) != 4):
                erro = True
            mascaraOriginalAux = ""
            for index in range(len(listaMascara)):
                if(int(listaMascara[index]) > 255 or int(listaMascara[index]) < 0):
                    erro = True
                elif (index > 0):
                    if (int(listaMascara[index]) > int(listaMascara[index-1]) or int(listaMascara[index-1] < 255)):
                        erro = True
                mascaraOriginalAux += ((8-len((bin(int(listaMascara[index])))[2:]))*"0") + (bin(int(listaMascara[index])))[2:]
            if(erro):
                print("Mascara invalida.Digite uma nova mascara.")
            else:
                numeroDeMascara = 0
                for index in range(32):
                    if(mascaraOriginalAux[index] == "1"):
                        numeroDeMascara+=1
        except ValueError:
            print("Mascara invalida.Digite uma nova mascara.")
            erro = True
    return numeroDeMascara
# Verifica a classe do endereço ip
def verificaClasseDoEnderecoIP(enderecoIPOriginal):
    lista = enderecoIPOriginal.split(".")
    if(int(lista[0]) <= 127 and int(lista[0]) >= 1): print("A classe do endereço IP "+enderecoIPOriginal+ ": A")
    elif(int(lista[0]) <= 191 and int(lista[0]) >= 128): print("A classe do endereço IP "+enderecoIPOriginal+ ": B")
    elif(int(lista[0]) <= 223 and int(lista[0]) >= 192): print("A classe do endereço IP "+enderecoIPOriginal+ ": C")
    elif(int(lista[0]) <= 239 and int(lista[0]) >= 224): print("A classe do endereço IP "+enderecoIPOriginal+ ": D")
    elif(int(lista[0]) <= 255 and int(lista[0]) >= 240): print("A classe do endereço IP "+enderecoIPOriginal+ ": E")
# Verifica se o endereço ip pertence a uma rede privada
def verificaRedePrivada(enderecoIP):
    enderecoIPLista = enderecoIP.split(".")
    if (int(enderecoIPLista[0]) == 10) or (int(enderecoIPLista[0]) == 172 and int(enderecoIPLista[1]) >= 16
        and int(enderecoIPLista[1]) <= 31) or (int(enderecoIPLista[0]) == 192 and int(enderecoIPLista[1]) >= 168):
        print("O endereço IP "+enderecoIP+" é uma rede privada: Sim")
    else: print("O endereço IP "+enderecoIP+" é uma rede privada: Não")
# Calcula a nova mascara
def calculaNovaMascara(numeroDeSubRedes, mascaraOriginal):
    novaMascara = calculaQuantidadeDeBits(numeroDeSubRedes) + int(mascaraOriginal)
    return (transformaParaFormaIp("1"*novaMascara + (32-novaMascara)*"0") + "/"+str(novaMascara))
# Calcula a nova mascara na forma decimal
def calculaNovaMascaraDecimal(numeroDeSubRedes, mascaraOriginal):
    novaMascara = calculaQuantidadeDeBits(numeroDeSubRedes) + int(mascaraOriginal)
    print ("Nova mascara: " + calculaNovaMascara(numeroDeSubRedes, mascaraOriginal)
            + " - Forma Decimal: "+str(transformaBinarioEmDecimal("1"*novaMascara + (32-novaMascara)*"0")))
# Calcula a quantidade de bits que serão usados
def calculaQuantidadeDeBits(numeroDeSubRedes): return int(math.ceil(math.log(numeroDeSubRedes)/math.log(2)))
# Transforma endereços que estão definidos em forma de octetos em forma binaria
def transformaEnderecoParaBinario(endereco):
    listaBinariaDoEnderecoIP = []
    for parteDoIP in endereco.split("."):
        octetoAux = (8-len(bin(int(parteDoIP))[2:]))*"0" + bin(int(parteDoIP))[2:]
        listaBinariaDoEnderecoIP.append(octetoAux)
    return "".join(listaBinariaDoEnderecoIP)
# Transforma endereços que estão na forma binaria para forma de octetos
def transformaParaFormaIp(listaIP):
    listaIPAux = []
    num = 0
    for s in range(4):
        listaIPAux.append(str(int(listaIP[num:num+8], 2)))
        num+=8
    return ".".join(listaIPAux)
# Transforma endereços da forma binaria para forma decimal
def transformaBinarioEmDecimal(ipBinario): return str(int(ipBinario, 2))
# Calcula as formações de cadas sub rede
def calculaSubRedes(enderecoIPOriginal, mascaraOriginal, numeroDeSubRedes):
    ipOriginal = transformaEnderecoParaBinario(enderecoIPOriginal)[:mascaraOriginal]
    listaDeIpDeRede = []
    formatacao = '{0:7s} | {1:8s} | {2:14s} | {3:32s} | {4:10s}'
    formatacaoTitulo = '{0:7s} | {1:7s} | {2:15s} | {3:32s} | {4:10s}'
    print ("-"*90)
    print(formatacaoTitulo.format("","Sub Rede", "Endereço IP", "Forma Binaria", "Forma Decimal"))
    for i in range(numeroDeSubRedes):
        aux = (calculaQuantidadeDeBits(numeroDeSubRedes)-len(bin(i)[2:]))*"0" + bin(i)[2:]
        ipR = ipOriginal + aux + (32-(len(ipOriginal)+len(aux)))*"0"
        ipB = ipOriginal + aux + (32-(len(ipOriginal)+len(aux)))*"1"
        listaDeIpDeRede.append(transformaParaFormaIp(ipR))
        print(formatacao.format("Inicial",str(i+1), transformaParaFormaIp(ipR), ipR, transformaBinarioEmDecimal(ipR)))
        print(formatacao.format("Final","", transformaParaFormaIp(ipB), ipB, transformaBinarioEmDecimal(ipB)))
    calculaRotas(listaDeIpDeRede, numeroDeSubRedes, mascaraOriginal)
# Calcula as rotas de cada sub rede
def calculaRotas(listaDeIpDeRede, numeroDeSubRedes, mascaraOriginal):
    print ("-"*90)
    formatacao = '{0:14s} | {1:14s} | {2:18s} | {3:6s} | {4:9s}'
    formatacaoTitulo = '{0:14s} | {1:14s} | {2:18s} | {3:6s} | {4:9s}'
    print(formatacaoTitulo.format("Destination", "Gateway", "Mascara", "Option", "Interface"))
    for index in range(len(listaDeIpDeRede)):
        ipRedeAtual = listaDeIpDeRede[index][:-1] + str (int(listaDeIpDeRede[index][-1])+1)
        novaMascara = calculaNovaMascara(numeroDeSubRedes, mascaraOriginal)
        if index == 0:
            print(formatacao.format("0.0.0.0", ipRedeAtual, "0.0.0.0", "UG", "ETH"+str(index)))
            print(formatacao.format(listaDeIpDeRede[index], "0.0.0.0", novaMascara, "U", "ETH"+str(index)))
        else:
            print(formatacao.format(listaDeIpDeRede[index], ipRedeAtual, novaMascara, "U", "ETH"+str(index)))
#----------------------------------------------------------
#----------------------Main--------------------------------
#----------------------------------------------------------
enderecoIPOriginal = leituraDoEnderecoIP()
mascaraOriginal = leituraDaMascaraOriginal()
numeroDeSubRedes = leituraDoNumeroDeSubRedes(mascaraOriginal)
print ("-"*90)
verificaClasseDoEnderecoIP(enderecoIPOriginal)
verificaRedePrivada(enderecoIPOriginal)
calculaNovaMascaraDecimal(numeroDeSubRedes, mascaraOriginal)
calculaSubRedes(enderecoIPOriginal, mascaraOriginal, numeroDeSubRedes)