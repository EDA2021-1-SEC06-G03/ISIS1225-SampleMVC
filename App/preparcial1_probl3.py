import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import queue as qu
from DISClib.ADT import stack as stk
assert cf

def binario_a_pila(N: int):
    if N > 0 :
        pila = stk.newStack()
        while N > 0 :
            stk.push(pila, N % 2)
            N = N//2
        resp = pila
    else:
        resp = None
    return resp

def pasar_lista_p(N : int):
    binario = binario_a_pila(N)
    tamaño = stk.size(binario)
    i = 0
    lista_p = []
    while i < tamaño :
        lista_p.append(str(stk.pop(binario)))
        i += 1
    return lista_p


def consola():
    N = int(input('Dame el N \n'))
    final_list = pasar_lista_p(N)
    final_str = ''.join(final_list)
    print(final_str)
while True:
    consola()