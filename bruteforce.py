# Principal|



class Bin:
    def __init__(self):
        self.list = []
 
    def AñadirPlaca(self, item):
        self.list.append(item)
 
    def suma(self):
        total = 0
        for elem in self.list:
            total += elem
        return total
 
    def Mostrar(self):
        return self.list
 
def BinPacking(arreglo, areaPlancha):
    """ Returns list of bins with input items inside. """
    a = []
    a.append(Bin())
 
    for item in arreglo:
       
        añadir = False
 
        for bin in a:
            if bin.suma() + item <= areaPlancha:
                bin.AñadirPlaca(item)
                añadir = True
                break
       
       
        if añadir == False:
            nuevo = Bin()
            nuevo.AñadirPlaca(item)
            a.append(nuevo)
 
    arreglo = []
    for bin in a:
        arreglo.append(bin.Mostrar())
 
    return(arreglo)


def sumarareas(G):
    n = len(G)
    suma = 0
    for i in range(n):
        suma += G[i]
    return suma

def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
    return unaLista

def Position(G):
    n = len(G)
    print(G[1])
    print(G)

def Ordenar(G):
    ordenado = sorted(G , key=lambda k: [k[0], k[1]],reverse=True)
    return ordenado

def SepararArea(arreglo):
	n=len(arreglo)
	a=[]

	for i in range(n):
		a.append(arreglo[i][0])
	
	return a

def Unificar(G):
    ordenado=SepararArea(Ordenar(TC))
    n=len(ordenado)
    a=[]
    resultado=[]
    for i in range(n):
        a.append(ordenado[i])
    for i in range(n):
        for j in range(3):
            resultado.append(a[i][j])
    return resultado

#print(ordenado)
#print(resultado)
def Posicionar(G):
    u=Unificar(SepararArea(Ordenar(TC)))
    n=len(u)
    b = []
    cordenadas = []
    arrx = []
    arry = []
    arrz = []
    x = 0
    y = 0
    z = 0
    arrx.append(x)
    for i in range(n):
        x = u[i] +x
        arrx.append(x)
    return arrx

with open('cortes.in') as f:
    contenedor = f.readline().strip()
    contenedor1, contenedor2,contenedor3 = [int(x) for x in contenedor.split(' ')]
    volume = contenedor1*contenedor2*contenedor3
    Medidas = []
    TC = []
    Areas = []
    line = int(f.readline())
    for i in range(line):
        D = f.readline().strip()
        T, Q, X, Y, Z = [x for x in D.split(' ')]
        cantidad = int(T)
        tipo = Q
        G = [[] for _ in range(cantidad)]
        for j in range(cantidad):
            G[j].append(((tipo),(int(X),int(Y),int(Z))))
            TC.append(((int(X),int(Y),int(Z)),(int(X)*int(Y)*int(Z))))
            Medidas.append((int(X),int(Y),int(Z)))    
            Areas.append((int(X)*int(Y)*int(Z)))
                   
        #print(G)
    #print(TC)
    #print(Areas)
    AreaTotal = sumarareas(Areas)
    Desperdicio = 100 -((AreaTotal/volume)*100)
    Usado = 100-Desperdicio
    #print(AreaTotal)
    #print(Usado)
    
    hola=  BinPacking(Areas, volume)
    print(Posicionar(Unificar(SepararArea(Ordenar(TC)))))
    #print(Medidas)
    #print(ordenamientoBurbuja(Areas))
    
    #print(Position(Areas))
    #SepararArea(Ordenar(TC))