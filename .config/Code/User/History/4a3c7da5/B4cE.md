# De un ejemplo pequeño de codigo, con una funcion o procedimiento que tenga variables locales y globales.

```Python
# VARIABLE GLOBAL
# Está fuera de las funciones y es accesible para todo el programa.
tienda_nombre = "Tech Store"

def realizar_venta(cantidad_vendida):
    # VARIABLE LOCAL
    # Solo existe dentro de esta función durante la ejecución de la venta.
    precio_unidad = 50.0
    total_venta = cantidad_vendida * precio_unidad

    # Acceso a la variable global (lectura)
    print(f"--- Factura de {tienda_nombre} ---")
    print(f"Cantidad: {cantidad_vendida}")
    print(f"Total a cobrar: ${total_venta}")
    print("--------------------------------")

# Ejecución
realizar_venta(3)

# Intento de acceso externo (Dará Error)
# print(total_venta)  # NameError: name 'total_venta' is not defined
```
