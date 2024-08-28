import sys
import glob
import serial
import threading
import queue

# https://docs.python.org/es/3/library/queue.html

data_queue = queue.Queue()
# Create and start the thread



def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def menu_ports(p_list):    
    print("Lista de puertos")
    for i in range(len(p_list)):
        print(f"{i}. {p_list[i]}")
    
def read_serial(ser, queue):
  while True:
    data = ser.readline().decode()  # Read and decode data
    # Process data (print, store in queue, etc.)
    queue.put(data)  # Example: Add data to a queue

def configure_serial(port = '', baud_rate = 9600):
    serial_object = serial.Serial(port = port, baudrate = baud_rate, timeout=.1)
    return serial_object

def setup_serial_port():
    ports = serial_ports()    
    menu_ports(ports)
    num_port = int(input("Seleccione numero del puerto al que se va a conectar: "))
    port = ports[num_port]    
    print(f"Puerto seleccionado: {port}")
    ser = configure_serial(port)
    return ser

def main():
    # Inicializacion del puerto serial
    ser = setup_serial_port()   
    # Cola para leer los datos que llegan desde el puerto serial
    data_queue = queue.Queue()
    # Crear e iniciar el hilo de lectura del serial
    read_thread = threading.Thread(target=read_serial, args=(ser, data_queue))
    read_thread.start()
    print(f"Recibiendo datos a traves del puerto {ser.port}. Presione [CTRL + C] para terminar")
    while True:
        # Check data queue (if used)
        try:   
            if not data_queue.empty():
                data = data_queue.get()
                print(f"{data}",end = '')
        except KeyboardInterrupt:
            print('Usted presiono Ctrl+C! Saliendo...')
            ser.close()
            print(f'Puerto {ser.port} Cerrado')
            sys.exit(0)

if __name__ == "__main__":
    main()

