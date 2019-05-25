#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 17:28:39 2019

@author: henrique
"""
import collections

class Castelator(object):
    
    
    def __init__(self):
    
        self.tamanho_exercito_0 = ''
        self.total_castelos = ''
        self.estradas_regiao = ''

    def leitura_pergaminho(self,arquivo):
        """
        Método que lê o arquivo inicial
        param arquivo: arquivo inicial a ser lido
        return: retorna uma lista com os dados do arquivo
        """
        arq = open(arquivo, 'r')
        pergaminho = arq.readlines()
        return pergaminho
    
        
    def separa_dados(self,pergaminho):
        """
        Método que separa o tamanho do exercito
        inicial, o total de castelos vizinhos e
        o total de estradas da região
        """
        a = pergaminho[0].split()
        self.tamanho_exercito_0 = a[0]
        self.total_castelos = a[1]
        self.estradas_regiao = a[2]
        
        
    def conta_guarnição(self,pergaminho,total_castelos):
        """
        Método que monta um OrderedDict com o 
        numero do castelo e a guarnição
        param pergaminho: lista contendo o pergaminho lido
        param total_castelos: dicionario ordenado por {'numero do castelo':'tamanho da guarnição'}
        retun: 
        """
        castelo_e_guarnicao = collections.OrderedDict()
        tamanho = int(total_castelos) + 1
        for i in range(1,tamanho):    
              temp = pergaminho[i].split()
              castelo_e_guarnicao[temp[0]] = temp[1]

        return(castelo_e_guarnicao)    
            
        
        
        
        
        
        
        
        
        
        
        
        
        