# -*- coding: utf-8 -*-
"""Fuzzy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cf5XkZ0Suu4RcWNmjwYLYGVEVJZuR0LC
"""

from google.colab import drive
drive.mount('/content/drive')

"""## DataSet"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
112
path = "drive/My Drive/Fuzzy/"
file_dataset = 'drive/My Drive/Fuzzy/influencers.csv'
columns = ["id", "followerCount", "engagementRate"]
dataset = pd.read_csv(file_dataset, header=None)
dataset.columns = columns
dataset

follow = dataset['followerCount']
follow

erate = dataset['engagementRate']
erate

"""# Fuzzification Process

## Graphic
"""

def fuzzification1(follower):
  # followerCount = [20000,40000,60000,80000]
  
  high = []
  normal = []
  low = []

  for i in range(max(follower)):

    if i >= 80000:
      high.append(1)
    elif i < 60000:
      high.append(0)
    else :
      high.append((i-60000)/(80000-60000))

    if i >= 40000:
      low.append(0)
    elif i <= 20000:
      low.append(1)
    else :
      low.append((40000-i)/(40000-20000))

    if i <= 20000 or i >= 80000:
      normal.append(0)
    elif i > 20000 and i < 40000 :
      normal.append((i-20000)/(40000-20000))
    elif i >= 40000 and i <= 60000 :
      normal.append(1)
    elif i > 60000 and i < 80000 :
      normal.append((80000-i)/(80000-60000))
  return high,normal,low

def fuzzification2(erate):
  # engagementRate = [1.5,3.0,4.5,6.0]
  high = []
  normal = []
  low = []
  i = 0.0

  while (i < max(erate)):

    if i >= 6.0:
      high.append(1)
    elif i < 4.5:
      high.append(0)
    else :
      high.append((i-4.5)/(6.0-4.5))

    if i >= 3.0:
      low.append(0)
    elif i <= 1.5:
      low.append(1)
    else :
      low.append((3.0-i)/(3.0-1.5))

    if i <= 1.5 or i >= 6.0:
      normal.append(0)
    elif i > 1.5 and i < 3.0 :
      normal.append((i-1.5)/(3.0-1.5))
    elif i >= 3.0 and i <= 4.5 :
      normal.append(1)
    elif i > 4.5 and i < 6.0 :
      normal.append((6.0-i)/(6.0-4.5))
    
    i += 0.1
  return high,normal,low

followHigh = fuzzification1(follow)[0]
followNormal = fuzzification1(follow)[1]
followLow = fuzzification1(follow)[2]

plt.plot(followHigh)
plt.plot(followNormal)
plt.plot(followLow)
plt.show()

erateHigh = fuzzification2(erate)[0]
erateNormal = fuzzification2(erate)[1]
erateLow = fuzzification2(erate)[2]

plt.plot(erateHigh)
plt.plot(erateNormal)
plt.plot(erateLow)
plt.show()

"""## Code"""

def fuzz1High(i):
  # followerCount = [20000,40000,60000,80000]
  if i >= 80000:
    return  1
  elif i < 60000:
    return  0
  else :
    return  (i-60000)/(80000-60000)
def fuzz1Low(i):
  if i >= 40000:
    return  0
  elif i <= 20000:
    return  1
  else :
    return  (40000-i)/(40000-20000)
def fuzz1Normal(i):
  if i <= 20000 or i >= 80000:
    return  0
  elif i > 20000 and i < 40000 :
    return  (i-20000)/(40000-20000)
  elif i >= 40000 and i <= 60000 :
    return  1
  elif i > 60000 and i < 80000 :
    return  (80000-i)/(80000-60000)

def fuzz2High(i):
  # engagementRate = [1.5,3.0,4.5,6.0]
  if i >= 6.0:
    return  1.0
  elif i < 4.5:
    return  0.0
  else :
    return  (i-4.5)/(6.0-4.5)
def fuzz2Low(i):
  if i >= 3.0:
    return  0.0
  elif i <= 1.5:
    return  1.0
  else :
    return  (3.0-i)/(3.0-1.5)
def fuzz2Normal(i):
  if i <= 1.5 or i >= 6.0:
    return  0.0
  elif i > 1.5 and i < 3.0 :
    return  (i-1.5)/(3.0-1.5)
  elif i >= 3.0 and i <= 4.5 :
    return  1.0
  elif i > 4.5 and i < 6.0 :
    return  (6.0-i)/(6.0-4.5)

"""# Execution"""

def minimum(a,b):
  if a < b :
    return a
  else : return b

id = []
value = []
i = 0
while i < 100:
  small = []
  medium = []
  big = []
  fz1High,fz1Normal,fz1Low = fuzz1High(follow[i]),fuzz1Normal(follow[i]),fuzz1Low(follow[i])
  fz2High,fz2Normal,fz2Low = fuzz2High(erate[i]),fuzz2Normal(erate[i]),fuzz2Low(erate[i])
  #inference
  small.append(minimum(fz2High,fz1Low))
  small.append(minimum(fz2High,fz1Normal))
  big.append(minimum(fz2High,fz1High))
  small.append(minimum(fz2Normal,fz1Low))
  medium.append(minimum(fz2Normal,fz1Normal))
  big.append(minimum(fz2Normal,fz1High))
  medium.append(minimum(fz2Low,fz1Low))
  big.append(minimum(fz2Low,fz1Normal))
  big.append(minimum(fz2Low,fz1High))
  maxSmall = max(small)
  maxMedium = max(medium)
  maxBig = max(big)
  #defuzzification
  # 20 40 60 80
  tes1 = [2,4,5,8,9,12,13,14,17,18,19]
  tes2 = [40,42,43,45,48,49,50,53,55,56,58,59]
  tes3 = [80,82,83,84,86,88,90,91,95,97,99,100]
  sumTes1,sumTes2,sumTes3 = 0,0,0
  for k in range(len(tes1)):
    sumTes1 += tes1[k]
  for l in range(len(tes2)):
    sumTes2 += tes2[l]
  for m in range(len(tes3)):
    sumTes3 += tes3[m]
  value.append((sumTes1*maxSmall + sumTes2*maxMedium + sumTes3*maxBig)/(len(small)*maxSmall + len(medium)*maxMedium + len(big)*maxBig))
  id.append(i+1)
  i += 1

x = 0
for x in range(len(value)):
  value[x] = value[x]*100/300

value

"""# Sorting"""

def insertionSort(arr,arr2): 
	for i in range(1, len(arr)): 
		key,xyxy = arr[i],arr2[i] 
		j = i-1
		while j >=0 and key > arr[j] : 
				arr[j+1],arr2[j+1] = arr[j],arr2[j] 
				j -= 1
		arr[j+1],arr2[j+1] = key,xyxy

insertionSort(value,id)

valueFixed = []
for n in range(20) :
  valueFixed.append(value[n])
while n < 99 :
  valueFixed.append('')
  n += 1
idFixed = []
for o in range(20) :
  idFixed.append(id[o])
while o < 99 :
  idFixed.append('')
  o += 1

len(idFixed)

len(valueFixed)

value

"""# Chosen.csv"""

info = []
for g in range(20):
  info.append('success')
while g < 99:
  info.append('')
  g += 1
nothing = []
for p in range(100):
  nothing.append('')
kolom = ['id','percentage','information','']
dataset.columns = kolom
dataset['id'] = idFixed
dataset['percentage'] = valueFixed
dataset['information'] = info
dataset[''] = nothing

dataset.to_csv(path+"chosen.csv",index=False)