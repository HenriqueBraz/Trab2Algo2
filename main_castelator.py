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
    pergaminho = c.leitura_pergaminho('/home/henrique/Trab2Algo2/casos-t2/casoteste.txt')
    print(pergaminho)
    c.separa_dados(pergaminho)
    print(c.tamanho_exercito_0)
    print(c.total_castelos)
    print(c.estradas_regiao)
              
        
    fim=time.time()
    
    print("Tempo total: {} segundos".format(fim-inicio))