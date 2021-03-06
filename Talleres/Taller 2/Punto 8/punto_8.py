# -*- coding: utf-8 -*-
"""Punto 8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rcrvhnnbnntXTTifvXfNcx_3guoLkhLp
"""

# Punto 8 - Taller 2

import numpy as np
import scipy.linalg as la
import copy

def main():
  opc = -1

  # Primer sistema
  A_i = np.array ([ [1,-8,-2],
                    [1,1,5],
                    [3,-1,1] ])

  B_i = np.array ([ [1], 
                    [4],
                    [-2] ])
  
  B2_i = np.array ([1,4,-2])

  # Segundo sistema
  A_ii = np.array ([ [1, 4, 0],
                     [0, 1, 1],
                     [2, 0, 3] ])

  B_ii = np.array ([ [5], 
                     [2],
                     [0] ])
  
  B2_ii = np.array ([5,2,0])

  # Tercer sistema
  A_iii = np.array ([ [1, 3, -1],
                      [4, -1, 1],
                      [1, 1, 7] ])
  
  B_iii = np.array ([ [18], 
                      [27.34],
                      [16.2] ])
  
  B2_iii = np.array ([18,27.34,16.2])

  while opc > 5 or opc < 0:
    print('Seleccione el método que quiere aplicar: ')
    print('1. Gauss con pivoteo parcial')
    print('2. Gauss')
    print('3. Cramer')
    print('4. Factorización LU')
    print('5. Salir')
    opc = int(input('\nEscoja una opción: '))

  if opc == 1:
    print('\nSistema 1: \n')
    Gauss_pivoteo_parcial(A_i, B_i)
    print('\nSistema 2: \n')
    Gauss_pivoteo_parcial(A_ii, B_ii)
    print('\nSistema 3: \n')
    Gauss_pivoteo_parcial(A_iii, B_iii)

  elif opc == 2:
    print('\nSistema 1: \n')
    Gauss(A_i, B_i)
    print('\nSistema 2: \n')
    Gauss(A_ii, B_ii)
    print('\nSistema 3: \n')
    Gauss(A_iii, B_iii)

  elif opc == 3:
    print('\nSistema 1: \n')
    Cramer(A_i, B2_i)
    print('\nSistema 2: \n')
    Cramer(A_ii, B2_ii)
    print('\nSistema 3: \n')
    Cramer(A_iii, B2_iii)
  
  elif opc == 4: 
    print('\nSistema 1: \n')
    Factorizacion_LU(A_i)
    print('\nSistema 2: \n')
    Factorizacion_LU(A_ii)
    print('\nSistema 3: \n')
    Factorizacion_LU(A_iii)

  else: 
    print('Adios...')

def Gauss_pivoteo_parcial(A, B):
    # Evitar truncamiento en operaciones
    A = np.array(A,dtype=float) 

    # Matriz aumentada
    AB  = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)

    # Pivoteo parcial por filas
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]

    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna  = abs(AB[i:,i])
        dondemax = np.argmax(columna)
        
        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    AB1 = np.copy(AB)

    # eliminación hacia adelante
    for i in range(0,n-1,1):
        pivote   = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor  = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor

    # sustitución hacia atrás
    ultfila = n-1
    ultcolumna = m-1
    X = np.zeros(n,dtype=float)

    for i in range(ultfila,0-1,-1):
        suma = 0
        for j in range(i+1,ultcolumna,1):
            suma = suma + AB[i,j]*X[j]
        b = AB[i,ultcolumna]
        X[i] = (b-suma)/AB[i,i]

    X = np.transpose([X])

    xa = []
    for i in range(len(X)):
      if i > 0:
        err_delante = X[i] - X[i-1]
        xa.append(err_delante)

    # SALIDA
    print('Matriz aumentada:')
    print(AB0)
    print('Pivoteo parcial por filas')
    print(AB1)
    print('Eliminación')
    print(AB)
    print('Solución: ')
    print(X)

    Ax = np.dot(A,X)
    error_hacia_atras = np.linalg.norm(B-Ax)
    print('\tError hacia atras: ', error_hacia_atras)
    print('\tError hacia delante: ', np.linalg.norm(err_delante))
    print('\tNúmero de condición: ', np.linalg.cond(AB)) 

