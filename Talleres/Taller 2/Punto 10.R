### Sistemas No lineales  
### 10.
### Determinar numéricamente la intersección entre la circunferencia $x^2 + y^2 = 1$ y la recta $y = x$. Usamos una aproximación inicial $(1,1)$.   

### - **Solución:**El paquete de R ('BB') se encarga de resolver y optimizar sistemas de ecuaciones no lineales, la funcion BBsolve nos permite encontrar las intersecciones de las ecuaciones propuestas dada una aproximación lineal. Para la solución de este problema pasamos las ecuaciones a una función que sería el sistema de ecuaciones no lineales en base a los pasos que nos muestra HELP de la función.

```{r}
library(BB)
re<-c(1,1)

sistem=function(x){
  n<-length(x)
  f<-rep(NA, n)
  f[1] = (x[1]^2)+(x[2]^2)-1
  f[2] = (x[1])-(x[2])
  f
}
sol=BBsolve(re, sistem)
sol$par
```

