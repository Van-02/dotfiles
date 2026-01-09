### Diseñar un algoritmo que ayude al personal de ventas a realizar el calculo de los intereses sobre un producto, cuando un cliente intenta pagar en cuotas con alguna tarjeta que acepte el comercio. Las tarjetas aceptadas son 3 y con estas se pueden abonar en 3, 6, y 12 cuotas. Se aclaran los recargos para cada una de las opciones. Para la primer tarjeta 3 pagos con 4% mensual, 6 pagos 4% mensual y 12 pagos 5% mensual. Para la segunda tarjeta 3 pagos con 3% mensual, 6 pagos 4% mensual y 12 pagos 5% mensual. Para la tercer tarjeta 3 pagos con 3.8% mensual, 6 pagos 5% mensual y 12 pagos 5.3% mensual. Para el caso seleccionado, debera mostrar la tasa de financiacion mensual, la tasa anual (tasa mensual x12) y el valor del producto aplicado los intereses correspondientes.

```Pseudocodigo
Algoritmo Calculo_Intereses_Cuotas
    Definir monto, tasa_mensual, tasa_anual, monto_final Como Real
    Definir tarjeta, cuotas Como Entero

    Escribir "Ingrese el valor del producto:"
    Leer monto

    Escribir "Seleccione la tarjeta (1, 2 o 3):"
    Leer tarjeta

    Escribir "Seleccione cantidad de cuotas (3, 6 o 12):"
    Leer cuotas

    Si tarjeta = 1 Entonces
        Si cuotas = 3 Entonces tasa_mensual <- 4.0 Sino
        Si cuotas = 6 Entonces tasa_mensual <- 4.0 Sino
        Si cuotas = 12 Entonces tasa_mensual <- 5.0 FinSi
    Sino Si tarjeta = 2 Entonces
        Si cuotas = 3 Entonces tasa_mensual <- 3.0 Sino
        Si cuotas = 6 Entonces tasa_mensual <- 4.0 Sino
        Si cuotas = 12 Entonces tasa_mensual <- 5.0 FinSi
    Sino Si tarjeta = 3 Entonces
        Si cuotas = 3 Entonces tasa_mensual <- 3.8 Sino
        Si cuotas = 6 Entonces tasa_mensual <- 5.0 Sino
        Si cuotas = 12 Entonces tasa_mensual <- 5.3 FinSi
    FinSi

    tasa_anual <- tasa_mensual * 12
    monto_final <- monto * (1 + (tasa_mensual / 100) * cuotas)

    Escribir "Tasa Mensual: ", tasa_mensual, "%"
    Escribir "Tasa Anual: ", tasa_anual, "%"
    Escribir "Monto final con intereses: $", monto_final
    Escribir "Valor de cada cuota: $", monto_final / cuotas
FinAlgoritmo
```
