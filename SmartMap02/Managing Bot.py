#Union Managing Bot
#Author: Tins-vn
#Git-hub: https://github.com/Tins-vn

import csv
from scipy.spatial.distance import euclidean
import plot
from sklearn.cluster import DBSCAN

file_name = input("Nhập tên file: ")
file_name = file_name + ".csv"
data = {}

with open(file_name, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    name = next(reader)

    X = next(reader)
    Y = next(reader)

    X = [X[0]] + list(map(int, X[1:])) 
    Y = [Y[0]] + list(map(int, Y[1:])) 

    cord = list(zip(X,Y))
    data = dict(zip(name, cord)) 


plot.scatter_map(X, Y, name)

