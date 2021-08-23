#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main()
{
    double n, e, x, y, error;
    int i=1;

    cout << "Ingrese el dato: ";
    cin >> n;

    cout << "Ingresar la tolerancia (1e-n): ";
    cin >> e;

    cout << "Ingrese el valor inicial: ";
    cin >> x;

    cout << setprecision(64);

    y =((0.5)*(x+(n/x)));

    while ((abs(x-y))> e){
    error= abs(x-y);
    x = y;
    y =((0.5)*(x+(n/x)));

    cout << i << " Respuesta " << y << " con un error de "<< error << " Y una tolerancia de "<< e << endl;
    i ++;
    }
    cout << endl;
    cout << "El valor real de la raiz cuadrada de "<< n << " es " << sqrt(n) << endl;

    return 0;
}
