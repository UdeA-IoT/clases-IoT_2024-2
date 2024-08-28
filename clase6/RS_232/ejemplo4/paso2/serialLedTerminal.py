import serial

SERIAL_PORT = 'COM7'
BAUD_RATE = 9600
ser = serial.Serial(port = SERIAL_PORT, baudrate = BAUD_RATE, timeout=.1)

def menu():
    print("Menu de control de la office " )
    print("1. Encender lampara" )
    print("2. Apagar lampara" )
    print("3. Salir de la aplicacion" )    

def lightON():
    ser.write(b'h')

def lightOFF():
    ser.write(b'l')

    
def main():
    print("SISTEMA DE CONTROL DE LA LAMPARA DE LA OFFICE")
    while True:
        menu()
        opc = input("Seleccione una opcion: ")
        if opc == '1':
            print("--> Encendiendo la lampara\n")
            lightON()     
        elif opc == '2':
            print("--> Apagando la lampara\n")
            lightOFF()
        elif opc == '3':
            ser.close()
            print("--> Chao bambino\n")
            break
        else:
            print("--> OPCION INVALIDA\n")

if __name__ == "__main__":
    main()