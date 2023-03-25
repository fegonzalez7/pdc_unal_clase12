# Programación de Computadores - UNAL
## Funciones 2

### Funciones recursivas
Una función recursiva es una función que se llama a sí misma dentro de su propia definición. En otras palabras, una función recursiva se define en términos de sí misma.

La definición de una función recursiva suele incluir dos partes: un caso base y un caso recursivo. El caso base es la condición que detiene la recursividad y devuelve un valor sin llamar a la función de nuevo. El caso recursivo es la parte de la función que llama a sí misma con una entrada modificada y se acerca al caso base.

```python
def <funcion_recursiva>(parametros):
  <caso_base> #suele ser un condicional asignando el valor base
  <funcion_recursiva>(parametros) # Llamada a si misma
```
**Ejemplo 1:** Factorial. Crear un programa que permita calcular el factorial de un número n entero positvo dado.

$$ n! = 1*2*3* \dots * (n-1) * n $$

```python
def factorial(n : int )-> int:
  i : int = 1
  fact : int = 1
  while(i <= n):
    fact *= i
    i += 1
  return fact

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  factorialDeNum = factorial(n)
  print("El factorial de " + str(n) + " es " + str(factorialDeNum))
```

```python
def factorialRecursivo(n : int )-> int:
  print(n)
  # Caso base 
  if n == 1: 
    return 1
  else:
    # Condicion de la funcion recursiva
    return n*factorialRecursivo(n-1)

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  factorialDeNum = factorialRecursivo(num)
  print("El factorial de " + str(num) + " es " + str(factorialDeNum))
```

**Ejemplo 2:** Fibonacci. Crear un programa que permita calcular la secuencia de Fibonacci hasta número n entero positvo dado.

$$f_0 = 0, \ f_1=1 \longrightarrow f_n= f_{n-1} + f_{n-2}$$
$$ 1 \ 1 \ 2 \ 3 \ 5 \ 8 \ 13 \ 21 \ \dots $$


```python
def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    print(sumFibo)
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  serieFibo = fibo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
```


```python
def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2)  

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  serieFibo = fiboRecursivo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
```

**Ejercicio 1:** Cree una función que permita calcular el Máximo Comun Divisor de dos números dados (a y b).

### Funciones sin  nombre - lambdas


### Argumentos *arg y **karg
