# Principal|


import heapq as hq
import math


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
    #print(arreglo)
 
    #print(Cantidad)  
    x = arreglo[(Cantidad[0]*3)-3]
    #print(x)
    w = arreglo[(Cantidad[0]*3)-2]  #19
    #print(w)
    #print(Cantidad)
    for i in range(len(Cantidad)):
        if Contador == i:
            
            for j in range(int(Cantidad[0])-1):
                if z <= altoz:
                    resultado.append(([0,0,z],Tipo[0]))
                    z += arreglo[2]
                    #x = arreglo[Cantidad[0]]
                
                   # print((Cantidad[i]*3)+2)
                if z > altoz:
                    resultado.append(([0,w,z3],Tipo[0]))
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
                    resultado.append(([x,0,z],Tipo[1]))
                    z += arreglo[(Cantidad[0]*3)+2]
                    #x = arreglo[Cantidad[0]]
                
                   # print((Cantidad[i]*3)+2)
                if z > altoz:
                    resultado.append(([x,w2,z4],Tipo[1]))
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
                    resultado.append(([x3,0,z],Tipo[2]))
                    z += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3))+2]
                    #x = arreglo[Cantidad[0]]
                
                   # print((Cantidad[i]*3)+2)
                if z > altoz:
                    resultado.append(([x3,w3,z5],Tipo[2]))
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
                    resultado.append(([x4,0,z],Tipo[3]))
                    z += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3))+2]
                    #x = arreglo[Cantidad[0]]
                
                   # print((Cantidad[i]*3)+2)
                if z > altoz:
                    resultado.append(([x4,w4,z6],Tipo[3]))
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
                    resultado.append(([x5,0,z],Tipo[4]))
                    z += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3))+2]
                    #x = arreglo[Cantidad[0]]
                
                   # print((Cantidad[i]*3)+2)
                if z > altoz:
                    resultado.append(([x5,w5,z7],Tipo[4]))
                    z7+=arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3))+2]
                    if z7 > altoz:
                        w5 += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3))+1]
                        z7 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3))+2]
                    if w5 > anchoy:
                        break
        
        '''if Contador6 == i+5:
            x6 = arreglo[0]+ arreglo[(Cantidad[0]*3)]+arreglo[(Cantidad[1]*3)]+arreglo[(Cantidad[2]*3)]+arreglo[(Cantidad[3]*3)+2]
            z = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3)+(Cantidad[4]*3))+2]
            z8 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3)+(Cantidad[4]*3))+2]
            w6 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3)+(Cantidad[4]*3))+1]
            #print(z4)
            #print(arreglo[(Cantidad[0]*3)+2])
            for j in range(int(Cantidad[5])-1):
                if z <= altoz:
                    resultado.append(([x6,0,z],Tipo[5]))
                    z += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3)+(Cantidad[4]*3))+2]
                    #x = arreglo[Cantidad[0]]
                
                   # print((Cantidad[i]*3)+2)
                if z > altoz:
                    resultado.append(([x6,w6,z8],Tipo[5]))
                    z7+=arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3)+(Cantidad[4]*3))+2]
                    if z8 > altoz:
                        w6 += arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3)+(Cantidad[4]*3))+1]
                        z8 = arreglo[((Cantidad[0]*3)+(Cantidad[1]*3)+(Cantidad[2]*3)+(Cantidad[3]*3)+(Cantidad[4]*3))+2]
                    if w5 > anchoy:
                        break''' 

        
     
        
    
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
    CantidadTipo = []
 
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
        print("Tipo de paquete",T," y sus dimensiones")
        print(G)
    #print(TC)
    #print(Areas)
    for k in range(line):
        OrdenarS.append((OrdenarTC[k],CantidadxTipo[k],TipoxCaja[k]))
        CantidadTipo.append((CantidadxTipo[k],TipoxCaja[k]))
    AreaTotal = sumarareas(Areas)
    Desperdicio = 100 -((AreaTotal/volume)*100)
    Usado = 100-Desperdicio
    #print(AreaTotal)
    #print(Usado)
    
    #print(Posicionar(Unificar(SepararArea(Ordenar(TC)))))
    
    
    
    ### funciones para la cantidad y tipos

    QTV = Ordenar(OrdenarS)
  
    
    QT = SepararTipo(QTV)
    #print(Areas)
    print("Dimensiones del Contenedor x, y, z")
    print("X = ",contenedor1, " - Y = ",contenedor2," - Z = ",contenedor3)
    print("Cantidad de cada tipo de paquete")
    print(CantidadTipo)  
    

    #print(QT)
 #   ---------------------
    #print(posicionar(20,30,8,Unificar(SepararArea(Ordenar(TC))),QT))
    print("---------------")
    print("Volumen total del contenedor:",volume)
    print("Volumen total de los paquetes: ",AreaTotal)
    print("Espacio de desperdicio: ",Desperdicio,"%")
    print("UBICACIÓN DE LOS PAQUETES")
    for line in posicionar(contenedor1,contenedor2,contenedor3,Unificar(SepararArea(Ordenar(TC))),QT):
        print(line)