#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 17:28:39 2019

@author: henrique
"""
from math import trunc
import collections
import time

def leitura_pergaminho(arquivo):
    arq = open(arquivo, 'r')
    pergaminho = arq.readlines()
    return pergaminho




if __name__ == "__main__":
    
    
    
    inicio=time.time()

    pergaminho = leitura_pergaminho('/home/henrique/algo2/TrabAlgo2/casos/casoteste.txt')
    
    
    
    fim=time.time()
    
    print("Tempo total: {} segundos".format(fim-inicio))