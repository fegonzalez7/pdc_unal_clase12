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

[![image.png](https://i.postimg.cc/kXrkjJkX/image.png)](https://postimg.cc/Yj3n0HrJ)

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

### Funciones sin  nombre (anónima) - lambdas
En Python, una función lambda es una función anónima que puede ser definida en **una sola línea de código** y puede tomar cualquier número de argumentos. Las funciones lambda se utilizan comúnmente para definir pequeñas funciones que se utilizarán en el momento o en contextos específicos.

```python
lambda <argumentos>: <expresion>
```

+ **argumentos:** Es una lista separada por comas de los argumentos que la función toma. 
+ **expresion:**  Es la expresión que la función devuelve. *traducción:* Es como poner toda la lógica en el *return* de una función.

**Ejemplo 3:** Función para sumar dos números.
```python
def sumarDosNumeros(a : int, b : int )-> int:
  return a + b

if __name__ == "__main__":
  a = int(input("Ingrese numero a: "))
  b = int(input("Ingrese numero b: "))
  suma = sumarDosNumeros(a, b)
  print("La suma de " + str(a) + " y " + str(b) + " es " + str(suma))
```

```python
if __name__ == "__main__":
  a = int(input("Ingrese numero a: "))
  b = int(input("Ingrese numero b: "))
  sumaFuncion = lambda a, b: a + b
  suma = sumaFuncion(a, b)
  print("La suma de " + str(a) + " y " + str(b) + " es " + str(suma))
```

```python
if __name__ == "__main__":
  a = int(input("Ingrese numero a: "))
  b = int(input("Ingrese numero b: "))
  suma = (lambda x, y: x + y)(a,b)
  print("La suma de " + str(a) + " y " + str(b) + " es " + str(suma))
```

**Ejercicio 2:** Cree una función anónima que calcule:
$$f(x) = \frac{x}{x^{1/3}-1}$$

### Argumentos por defecto
Al escribir una función es necesario definir los argumentos que recibirá. Sin embargo, al llamar la función se puede incurrir en un error si no se llaman todos los parametros con su respectivo tipo y valor (por eso es buena práctica *tipear* los argumentos, para poder saber que valores deben tomar). 

En ocasiones ciertos argumentos vienen definidos con valores por defecto, de ese modo no es necesario dar su valor al momento de llamar la función.

**Ejemplo 4:** Función para sumar dos números con un argumento por defecto.
```python
def sumarDosNumeros(a : int, b : int = 10)-> int:
  return a + b

if __name__ == "__main__":
  a = int(input("Ingrese numero a: "))
  b = int(input("Ingrese numero b: "))
  suma = sumarDosNumeros(a)
  print("La suma de " + str(a) + " y " + str(10) + " es " + str(suma))
  suma = sumarDosNumeros(a, b)
  print("La suma de " + str(a) + " y " + str(b) + " es " + str(suma))
```

**Ejercicio 4:** Cree una función que reciba dos números y un parametro con el cual se decida si regresa el mayor o el menor, por defecto debe regresar el mayor.

### Argumentos *args y **kwargs
**Spoiler:** Esto implica un pequeño viaje al futuro, ya que se van a tocar temas como tuplas y diccionarios. Sin embargo, es sólo lo básico.

Para resolver el problema de los argumentos en Python se pueden definir funciones con los argumentos <i>*args</i> y <i>**kwargs</i>:

+ <i>*args</i>: La función recibe *n* argumentos sin nombre y los guarda en una tupla (arreglo inmutable de objetos). *args* es un identificador cualquiera, lo impotante en el operador *.

+ <i>**kwargs</i>: La función recibe *n* argumentos con nombre y los guarda en un diccionario (arreglo de objetos con identificador). *kwargs* es un identificador cualquiera, lo impotante en el operador **.


**Ejemplo 5:** Función para sumar n números.

```python
def sumarNumeros(*args)-> int:
  suma : int = 0
  # Los argumentos están almacenados en la tupla args
  for num in args:
    suma +=  num
  return suma

if __name__ == "__main__":
  a = int(input("Ingrese numero a: "))
  b = int(input("Ingrese numero b: "))
  c = int(input("Ingrese numero c: "))
  d = int(input("Ingrese numero d: "))
  e = int(input("Ingrese numero e: "))
  print("La suma de dos " + str(sumarNumeros(a, b)))
  print("La suma de tres " + str(sumarNumeros(a, b, c)))
  print("La suma de cuatro " + str(sumarNumeros(a, b, c, d)))
  print("La suma de cinco " + str(sumarNumeros(a, b, c, d, e)))
```

## Reto 9
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_9 en slack.

1. De los retos anteriores seleciones 3 funciones y escribalas en forma de lambdas.
2. De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).
3. Escriba una función recursiva para calcular la operación de la potencia.
4. Utilice la siguiente plantilla de code para contar el tiempo:
```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```

Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
**Importante:** Revisar este [hilo](https://stackoverflow.com/questions/8220801/how-to-use-timeit-module).

5. Crear cuenta en [stackoverflow](https://stackoverflow.com/) y adjuntar imagen en el repo

6. Cosas de adultos....ir a [linkedin](https://www.linkedin.com/) y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalon. Dejar enlace en el repo.
