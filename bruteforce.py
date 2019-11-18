# Principal|

import heapq as hq
import math

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
def SepararTipoQ(arreglo):
	n=len(arreglo)
	a=[]

	for i in range(n):
		a.append(arreglo[i][1])
	
	return a
def SepararTipo(arreglo):
	n=len(arreglo)
	a=[]

	for i in range(n):
		a.append((arreglo[i][1],arreglo[i][2]))
	
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
'''def Posicionar(G):
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
    u3 = []
    #del(u[0])
    #arrx.append(x)
    for i in range(n):
        arrx.append(u[i])
    u.pop(0)
        #u2 = u.pop(0)
        #arry.append(u[i])
        #arrz.append(u[i])
    return u '''
def posicionar(largox,anchoy,altoz,arreglo,TQ):
    Cantidad = SepararArea(TQ)
    Tipo = SepararTipoQ(TQ)
    n=len(arreglo)
    resultado=[]
    #resultado.append([0,0,0])
    x = arreglo[0]
    y = arreglo[1]
    z = arreglo[2]
    
    x2 = 0
    x2 = 0
    z2  = arreglo[(Cantidad[0]*3)+2]
    z3 = arreglo[2]
    #z2 = arreglo[(Cantidad[0]*3)+2)]
    Contador = 0
    Contador2 = 1
    Contador3 = 2
    Contador4 = 3
    Contador5 = 4
    Contador6 = 5
    print(arreglo)
    ''' for i in range(len(Cantidad)):
        C
        a = []*Cantidad[i]
        a[i]
    print(a) '''
    print(Cantidad)  
    x = arreglo[(Cantidad[0]*3)-3]
    #print(x)
    w = arreglo[(Cantidad[0]*3)-2]  #19
    #print(w)
    #print(Cantidad)
    for i in range(len(Cantidad)):
        if Contador == i:
            
            for j in range(int(Cantidad[0])-1):
                if z <= altoz:
                    resultado.append([0,0,z])
                    z += arreglo[2]
                    #x = arreglo[Cantidad[0]]
                
                   # print((Cantidad[i]*3)+2)
                if z > altoz:
                    resultado.append([0,w,z3])
                    z3+=arreglo[2]
                    if z3 > altoz:
                        w += arreglo[(Cantidad[0]*3)-2]
                        z3 = arreglo[2]
                    if w > anchoy:
                        break
        if Contador2 == i+1:
            z = arreglo[(Cantidad[0]*3)+2]
            z4 = arreglo[(Cantidad[0]*3)+2]
            w2 = arreglo[(Cantidad[0]*3)+1]
            #print(z4)
            #print(arreglo[(Cantidad[0]*3)+2])
            for j in range(int(Cantidad[1])-1):
                if z <= altoz:
                    resultado.append([x,0,z])
                    z += arreglo[(Cantidad[0]*3)+2]
                    #x = arreglo[Cantidad[0]]
                
                   # print((Cantidad[i]*3)+2)
                if z > altoz:
                    resultado.append([x,w2,z4])
                    z4+=arreglo[(Cantidad[0]*3)+2]
                    if z4 > altoz:
                        w2 += arreglo[(Cantidad[0]*3)+1]
                        z4 = arreglo[(Cantidad[0]*3)+2]
                    if w2 > anchoy:
                        break
        if Contador3 == i+2:
            x3 = arreglo[0]+ arreglo[(Cantidad[0]*3)+2]
            z = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3))+2]
            #z100 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3))+2]
            #print(z100)
            z5 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3))+2]
            w3 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3))+1]
            #print(z4)
            #print(arreglo[(Cantidad[0]*3)+2])
            for j in range(int(Cantidad[2])-1):
                if z <= altoz:
                    resultado.append([x3,0,z])
                    z += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3))+2]
                    #x = arreglo[Cantidad[0]]
                
                   # print((Cantidad[i]*3)+2)
                if z > altoz:
                    resultado.append([x3,w3,z5])
                    z5+=arreglo[((Cantidad[0]*3)+(Cantidad[1]*3))+2]
                    if z5 > altoz:
                        w3 += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3))+1]
                        z5 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3))+2]
                    if w3 > anchoy:
                        break
                        
        if Contador4 == i+3:
            x4 = arreglo[0]+ arreglo[(Cantidad[0]*3)]+arreglo[(Cantidad[1]*3)+2]
            z = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3))+2]
            z6 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3))+2]
            w4 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3))+1]
            #print(z4)
            #print(arreglo[(Cantidad[0]*3)+2])
            for j in range(int(Cantidad[3])-1):
                if z <= altoz:
                    resultado.append([x4,0,z])
                    z += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3))+2]
                    #x = arreglo[Cantidad[0]]
                
                   # print((Cantidad[i]*3)+2)
                if z > altoz:
                    resultado.append([x4,w4,z6])
                    z6+=arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3))+2]
                    if z6 > altoz:
                        w4 += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3))+1]
                        z6 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3))+2]
                    if w4 > anchoy:
                        break
        if Contador5 == i+4:
            x5 = arreglo[0]+ arreglo[(Cantidad[0]*3)]+arreglo[(Cantidad[1]*3)]+arreglo[(Cantidad[2]*3)+2]
            z = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3))+2]
            z7 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3))+2]
            w5 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3))+1]
            #print(z4)
            #print(arreglo[(Cantidad[0]*3)+2])
            for j in range(int(Cantidad[4])-1):
                if z <= altoz:
                    resultado.append([x5,0,z])
                    z += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3))+2]
                    #x = arreglo[Cantidad[0]]
                
                   # print((Cantidad[i]*3)+2)
                if z > altoz:
                    resultado.append([x5,w5,z7])
                    z7+=arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3))+2]
                    if z7 > altoz:
                        w5 += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3))+1]
                        z7 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3))+2]
                    if w5 > anchoy:
                        break

        
     
        
    
    return resultado


