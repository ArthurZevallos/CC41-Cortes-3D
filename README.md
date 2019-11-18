# Complejidad Algorítmica

## Trabajo Final

### Sección CC41

### Tema: Bin Packing 3D 

###      Integrantes:

- Zevallos Ccorahua, Arthur Antoni F.

### INTRODUCCIÓN:

Este proyecto trata de solucionar un problema sobre la optimización de uso de espacio, ya que se cuenta con diversas aplicaciones en diferentes industrias. Hace referencia al ahorro de espacio que se podría aplicar en los almacenes de embarcamientos, almacenes de mercadería para poder minimizar el desperdicio de recursos o activo (el costo y espacio) y maximizar algún otro. Para este proyecto se podrían aplicar varios algoritmos que podrían dar una solución o también se podría usar algoritmos heurísticos para tratar de dar una solución más exacta al problema, pero en este trabajo estaré implementando el algoritmo de Fuerza bruta. Luego podremos analizar y se compararan el algoritmo con otras soluciones cual solución tiene manera tiempo de ejecución y ver cuáles son las soluciones más optimas y más eficientes.

### OBJETIVOS:

##### Objetivo General:

Al finalizar el curso, el estudiante implemente distintos algoritmos para resolver problemas en contexto real sobre problemas de almacenamiento basándose en técnicas tales como Fuerza Bruta, Programación Dinámica o implementación de algoritmos heurísticos.

##### Objetivos Específicos:

•	Crear algoritmos que solucione el problema de cortes y almacenamiento con distintos métodos de programación.
•	Calcular los tiempos de complejidad de los algoritmos implementados.
•	Analizar la eficiencia de las soluciones propuestas mediante los tiempos algorítmicos que presentan. 
•	Porcentaje de desperdicio para el empaquetamiento y número de cortes (para los recortes)
•	Tablas de comparación: tiempo de ejecución de algoritmo vs entrada de datos, memoria consumida por algoritmo vs entrada de datos
•	Presentar conclusiones en función de los datos levantados en el punto anterior.


### MARCO TEORICO:

Para el trabajo, la implementación de los algoritmos que usaremos estará en base al lenguaje de programación Phyton. Dichos algoritmos son los siguientes:
1.	Fuerza Bruta: Es el algoritmo más simple. Consiste en probar todas las posibles posiciones de forma exhaustiva. Ya que la fuerza bruta atravesará todas las combinaciones posibles, no toma en cuenta nada. Entonces, al considerar todo, el problema se puede salir de control, por lo que solo es lo suficientemente buena para problemas de pequeñas instancias.



# Análisis de complejidad de Fuerza Bruta
Fuerza bruta= O(n)  en el peor de los casos O(n^2)

### CONCLUSIONES:

El problema de Bin Packing en 3D busca que las piezas a disposición quepa de forma eficiente en un contenedor al momento de almacenar las piezas el espacio utiliazdo. Este problema conocido también como problema de la mochila tiene diferentes soluciones, entre las más eficientes se requeriría un algoritmo de aproximación como el del Primer ajuste. Sin embargo, en este ocasión se intentó solucionarlo con los algoritmos Backtracking y Fuerza bruta debido al diferente orden de las piezas, restricciones del empaquetamiento y los diferentes resultados que este propone.
