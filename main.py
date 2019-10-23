# -*- coding: utf-8 -*-

"""
iMC - É uma ferramenta para cálculo do indice de massa corporal (IMC). O IMC pode ajudar a 
identificar obesidade ou desnutrição em crianças, adolescentes, adultos e idosos.

Requisitos e orientações para resolução dessa tarefa encontram-se na wiki do projeto: 
_Wiki: https://github.com/alexaquino/IINELS-PES-001/wiki.

:Authors: Alex Aquino, Bruno Spinelli, Pablo Queiroz, Rodrigo Henrique
:Version: 2.0.0
:License: MIT
"""

# imports
import imc


# Métodos

def exibir_cabecalho_resultado_formatado(titulo_cabecalho):
    """Exibe na tela o cabeçalho da exibição do resultado formatado
        :param titulo_cabecalho: título a ser exibido no cabeçalho
        :type titulo_cabecalho: str
    """    
    print("\n")
    print("---------------------------------------------------------------------------------")
    print("  > {} " .format(titulo_cabecalho)                                                )
    print("---------------------------------------------------------------------------------")


def exibir_resultado_formatado(indice_massa_corporal, enquadramento_imc):
    """Exibe na tela o cabeçalho da tabela de exibição do resultado 
        :param indice_massa_corporal: indice de massa corporal do indivíduo
        :type indice_massa_corporal: float
        :param enquadramento_imc: enquadramento do indivíduo na escala IMC
        :type enquadramento_imc: str
    """   
    print("---------------------------------------------------------------------------------")
    print("  = IMC -------------->  {0:.2f} " .format(indice_massa_corporal)                 )
    print("  = ENQUADRAMENTO ---->  {} " .format(enquadramento_imc)                          )                                                   
    print("---------------------------------------------------------------------------------")
    print("\n")
    

def verificar_enquadramento_imc():
    """Verifica e retorna enquadramento do indivíduo na escala IMC
        :return enquadramento_imc: enquadramento do indivíduo na escala IMC
        :rtype: str
    """   
    if is_muito_abaixo_peso: 
        enquadramento_imc = "MUITO ABAIXO DO PESO"
    elif is_abaixo_peso: 
        enquadramento_imc = "ABAIXO DO PESO"
    elif is_peso_normal: 
        enquadramento_imc = "PESO NORMAL"
    elif is_acima_peso: 
        enquadramento_imc = "ACIMA DO PESO"
    else: 
        enquadramento_imc = "MUITO ACIMA DO PESO"   
    
    return enquadramento_imc


# Entrada/Saída de dados

exibir_cabecalho_resultado_formatado("iMC - Enquadramento na Escala do Índice de Massa Coporal")

peso_quilos = float(input("  + Informe o peso em quilos   (Ex.: 70.5): "))
altura_metros = float(input("  + Informe a altura em metros (Ex.: 1.85): "))

indice_massa_corporal = imc.calcular_indice_massa_corporal(peso_quilos, altura_metros)
is_muito_abaixo_peso = imc.is_muito_abaixo_peso(indice_massa_corporal)
is_abaixo_peso = imc.is_abaixo_peso(indice_massa_corporal)
is_peso_normal = imc.is_peso_normal(indice_massa_corporal)
is_acima_peso = imc.is_acima_peso(indice_massa_corporal)
isMuitoAcimaPeso = imc.is_muito_acima_peso(indice_massa_corporal)
enquadramento_imc = verificar_enquadramento_imc()

exibir_resultado_formatado(indice_massa_corporal, enquadramento_imc)