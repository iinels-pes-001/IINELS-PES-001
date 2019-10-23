"""
# -*- coding: utf-8 -*-

Esse módulo implementa os métodos necessários para calcular o indice de massa corporal (IMC) do 
indivíduo. O IMC pode ajudar a identificar obesidade ou desnutrição em crianças, adolescentes, 
adultos e idosos.

Requisitos e orientações para resolução desse problema encontram-se na wiki do projeto: 
_Wiki: https://github.com/alexaquino/IINELS-PES-001/wiki.

:Authors: Alex Aquino, Bruno Spinelli, Pablo Queiroz, Rodrigo Henrique
:Version: 2.1.0
:License: MIT
"""

# Métodos 

def calcular_indice_massa_corporal(__peso_quilos, __altura_metros):
    """Realiza o cálculo do índice de massa corporal (IMC)
        :param __peso_quilos: peso do indivíduo em quilos
        :type __peso_quilos: float
        :param __altura_metros: altura do indivíduo metros
        :type __altura_metros: float
        :return __indice_massa_corporal: índice de massa corporal (IMC)
        :rtype: float
    """
    __indice_massa_corporal = (__peso_quilos / (__altura_metros ** 2)) 
    return __indice_massa_corporal


def is_muito_abaixo_peso(__indice_massa_corporal):
    """Verifica se o indivíduo está muito abaixo do peso ideal
        :param __indice_massa_corporal: indice de massa corporal do indivíduo
        :type __indice_massa_corporal: float
        :return __is_muito_abaixo_peso: True ou False para IMC < 17
        :rtype: bool
    """
    __is_muito_abaixo_peso = (__indice_massa_corporal < 17)
    return __is_muito_abaixo_peso


def is_abaixo_peso(__indice_massa_corporal):
    """Verifica se o indivíduo está abaixo do peso ideal
        :param __indice_massa_corporal: indice de massa corporal do indivíduo
        :type __indice_massa_corporal: float
        :return __is_abaixo_peso: True ou False para IMC >= 17 e IMC <= 18.5
        :rtype: bool
    """
    __is_abaixo_peso = (__indice_massa_corporal >= 17 and __indice_massa_corporal < 18.5)
    return __is_abaixo_peso


def is_peso_normal(__indice_massa_corporal):
    """Verifica se o indivíduo está com o peso ideal
        :param __indice_massa_corporal: indice de massa corporal do indivíduo
        :type __indice_massa_corporal: float
        :return __is_peso_normal: True ou False para IMC >= 18.5 e IMC <= 25
        :rtype: bool
    """
    __is_peso_normal = (__indice_massa_corporal >= 18.5 and __indice_massa_corporal < 25)
    return __is_peso_normal
  
  
def is_acima_peso(__indice_massa_corporal):
    """Verifica se o indivíduo está acima do peso ideal
        :param indiceMassaCorporal: indice de massa corporal do indivíduo
        :type indiceMassaCorporal: float
        :return is_acima_peso: True ou False para IMC >= 25 e IMC <= 30
        :rtype: bool
    """
    __is_acima_peso = (__indice_massa_corporal >= 25 and __indice_massa_corporal < 30)
    return __is_acima_peso


def is_muito_acima_peso(__indice_massa_corporal):
    """Verifica se o indivíduo está muito acima do peso ideal
        :param __indice_massa_corporal: indice de massa corporal do indivíduo
        :type __indice_massa_corporal: float
        :return is_muito_acima_peso: True ou False para IMC > 30
        :rtype: bool
    """
    __is_muito_acima_peso = (__indice_massa_corporal >= 30)
    return __is_muito_acima_peso
