import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import queue as qu
from DISClib.ADT import stack as stk
assert cf


def cola_to_pila(cola):
    tamaño = qu.size(cola)
    pila = stk.newStack()
    i = 0
    while i < tamaño:
        stk.push(qu.dequeue(cola))
        i += 1
    return pila

def pila_to_cola(pila):
    tamaño = stk.size(pila)
    cola = qu.newQueue()
    i = 0
    while i < tamaño:
        qu.enqueue(stk.pop(pila))
        i += 1
    return cola


def voltear_cola(cola):
    cola_nueva = pila_to_cola(cola_to_pila(cola))
    return cola_nueva

def cola_to_plist_no_reuse(cola):
    tamaño = qu.size(cola)
    i = 0
    lista_p = []
    while i < tamaño:
        lista_p.append(qu.dequeue(cola))
        i += 1
    return lista_p

def cola_to_plist_reuse(cola):
    tamaño = qu.size(cola)
    i = 0
    lista_p = []
    while i < tamaño:
        lista_p.append(qu.peek(cola))
        i += 1
    return lista_p