def Gauss(A, B):
    # Evitar truncamiento en operaciones
    A = np.array(A,dtype=float) 

    # Matriz aumentada
    AB  = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)

    # Pivoteo parcial por filas
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]

    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna  = abs(AB[i:,i])
        dondemax = np.argmax(columna)
        
        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    AB1 = np.copy(AB)

    # eliminación hacia adelante
    for i in range(0,n-1,1):
        pivote   = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor  = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor

    # sustitución hacia atrás
    ultfila = n-1
    ultcolumna = m-1
    X = np.zeros(n,dtype=float)

    for i in range(ultfila,0-1,-1):
        suma = 0
        for j in range(i+1,ultcolumna,1):
            suma = suma + AB[i,j]*X[j]
        b = AB[i,ultcolumna]
        X[i] = (b-suma)/AB[i,i]

    X = np.transpose([X])

    xa = []
    for i in range(len(X)):
      if i > 0:
        err_delante = X[i] - X[i-1]
        xa.append(err_delante)

    # SALIDA
    print('Matriz aumentada:')
    print(AB0)
    # print('Pivoteo parcial por filas')
    # print(AB1)
    print('Eliminación')
    print(AB)
    print('Solución: ')
    print(X)

    Ax = np.dot(A,X)
    error_hacia_atras = np.linalg.norm(B-Ax)
    print('\tError hacia atras: ', error_hacia_atras)
    print('\tError hacia delante: ', np.linalg.norm(err_delante))
    print('\tNúmero de condición: ', np.linalg.cond(AB)) 
    
def Cramer(d,b):
    if d.shape[0]!=d.shape[1]:
        print('¡Esta matriz no es una matriz cuadrada! ')
        return
    if det(d) == 0:
        print('Coeficiente de matriz cuadrada es 0')
        return
    d_i = []
    for i in range(b.shape[0]):
        d_i.append(copy.deepcopy(d))
        d_i[i][:,i] = b
        pass
    x = []
    for i in range(b.shape[0]):
      x.append(det(d_i[i]) / det(d))
    print('Solucion: ')
    print(x)

    xa = []
    for i in range(len(x)):
      if i > 0:
        err_delante = x[i] - x[i-1]
        xa.append(err_delante)

    Ax = np.dot(d,x)
    error_hacia_atras = np.linalg.norm(b-Ax)
    print('\tError hacia atras: ', error_hacia_atras)
    print('\tError hacia delante: ', np.linalg.norm(err_delante))
    print('\tNúmero de condición: ', np.linalg.cond(d)) 

# Arreglo completo
def permutations(n):
    arr = [x for x in range(n)]
    result =[]
    dfs(arr,0,len(arr),result)
    return result

def dfs(arr, begin, end,result):
    if begin == end:
        result.append(copy.deepcopy(arr))
        pass
    else:
        for i in range(begin,end):
            arr[i],arr[begin] = arr[begin],arr[i]
            dfs(arr,begin+1,end,result)
            arr[i],arr[begin] = arr[begin],arr[i]
            pass
        pass

# Número inverso
def inverse(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                count+=1
                pass
            pass
        pass    
    return count

def det(matrix):
    if matrix.shape[0]!=matrix.shape[1]:
        print('¡Esta matriz no es una matriz cuadrada! ')
        return
    permutation = permutations(matrix.shape[0])
    permutation = np.array(permutation)
    result = 0
    for i in range(len(permutation)):
        a = 1
        for j in range(matrix.shape[0]):
            a*=matrix[j][permutation[i][j]]
        result += pow(-1,inverse(permutation[i]))*a
    return result

def Factorizacion_LU(A):
    P, L, U = la.lu(A)
    print('Matriz L: \n', L)
    print('Matriz U: \n', U)

    # A = LU
    LU = L @ U
    print('Matriz LU: \n', LU)

    print('\n\tNúmero de condición: ', np.linalg.cond(LU))

main()