def doubleDown(n):
  return lambda a : a * n

doubleNum = doubleDown(8)

print(doubleNum(12))

