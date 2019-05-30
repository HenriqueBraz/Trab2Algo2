#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:35:31 2019

@author: henrique
"""
from castelator import Castelator
import time

if __name__ == "__main__":
    
    inicio=time.time()
    
    
    c = Castelator()
    pergaminho = c.leitura_pergaminho('/home/henrique/Trab2Algo2/casos-t2/caso60.txt')
    print('pergaminho:')
    print(pergaminho)
    print('\n')
    
    c.separa_dados(pergaminho)
    print('c.tamanho_exercito_0')
    print(c.tamanho_exercito_0)
    print('c.total_castelos')
    print(c.total_castelos)
    print('c.estradas_regiao')
    print(c.estradas_regiao)
    print('\n')
    
    castelo_e_guarnicao = (c.conta_guarnição(pergaminho,c.total_castelos))
    print('castelo_e_guarnicao')
    print(castelo_e_guarnicao)
    print('\n')
    
    estradas = c.conta_estradas(pergaminho, c.total_castelos,c.estradas_regiao)
    print('estradas')
    print(estradas)
    print('\n')
    
     
    grafo = c.grafo(castelo_e_guarnicao,estradas)
    print('grafo')
    print(grafo)
    print('\n')
    
    c.grafo_pronto = c.arruma_grafo(grafo,estradas)
    print('grafo_pronto')
    print(c.grafo_pronto)
    print('\n')

    print('castelos conquistados:\n')
    print(c.conquistator())

        
    fim=time.time()
    print("Tempo total: {} segundos".format(fim-inicio))