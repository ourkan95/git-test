#Kütüphaneler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import warnings


#Data okuması
def read_exc(data):
    
    data = pd.read_excel(data,header = 0)  
    
    return data

#Nan değerlerin silinmesi    
def delete_nan(data):  
    
    data = data.dropna()    
           
    return data

#NaN Numeric değerlerin silinmesi
def delete_nanNum(data):
    
    data = data.apply(pd.to_numeric(), errors = 'coerence')
    
    return data
    
def delete_zeros(data):
    
    data = data[~(data == 0).all(axis=1)]
    
    return data