#Parcial Johanna Bolívar Punto 3 
import math

def PuntoFijo(f, p, TOL):
    error = 1
    iteraciones = 0
    while error > TOL:
        p_new = f(p)
        error = abs(p_new - p)
        p = p_new
        iteraciones += 1
        print(f'p{iteraciones} = {p: 0.5f}')
    print(f'Raiz: {p}\nIteraciones: {iteraciones}')

if __name__ == '__main__':
    f = lambda x: (2+math.sin(x)-x)
    PuntoFijo(f, 0, 1e-5)