#print(posicionar(20,30,8,resultado))

with open('cortes.in') as f:
    contenedor = f.readline().strip()
    contenedor1, contenedor2,contenedor3 = [int(x) for x in contenedor.split(' ')]
    volume = contenedor1*contenedor2*contenedor3
    Medidas = []
    TC = []
    Areas = []
    OrdenarTC = []
    OrdenarS = []
    CantidadxTipo = []
    TipoxCaja = []
 
    line = int(f.readline())
    for i in range(line):
        D = f.readline().strip()
        Q, T, X, Y, Z = [x for x in D.split(' ')]
        cantidad = int(Q)
        CantidadxTipo.append((cantidad))
        tipo = T
        TipoxCaja.append((tipo))
        G = [[] for _ in range(cantidad)]
        OrdenarTC.append((int(X)*int(Y)*int(Z)))
        for j in range(cantidad):
            G[j].append(((tipo),(int(X),int(Y),int(Z))))
            TC.append(((int(X),int(Y),int(Z)),(int(X)*int(Y)*int(Z))))
            Medidas.append((int(X),int(Y),int(Z)))    
            Areas.append((int(X)*int(Y)*int(Z)))
            
        #print(G)
    #print(TC)
    #print(Areas)
    for k in range(line):
        OrdenarS.append((OrdenarTC[k],CantidadxTipo[k],TipoxCaja[k]))
    AreaTotal = sumarareas(Areas)
    Desperdicio = 100 -((AreaTotal/volume)*100)
    Usado = 100-Desperdicio
    #print(AreaTotal)
    #print(Usado)
    
    hola =  BinPacking(Areas, volume)
    #print(Posicionar(Unificar(SepararArea(Ordenar(TC)))))
    
    
    #print(Medidas)
    #print(ordenamientoBurbuja(Areas))
    #print(Position(Areas))
    #SepararArea(Ordenar(TC))
    #print(Unificar(SepararArea(Ordenar(TC))))
    
### funciones para la cantidad y tipos

    QTV = Ordenar(OrdenarS)
    #print(QTOrdenado)
    #for l in range(len(QTOrdenado)):
        #del(QTOrdenado[i][0])
    
    QT = SepararTipo(QTV)
    #print(QT)  
    #print(QT)
 #   ---------------------
    print(posicionar(20,30,8,Unificar(SepararArea(Ordenar(TC))),QT))