#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:43:22 2019

@author: yifan
"""

#normalcalc

from numpy import subtract
import numpy as np
import pandas as pd

def normal(v0, v1, v2, ccw = True):
    #edge v0->v1, edge v1->v2
    if ccw == True:
        return np.cross(subtract(v1,v0),subtract(v2,v1)).astype('float16')
    elif ccw == False:
        return np.cross(subtract(v1,v0),subtract(v2,v0)).astype('float16')


def df_as_list(csv_dir):
    df=pd.read_csv(csv_dir, header = None, index_col=[0])
    return df.values.tolist()

def getFaceNormal(root, nodeCount, CCW = True):
    coord = df_as_list(root+'_coord_'+str(nodeCount)+'.csv')
    index = df_as_list(root+'_index_'+str(nodeCount)+'.csv')
    faceNormal = []
    for face in index:
        v0 = coord[int(face[0])]
        v1 = coord[int(face[1])]
        v2 = coord[int(face[2])]
        n = normal(v0, v1, v2, ccw=CCW)
        faceNormal.append(n)
    np.savetxt(root+'_faceNormal_'+str(nodeCount)+'.csv',
               faceNormal,delimiter=",")
