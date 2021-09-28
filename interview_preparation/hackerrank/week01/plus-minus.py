import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    map = {"positives": 0, "negatives": 0, "zeros": 0}

    for item in arr:
        if item < 0:
            map["negatives"] += 1
        elif item == 0:
            map["zeros"] += 1
        else:
            map["positives"] += 1
    
    for currency in map.values():
        prop = currency / len(arr)
        print("%.6f" % prop)