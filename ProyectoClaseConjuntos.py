
#calcular la union de los conjuntos
def UnionConjuntos(A,B):
    union=set();

    for elemento in A:
        union.add(elemento)

    for elemento in B:
        union.add(elemento)

    return union

#Calcular la interseccion de los conjuntos
def InterseccionConjuntos(A,B):
    interseccion = set()

    for elemento in A:
        if elemento in B:
            interseccion.add(elemento)

    return interseccion

#Calcular diferencias de los conjuntos
def DiferenciaConjuntos(A,B):
    diferencia =set()

    for elemento in A:
        if  elemento not in B:
            diferencia.add(elemento)

    return diferencia

#Calcular complemento de conjuntos
def ComplementoConjuntos(A,U):
    complemento =set()
    for elemento in U:
        if elemento not in A:
            complemento.add(elemento)
    return complemento

#Calcular operaciones combinadas entre conjuntos
def CombinacionesConjuntos(A,B):
    combinaciones =set()
    return combinaciones

#Calcular Cardinalidad del conjunto
def CalcularCardinalidad(A):
    cardinalidad=len(A)

    return cardinalidad

#calcular Subconjunto
def Subconjunto(A,inicio,fin):
    subconjunto = set()
    indice = 0

    for elemento in A:
        if indice >= inicio and indice <= fin:
            subconjunto.add(elemento)
        indice += 1

    return subconjunto

#calcular conjuntos disjuntos entre dos conjuntos
def Disjuntos(A,B):
    disjunto = set()
    return disjunto


A={1,2,3,4,5}
B={4,5,6,7}
U={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18}

inicio=1
fin=3

print(A)
print(B)
print(UnionConjuntos(A,B))
print(InterseccionConjuntos(A,B))
print(DiferenciaConjuntos(A,B))
print(ComplementoConjuntos(A,U))
print(CalcularCardinalidad(A))
print(Subconjunto(A,inicio,fin))