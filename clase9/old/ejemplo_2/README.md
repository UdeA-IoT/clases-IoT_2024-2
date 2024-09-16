# Ejemplo 2

## Componentes

A continuación se muestran las partes del ejemplo 2:
* Interfaz grafica ([link](interfaz/README.md))
* **Thing 1** ([link](thing_01/README.md))
* **Thing 2** ([link](thing_02/README.md))

> **En construcción**: 
> Disculpe las molestias causadas...

Ensayos con la interfaz usando malicia indigena:

```
mosquitto_pub -t home -m hola
mosquitto_pub -t home -m hola
mosquitto_pub -t home -m 0,1
mosquitto_pub -t home -m 0,2
mosquitto_pub -t home -m 1,2
mosquitto_pub -t home -m 2,2
mosquitto_pub -t home -m 2,234
mosquitto_pub -t home -m 3,0
mosquitto_pub -t home -m 3,1
mosquitto_pub -t home -m 3,0
mosquitto_pub -t home -m 3,100
mosquitto_pub -t home -m 2,100
mosquitto_pub -t home -m 4,100
mosquitto_pub -t home -m 2,2
mosquitto_pub -t home -m 1,2
mosquitto_pub -t home -m 0,2
mosquitto_pub -t home -m 0,1
mosquitto_pub -t home -m 0,0
mosquitto_pub -t home -m 0,2
```