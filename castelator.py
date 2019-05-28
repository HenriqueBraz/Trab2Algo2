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
        self.total_conquistados = 0
        self.grafos_estrada = []

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
        tamanho = int(self.estradas_regiao)
        temp3 = []
        for i in range((tamanho -1)):
              temp = pergaminho[inicio].split()
              temp2 = pergaminho[inicio + 1].split()
              if i == (tamanho -2):
                  if temp[0] == temp2[0]:
                      temp3.append(temp)
                      temp3.append(temp2) 
                      estradas.append(temp3)
                  else:
                      temp3.append(temp)
                      estradas.append(temp)
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
        lista_chaves = list(castelo_e_guarnicao.keys())
        lista = []

        for i in range(len(estradas)):
            if (len(estradas[i])) < 3:
                temp = (estradas[i][0])
                if type(temp) ==  list :   
                    tempx = temp[0]
                    if tempx not in lista:
                        lista.append(tempx)
            else:        
                temp = (estradas[i][0][0])
                if temp not in lista:
                    lista.append(temp)
        
        li1 = lista
        li2 = lista_chaves
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
                
        for i in range(len(li_dif)):
            temp = li_dif[i]
            temp2 = lista_valores[int(temp)]
            temp3 = []
            castelo_e_guarnicao[str(temp)] = temp2,temp3 
        
        for i in range(len(estradas)):
            for j in range(len(estradas[i])):
                if len(estradas[i]) < 3:
                    temp = estradas[i][0]
                    if type(temp) ==  list :   
                        temp = temp[0]
                else:
                    temp = estradas[i][0][0]
                                   
            temp2 = lista_valores[int(temp)]
            temp3  = estradas[i]
            castelo_e_guarnicao[str(temp)] = temp2,temp3
            
        return(castelo_e_guarnicao)
            
            
    def arruma_grafo(self,grafo,estradas):
       """
        Método que incrementa e ordena os caminhos que estão faltando
        no grafo anterios
        param grafo: OrderedDict contendo o grafo
        param entradas: lista contendo as listas dos caminhos,
        agrupadas por ordem do castelo que saem (0,1,2,etc)
        return: um dicionario que representa o grafo do pergaminho, 
        na ordem: [numero do castelo]:[guanição],[caminhos que saem do castelo]
        """ 
       lista_chaves = list(grafo.keys())
       lista_valores = list(grafo.values())
       temp = ''
       temp2 = ''
       temp3 = []
       for i in range(len(lista_chaves)):
           if lista_valores[i][1] == []:
               temp3 = []
               for j in range(len(estradas)):
                   for k in range(len(estradas[j])):
                       if lista_chaves[i] in (estradas[j][k]):
                           if (len(estradas[j][k])) == 1:
                               temp = lista_chaves[i]
                               x = estradas[j]
                               if x[0] != i:
                                   temp3 += [[x[1],x[0]]]    
                               else:
                                   temp3 += [estradas[j][k]]
                               temp2 = grafo[str(temp)]
                               grafo[str(temp)] = temp2[0],temp3
                           else:    
                               temp = lista_chaves[i]
                               x = estradas[j][k]
                               if x[0] != i:
                                   temp3 += [[x[1],x[0]]]
                               else:    
                                   temp3 += [estradas[j][k]]
                               temp2 = grafo[str(temp)]
                               grafo[str(temp)] = temp2[0],temp3
                              
                           
       return(grafo)                 
               
                    
          
        
    def test(self, grafo, castelo, castelo_origem):
        conquista = 1
        index = 0
        self.tamanho_exercito_0 = int(self.tamanho_exercito_0) - 50
        lista_grafo = grafo
        while(conquista == 1):
            if(int(lista_grafo[castelo][1][index][1]) == castelo_origem):
                index = index+1
                idx_castelo = 0
            else:
                idx_castelo = 1
            castelo_origem = castelo
            primeiro_castelo = int(lista_grafo[castelo][1][index][idx_castelo])
            castelo_a_conquistar = lista_grafo[primeiro_castelo]
            tropas_castelo_a_conquistar = int(castelo_a_conquistar[0])
            if(2*tropas_castelo_a_conquistar < self.tamanho_exercito_0 and primeiro_castelo not in self.grafos_estrada):
                print(castelo_a_conquistar)
                self.total_conquistados = self.total_conquistados+1
                self.grafos_estrada.append(primeiro_castelo)
                self.test(lista_grafo, primeiro_castelo, castelo_origem)
                index = index+1
            else:
                conquista = 0



        
        
        
        
        
        
        
        
        
        
        