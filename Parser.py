# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:34:15 2020

@author: hellf
"""
import os
import re
class sql_parser():
    
    def __init__(self,path):
        
        self.path = path

        
    def sql_parse(self,sep,file):
        with open(self.path+sep+file,'r+') as file:
            data = file.read() 
        queries = [re.findall('CREATE .*|Insert .*|ALTER .*|SET DEFINE .*',el) for el in re.sub('\n|\t| -- fk', ' ',data).split(';')]
        return queries

# %%