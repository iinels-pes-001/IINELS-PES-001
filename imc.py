"""
# -*- coding: utf-8 -*-

Esse módulo implementa os métodos necessários para o calcular o indice de massa corporal (IMC) e fornecer 
a classificação do indivíduo dentro da escala que determina o nível de obesidade. o IMC, pode ajudar a 
identificar obesidade ou desnutrição em crianças, adolescentes, adultos e idosos.

Requisitos e orientações para resolução desse problema encontram-se na wiki do projeto: 
_Wiki: https://github.com/alexaquino/IINELS-PES-001/wiki.

:Authors: Alex Aquino, Bruno Spinelli, Pablo Queiroz, Rodrigo Henrique
:Version: 2.0.0
:License: MIT
"""

# Métodos 

def calcularIndiceMassaCorporal(__pesoQuilos, __alturaMetros):
    """Realiza o cálculo do índice de massa corporal (IMC)
        :param __pesoQuilos: peso do indivíduo em quilos
        :type __pesoQuilos: float
        :param __alturaMetros: altura do indivíduo metros
        :type __alturaMetros: float
        :return __indiceMassaCorporal: índice de massa corporal (IMC)
        :rtype: float
    """
    __indiceMassaCorporal = (__pesoQuilos / (__alturaMetros ** 2)) 
    return __indiceMassaCorporal


def isMuitoAbaixoPeso(__indiceMassaCorporal):
    """Verifica se o indivíduo está muito abaixo do peso ideal
        :param __indiceMassaCorporal: indice de massa corporal do indivíduo
        :type __indiceMassaCorporal: float
        :return __isMuitoAbaixoPeso: True ou False para IMC < 17
        :rtype: bool
    """
    __isMuitoAbaixoPeso = (__indiceMassaCorporal < 17)
    return __isMuitoAbaixoPeso


def isAbaixoPeso(__indiceMassaCorporal):
    """Verifica se o indivíduo está abaixo do peso ideal
        :param __indiceMassaCorporal: indice de massa corporal do indivíduo
        :type __indiceMassaCorporal: float
        :return __isAbaixoPeso: True ou False para IMC >= 17 e IMC <= 18.5
        :rtype: bool
    """
    __isAbaixoPeso = (__indiceMassaCorporal >= 17 and __indiceMassaCorporal <= 18.5)
    return __isAbaixoPeso


def isPesoNormal(__indiceMassaCorporal):
    """Verifica se o indivíduo está com o peso ideal
        :param __indiceMassaCorporal: indice de massa corporal do indivíduo
        :type __indiceMassaCorporal: float
        :return __isPesoNormal: True ou False para IMC >= 18.5 e IMC <= 25
        :rtype: bool
    """
    __isPesoNormal = (__indiceMassaCorporal >= 18.5 and __indiceMassaCorporal <= 25)
    return __isPesoNormal
  
  
def isAcimaPeso(__indiceMassaCorporal):
    """Verifica se o indivíduo está acima do peso ideal
        :param indiceMassaCorporal: indice de massa corporal do indivíduo
        :type indiceMassaCorporal: float
        :return isAcimaPeso: True ou False para IMC >= 25 e IMC <= 30
        :rtype: bool
    """
    __isAcimaPeso = (__indiceMassaCorporal >= 25 and __indiceMassaCorporal <= 30)
    return __isAcimaPeso


def isMuitoAcimaPeso(__indiceMassaCorporal):
    """Verifica se o indivíduo está muito acima do peso ideal
        :param __indiceMassaCorporal: indice de massa corporal do indivíduo
        :type __indiceMassaCorporal: float
        :return isMuitoAcimaPeso: True ou False para IMC > 30
        :rtype: bool
    """
    __isMuitoAcimaPeso = (__indiceMassaCorporal > 30)
    return __isMuitoAcimaPeso


def exibirCabecalhoResultadoFormatado(__tituloCabelaho):
    """Exibe na tela o cabeçalho da exibição do resultado formatado
        :param __tituloCabelaho: título a ser exibido no cabeçalho
        :type __tituloCabelaho: str
    """    
    print("-------------------------------------------------------------------------------------------")
    print("%s " %(__tituloCabelaho)                                                                    )
    print("-------------------------------------------------------------------------------------------")


def exibirResultadoFormatado(__indiceMassaCorporal):
    print("-------------------------------------------------------------------------------------------")
    print("  - Está muito abaixo do peso ideal? ----> %r" %(isMuitoAbaixoPeso(__indiceMassaCorporal)))
    print("  - Está abaixo do peso ideal? ----------> %r" %(isAbaixoPeso(__indiceMassaCorporal)))
    print("  - Está com o peso ideal? --------------> %r" %(isPesoNormal(__indiceMassaCorporal)))
    print("  - Está acima do peso ideal? -----------> %r" %(isAcimaPeso(__indiceMassaCorporal)))
    print("  - Está muito acima do peso ideal? -----> %r" %(isMuitoAcimaPeso(__indiceMassaCorporal)))
    print("-------------------------------------------------------------------------------------------")
    print("\n")


def exibirAnalise(__indiceMassaCorporal):
    """Exibe na tela o resultado da análise de classificação do IMC
        :param __indiceMassaCorporal: indice de massa corporal do indivíduo
        :type __indiceMassaCorporal: float
    """
    print("-------------------------------------------------------------------------------------------")
    if (isAcimaPeso(__indiceMassaCorporal)):
        print("  - Está acima do peso ideal.")
    elif (isMuitoAcimaPeso(__indiceMassaCorporal)):
        print("  - Está muito acima do peso ideal.")
    elif (isMuitoAbaixoPeso(__indiceMassaCorporal)):
        print("  - Está muito abaixo do peso ideal.")
    elif (isAbaixoPeso(__indiceMassaCorporal)):
        print("  - Está abaixo do peso ideal.")
    else:
        print("  - Está com o peso ideal.")
