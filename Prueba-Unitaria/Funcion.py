def Nota_estudiante(x):
  try:
    x = int(x)
  except ValueError:
    print ("Ingrese un Numero")
    return False

  if x >= 75:
    return("O")

  elif x >=60 and x <= 74:
    return("A")

  elif x >= 50 and x <= 59:
    return("B")

  elif x >=40 and x <= 49:
    return("C")

  elif x <= 40:
    return("D")