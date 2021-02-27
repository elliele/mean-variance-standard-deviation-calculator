import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  a = np.array(list).reshape(3,3)
  mean1 = a.mean(axis=0).tolist()
  mean2 = a.mean(axis=1).tolist()
  mean3 = a.mean()
  var1 = a.var(axis=0).tolist()
  var2 = a.var(axis=1).tolist()
  var = a.var()
  std1 = a.std(axis=0).tolist()
  std2 = a.std(axis=1).tolist()
  std3 = a.std()
  mx1 = a.max(axis=0).tolist()
  mx2 = a.max(axis=1).tolist()
  mx3 = a.max()
  mn1 = a.min(axis=0).tolist()
  mn2 = a.min(axis=1).tolist()
  mn3 = a.min()
  sum1 = a.sum(axis=0).tolist()
  sum2 = a.sum(axis=1).tolist()
  sum3 = a.sum()
  
  calculations = {'mean':[mean1, mean2, mean3],
  'variance': [var1, var2, var],
  'standard deviation': [std1, std2, std3],
  'max': [mx1, mx2, mx3],
  'min': [mn1, mn2, mn3],
  'sum': [sum1, sum2, sum3]}




  return calculations 
