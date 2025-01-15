if __name__ == "__main__":
  a = float(input("Ingrese numero a: "))
  fun = (lambda x: x/(x**(1/3)-1))(a)
  print("Funcion racional " + str(a) + " es " + str(fun))