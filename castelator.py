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
        return: void
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
        return: OrderedDict
        """
        castelo_e_guarnicao = collections.OrderedDict()
        #castelo_e_guarnicao = {}
        castelo_e_guarnicao['0'] = self.tamanho_exercito_0
        tamanho = int(total_castelos) + 1
        for i in range(1,tamanho):    
              temp = pergaminho[i].split()
              castelo_e_guarnicao[temp[0]] = temp[1]

        return(castelo_e_guarnicao)
        
        
        
    def conta_estradas(self,pergaminho,total_castelos,estradas_regiao):
        """
        Método que monta uma lista com listas com os 
        numeros de estradas, agrupadas por ordem do castelo que saem (0,1,2,etc)
        param pergaminho: lista contendo o pergaminho lido
        param total_castelos: dicionario ordenado por {'numero do castelo':'tamanho da guarnição'}
        param estradas_região: variável contendo o numero de estradas da região
        retun: list
        """
        estradas = []
        inicio = int(total_castelos) + 1
        tamanho = (int(len(pergaminho))) - (int(total_castelos) + 1)
        temp3 = []
        for i in range((tamanho - 1)):
              temp = pergaminho[inicio].split()
              temp2 = pergaminho[inicio + 1].split()
              print(temp)
              print(i)
              print(tamanho -2)
              if i == (tamanho -2):
                  if temp[0] == temp2[0]:
                      temp3.append(temp2) 
                      estradas.append(temp3)
                  else:
                      temp3.append(temp)
                      estradas.append(temp2)
                   
              elif temp[0] != temp2[0]:
                  if temp3 != []:
                     temp3.append(temp) 
                     estradas.append(temp3)
                     inicio +=1
                     temp3 = []
                  else:  
                     estradas.append(temp)
                     inicio +=1       
              else:
                   temp3.append(temp)
                   inicio +=1 
                   
        return(estradas)     
    
        
        
        
    
    def grafo(self,castelo_e_guarnicao,estradas):
        """
        Método que retorna um dicionario contendo chave
        como nunero do castelo e valor como os caminhos
        possíveis daquele castelo
        param castelo_e_guarnicao: OrderedDict contendo os castelos e guarniçoes
        param entradas: lista contendo as listas dos caminhos,
        agrupadas por ordem do castelo que saem (0,1,2,etc)
        return: um dicionario que representa o grafo do pergaminho, 
        na ordem: [numero do castelo]:[guanição],[caminhos que saem do castelo]
        """
        lista_valores = list(castelo_e_guarnicao.values())
        lista = []
        for i in range(len(estradas)):
           temp = (estradas[i][0][0])
           if temp not in lista:
               lista.append(temp)
        
        for i in range(len(lista)):
            temp = (estradas[i][0][0])
            temp2 = lista_valores[int(temp)]
            temp3  = estradas[i]
            castelo_e_guarnicao[str(temp)] = [temp2],temp3
            
        return(castelo_e_guarnicao)
            
            
    def arruma_grafo(self,grafo):
        
       lista_chaves = list(grafo.keys())
       lista_valores = list(grafo.values())
       
       print(lista_valores)
       print('\n')
       print(lista_chaves)
       print('\n')
       
       for i in range(len(lista_chaves)):
           
           print(lista_valores[i][0])
           print(lista_valores[i][1])
        
        
        
        
        
        
        
        
        
        
        
        
        