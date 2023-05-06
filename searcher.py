import json
import pickle

from nltk.corpus.reader.panlex_swadesh import line_tokenize
import Stemmer
import sys
import re
from collections import defaultdict
from nltk.stem import PorterStemmer
import numpy as np
import time
ind = {'n': 0, 't': 1, 'b': 2, 'i': 3, 'l': 4, 'r': 5, 'c': 6}

query = 'hello t:hi b:hey'


def binarySearch(arr, x):
    l = 0
    r = len(arr)
    while (l <= r):
        m = l + ((r - l) // 2)
 
        res = (x == arr[m])
 
        # Check if x is present at mid
        if (res == 0):
            return m - 1
 
        # If x greater, ignore left half
        if (res > 0):
            l = m + 1
 
        # If x is smaller, ignore right half
        else:
            r = m - 1
    return 

# arr = [1,2,3,5,6,7]
st_f=['0', '0xa208070d38331937', '1226770', '157765058', '18485695', '197915449', '20080224151946', '20110708154941', '20160917212050', '205478437', '21464002', '27381421', '3325', '43302544', '56849', '7355598', '8dko_nakagawa', 'a13', 'albrecht', 'area_footnotes', 'b6berg', 'beyrut', 'bricquebec', 'carruba', 'cityscholarships', 'creveld', 'denmarkboxers', 'dsutor', 'environ', 'fh8065503553400', 'gaabanter', 'goujin', 'heartorg', 'høegh', 'isro', 'kaev', 'kone', 'leban', 'lutjenholm', 'match_bog_thu', 'melker', 'mosier', 'ndrd4', 'o3szudo1', 'paddle', 'pickhandle', 'primariapitesti', 'rangeblock', 'room', 'scheming', 'sikhsiyasat', 'srweb', 'szomoru', 'thodi', 'tura', 'vasterasgustav', 'weak', 'yamoto', 'εβραϊκό', 'ホテル']
pro = query.split(' ')

# for i in pro:
#     if ':' in i:
#         pro[i] = 'f' + pro[i]
#     else:
#         pro[i] = 'q' + pro[i]
length = len(pro)
arr=''
for i in pro:
    if ':' in i:
        arr.append(pro[:pro.index(":")])
    else:
        arr.append('q')
    str1 = str(binarySearch(st_f, arr[i])) + '.txt'
    with open(str1, 'r') as fp:
        for j, line in enumerate(fp):
            if line[:line.index(":")] == arr[i]:
                x = line[line.index(":"):]
