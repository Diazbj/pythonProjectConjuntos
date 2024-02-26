import tkinter as tk  # Importa la biblioteca Tkinter para la interfaz gráfica
from matplotlib import pyplot as plt  # Importa pyplot de matplotlib para graficar
from matplotlib_venn import venn2, venn3, venn3_circles,venn2_circles   # Importa venn2 de matplotlib_venn para dibujar diagramas de Venn
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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

def InterseccionTresConjuntos(A,B,C):
    interseccion = set()

    for elemento in A:
        if elemento in B:
            if elemento in C:
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

# Función para mostrar el diagrama de Venn de dos conjuntos en una ventana

def mostrar_venn(ventana, A, B,boton_presionado=None):
    fig = Figure(figsize=(6, 6), dpi=100)
    venn_ax = fig.add_subplot(111)
    if boton_presionado == 'A_B':
        v = venn2(subsets=[A, B], set_labels=('A', 'B'), ax=venn_ax)
    elif boton_presionado == 'B_C':
        v = venn2(subsets=[A, B], set_labels=('B', 'C'), ax=venn_ax)
    else:
        v = venn2(subsets=[A, B], set_labels=('A', 'C'), ax=venn_ax)
    v.get_label_by_id('10').set_text(A - B)
    v.get_label_by_id('11').set_text(InterseccionConjuntos(A,B))
    v.get_label_by_id('01').set_text(B - A)
    c = venn2_circles(subsets=[A, B], linestyle='dashed', ax=venn_ax)
    c[0].set_ls('solid')

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=1, columnspan=5, padx=5, pady=5)

# Función para mostrar el diagrama de Venn de tres conjuntos en una ventana
def mostrar_venn_3(ventana, A, B, C):
    fig = Figure(figsize=(6, 6), dpi=100)
    venn_ax = fig.add_subplot(111)
    v = venn3(subsets=(A, B, C,  ),
              set_labels=('A', 'B', 'C'), ax=venn_ax)
    c = venn3_circles(subsets=(A, B, C),
                      linestyle='dashed', ax=venn_ax)
    c[0].set_ls('solid')
    c[1].set_ls('solid')
    c[2].set_ls('solid')
    # Verificar si el identificador existe antes de intentar establecer el texto
    if v.get_label_by_id('100') is not None:
        v.get_label_by_id('100').set_text(A - (UnionConjuntos(B,C)))
    if v.get_label_by_id('010') is not None:
        v.get_label_by_id('010').set_text(B - (UnionConjuntos(A,C)))
    if v.get_label_by_id('001') is not None:
        v.get_label_by_id('001').set_text(C - (UnionConjuntos(A,B)))
    if v.get_label_by_id('110') is not None:
        v.get_label_by_id('110').set_text((InterseccionConjuntos(A, B) - C) if (InterseccionConjuntos(A, B) - C) else "")
    if v.get_label_by_id('101') is not None:
        v.get_label_by_id('101').set_text((InterseccionConjuntos(A,C) - B) if (InterseccionConjuntos(A,C) - B) else "")
    if v.get_label_by_id('011') is not None:
        v.get_label_by_id('011').set_text((InterseccionConjuntos(B,C) - A) if (InterseccionConjuntos(B,C) - A) else "")
    if v.get_label_by_id('111') is not None:
        v.get_label_by_id('111').set_text(InterseccionTresConjuntos(A, B, C))

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=1, columnspan=5, padx=5, pady=5)

# Función para crear la interfaz gráfica
def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Operaciones de Conjuntos")
    # Establecer un tamaño fijo para la ventana
    ventana.geometry("900x700")

    # Etiqueta y entrada para el conjunto A
    etiqueta_A = tk.Label(ventana, text="Conjunto A:")
    etiqueta_A.grid(row=0, column=0, padx=5, pady=5)
    entrada_A = tk.Entry(ventana)
    entrada_A.grid(row=0, column=1, padx=5, pady=5)

    # Etiqueta y entrada para el conjunto B
    etiqueta_B = tk.Label(ventana, text="Conjunto B:")
    etiqueta_B.grid(row=1, column=0, padx=5, pady=5)
    entrada_B = tk.Entry(ventana)
    entrada_B.grid(row=1, column=1, padx=5, pady=5)

    # Etiqueta y entrada para el conjunto C
    etiqueta_C = tk.Label(ventana, text="Conjunto C:")
    etiqueta_C.grid(row=0, column=2, padx=5, pady=5)
    entrada_C = tk.Entry(ventana)
    entrada_C.grid(row=0, column=3, padx=5, pady=5)

    # Botón para mostrar el diagrama A y B
    boton_A_B = tk.Button(ventana, text="Diagrama A y B", command=lambda: mostrar_venn(ventana, set(entrada_A.get().split(',')), set(entrada_B.get().split(',')),'A_B'))
    boton_A_B.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Botón para mostrar el diagrama B y C
    boton_B_C = tk.Button(ventana, text="Diagrama B y C", command=lambda: mostrar_venn(ventana, set(entrada_B.get().split(',')), set(entrada_C.get().split(',')),'B_C'))
    boton_B_C.grid(row=3, column=0, columnspan=10, padx=5, pady=5)

    # Botón para mostrar el diagrama A y C
    boton_A_C = tk.Button(ventana, text="Diagrama A y C", command=lambda: mostrar_venn(ventana, set(entrada_A.get().split(',')), set(entrada_C.get().split(',')),'A_C'))
    boton_A_C.grid(row=3, column=2, columnspan=10, padx=5, pady=5)

    # Botón para mostrar el diagrama A, B y C
    boton_A_By_C = tk.Button(ventana, text="Diagrama A, B y C", command=lambda: mostrar_venn_3(ventana, set(entrada_A.get().split(',')), set(entrada_B.get().split(',')), set(entrada_C.get().split(','))))
    boton_A_By_C.grid(row=3, column=4, columnspan=10, padx=5, pady=5)

    # Ejecutar el bucle principal de la interfaz gráfica
    ventana.mainloop()

# Llamar a la función para crear la interfaz
crear_interfaz()


A={1,2,3,4,5}
B={4,5,6,7}
U={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18}

inicio=1
fin=3

print("El conjunto A es: ",A)
print("El conjunto B es: ",B)
print("La union de los conjuntos es: ",UnionConjuntos(A,B))
print("La interseccion de los conjuntos es: ",InterseccionConjuntos(A,B))
print("La diferencia de A-B es: ",DiferenciaConjuntos(A,B))
print("El complemento de A es: ",ComplementoConjuntos(A,U))
print("La cardinalidad de el conjunto A es:",CalcularCardinalidad(A))
print("El subconjunto de A es: ",Subconjunto(A,inicio,fin))