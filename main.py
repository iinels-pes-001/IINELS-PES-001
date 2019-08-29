# -*- coding: utf-8 -*-

"""
Esse módulo implementa a funcionalidade de entrar com os dados de peso e altura do indivíduo através 
de um dispositivo de entrada de dados, otimizando a versão iMC v1.0.0, em que esses parâmetros eram
definidos diretamente via código.

Requisitos e orientações para resolução dessa tarefa encontram-se na wiki do projeto: 
_Wiki: https://github.com/alexaquino/IINELS-PES-001/wiki.

:Authors: Alex Aquino, Bruno Spinelli, Pablo Queiroz, Rodrigo Henrique
:Version: 2.0.0
:License: MIT
"""

import imc

# Entrada/Saída de dados

imc.exibirCabecalhoResultadoFormatado("iMC - Calculadora Índice de Massa Coporal v2.0.0")
pesoQuilos = float(input("  + Informe o peso em quilos   (Ex.: 70.5): "))
alturaMetros = float(input("  + Informe a altura em metros (Ex.: 1.85): "))
indiceMassaCorporal = imc.calcularIndiceMassaCorporal(pesoQuilos, alturaMetros)
imc.exibirAnalise(indiceMassaCorporal)
imc.exibirResultadoFormatado(indiceMassaCorporal)