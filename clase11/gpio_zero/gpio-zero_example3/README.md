# Ejemplo 3 

## Descripción

Repita el [ejemplo 2](../gpio_example2/README.md) pero sin usar resistencia de pull-up externa.

## Hardware

La siguiente tabla muestra los componentes principales del circuito a montar:

|Item # |Cantidad |Descripción| Información|
|---|---|---|---|
|1|1|rPi (3 o 4)||
|2|1|Pulsador||

> **Archivo Fritzing** <br>
> El archivo fritzing asociado al ejemplo es [button_internal_pullUp.fzz](button_internal_pullUp.fzz)

### Esquematico

<p align = "center">
<img src = "example3_sch.png">
</p>

### Conexión

<p align = "center">
<img src = "example3_bb.png">
</p>


## Software

### Codigo

> **Rebote** </br>
> Cuando se presiona o libera un botón lo que sucede es un cambio en su estado (nivel de voltaje). Desde el punto de vista ideal este cambio debería ser instantaneo, sin embargo, en la realidad lo que sucede es una serie de oscilaciones antes de que el botón alcance un valor estable. Estas oscilaciones se conocen como rebotes (bounce).
>
> <p align = "center">
> <img src = "rebote.png">
> </p>

El archivo [gpio_zero_button_anti_db_ex3.py](gpio_zero_button_anti_db_ex3.py) contiene el código solución en el cual, la lectura del valor del botón se lleva a cabo 200 ms despues con el fin de que el valor obtenido en la lectura del boton sea el valor ya estabilizado. El código se muestra a continuación:

```py
from gpiozero import Button

buttonPin = Button(17, bounce_time=0.2) 
while True:
    if buttonPin.is_pressed:
        print("Boton presionado")
```


### Pruebas

To Do...

## Referencias

To Do...



