# Ejemplo 4 - Aplicación para control de una ESP32 usando serial

El objetivo de esta sesión es explicar paso a paso como se construye una aplicación sencilla en Node-RED que se ejecuta en el PC y que se comunica mediante comunicación serial con un ESP32.

## Enuciado de la aplicación

Desarrolle una aplicación que permita encender y apagar un Led para el siguiente hardware:

<p align = "center">
<img src = "ESP32-serial1_bb.png">
</p>

La aplicación se conectara mediante el serial enviando dos comandos basicos para modificar el estado del led:

* **```h```**: Comando empleado para encender el Led.
* **```l```**: Comando empleado para apagar el Led.

## Prerequisitos

A continuación, se listan los ejemplos de software y hardware necesarios para llevar a cabo la implementación del proyecto.

### Hardware necesario

A continuación se muestra el harware necesario:
* **Placa ESP32**: NodeMCU ESP-32S (O similar).

### Software necesario

La siguiente tabla muestra la lista de programas necesarios para la implmentación del problema:
* **Visual Studio Code**: Entorno de desarrollo.
* **Platformio**: Complemento de Visual Studio code para la programación de placas de desarrollo.
* **Librerias de python**: Estas se listan a continuación:
  
   |Libreria|Descripción|
   |---|---|
   |pyserial|Libreria para el manejo del puerto serial|
   |kiby|Libreria para el desarrollo de interfaces graficas|

* **NodeRed**: Para la creación de una interfaz grafica amigable.

## Configurando el entorno virtual

Para este caso, se proporciona el archivo [requirements.txt](requirements.txt) con el fin de configurar el entorno de desarrollo (para mas información sobre como hacerlo puede consultar el siguiente [link](../../herramientas/entorno-virtual-python/README.md)), por ahora resumimos el procedimiento a la ejecución de los siguientes comandos:

```
mkdir env_test
cd env_test
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Desarrollo de la aplicación

La implementación de la aplicación se realizará paso a paso. A continuación se resumen los pasos para realizar esto:

1. **Implementación del firmware de la ESP32**: Inicialmente, según los requerimientos de la aplicación, lo primero que se debe hacer el codificar el programa que va a descargarse en el ESP32. Este paso se abordara en el siguiente **paso 1** ([link](paso1/README.md))
   
   <p align = "center">
   <img src = "serial_output.png">
   </p>

2. **Implementación del software de la aplicación de escritorio**: Una vez verificado el correcto funcionamiento del Firmware del arduino, se procede al desarrollo de la aplicación de escritorio. En nuestro caso se desarrollo una aplicación de escritorio usando python. En lo que respecta a la aplicación de escritorio se realizaron dos variantes:
   * **Desarrollo de la aplicación de consola**: Aplicación que pasa los comandos de control usando la terminal. Esta se tratará con detalle en el **paso 2** ([link](paso2/README.md))
  

   <p align = "center">
   <img src = "app_terminal.png">
   </p>

   * **Desarrollo de la aplicación con interfaz grafica**: Es la misma aplicación basica pero con interfaz grafica usando kivy (lo cual se vera luego) para hacer la interacción con el usuario mas agradable. Esta parte se tratará en el **paso 3** ([link](paso3/README.md))
  
   <p align = "center">
   <img src = "app_ui.png">
   </p>

3. **Desarrllo de una aplicación con interfaz grafica usando Node-RED**: En este caso, la aplicación se realizará usando [Node-RED](https://nodered.org/). El procedimiento para hacer esto se explica con mas detalle en al **paso 4** ([link](paso4/README.md))

   <p align = "center">
   <img src = "Node-RED_ui.png">
   </p>