# Diseñar un algoritmo que permita aplicar un descuento del 10% al monto total de una compra si la forma de pago empleada es mediante debito, 13% si la compra la realiza mediante pago contado-efectivo o aumente en un 4% si es un solo pago y se realiza en pago con tarjeta. El usuario debera ingresar el monto de la compra realizada y la forma de pago utilizada. Si es debito o efectivo, debera aplicar el descuento, sino realizar el recargo correspondiente.

```Pseudocodigo
Algoritmo Descuento_Recargo_Compra
    Definir monto, monto_final Como Real
    Definir forma_pago Como Entero

    Escribir "Ingrese el monto total de la compra:"
    Leer monto

    Escribir "Seleccione la forma de pago:"
    Escribir "1 - Débito (10% descuento)"
    Escribir "2 - Contado-Efectivo (13% descuento)"
    Escribir "3 - Tarjeta (1 solo pago, 4% recargo)"
    Leer forma_pago

    Segun forma_pago Hacer
        1:
            monto_final <- monto * 0.90
        2:
            monto_final <- monto * 0.87
        3:
            monto_final <- monto * 1.04
        De Otro Modo:
            Escribir "Forma de pago no válida."
            monto_final <- monto
    Fin Segun

    Escribir "El monto final a pagar es: $", monto_final
FinAlgoritmo
```
