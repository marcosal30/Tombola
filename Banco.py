#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:36:57 2022

@author: mariaelenacontini
"""

import Utils
import Giocatore
import random

class Banco:
    
    def __init__(self,n_giocatori,lista_cartelle):
        self.n_giocatori = n_giocatori
        self.lista_cartelle = lista_cartelle
            
    def assegna_cartelle(self):
        """
        Assegna a ciascun giocatore il numero richiesto di cartelle facendo in modo che
        non sia possibile assegnare a più giocatori la medesima cartella.
        
        Input
        -----
        NaN
        
        Output
        ------
        giocatori (giocatore[]) : lista di oggetti giocatore aventi ognuno il numero
        di cartelle richieste 
        
      
        """
        cartelle_disponibili=[]
        cartelle_disponibili = Utils.genera_gruppi(self.lista_cartelle)
        giocatori=[]

        for i in range(0,self.n_giocatori):
            giocatori.append(Giocatore.Giocatore(str(i+1),self.lista_cartelle[i]))
            for j in range(0,self.lista_cartelle[i]):
                index_cartella = random.randint(0,len(cartelle_disponibili)-1)
                giocatori[i].prendi_cartella(cartelle_disponibili[index_cartella])
                cartelle_disponibili.pop(index_cartella)
                
        return giocatori
        
        
            
            
        
        
            
            
        