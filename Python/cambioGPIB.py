import serial

# Configurar el puerto serie
serial_port = "COM12"  # Cambia según sea necesario
baud_rate = 115200  # Velocidad actual
ser = serial.Serial(serial_port, baud_rate, timeout=2)
print("Conectado al dispositivo.")

def send_command(ser, cmd):
    """Envia un comando al dispositivo GPIB y muestra la respuesta"""
    ser.write((cmd + '\n').encode())  # Enviar comando
    try:
        response = ser.readline().decode().strip()  # Leer respuesta
        if response:
            print("Respuesta:", response)
        else:
            print("Comando enviado, pero sin respuesta.")
    except serial.SerialTimeoutException:
        print("Error: Tiempo de espera agotado.")

# Pedir dirección GPIB al usuario
while True:
    try:
        gpib_address = int(input("Ingresa la dirección GPIB (1-29): "))
        if 1 <= gpib_address <= 29:
            break
        else:
            print("Por favor, ingresa un número entre 1 y 29.")
    except ValueError:
        print("Entrada no válida. Ingresa un número entre 1 y 29.")

# Configurar la dirección GPIB y guardar configuración
send_command(ser, f"++addr {gpib_address}")
send_command(ser, "++savecfg")

# Mostrar información del dispositivo
send_command(ser, "++ver")
send_command(ser, "*IDN?")

# Envío de comandos en bucle
while True:
    command = input("Escribe un comando (o 'exit' para salir): ")
    if command.lower() == "exit":
        break
    send_command(ser, command)

# Cerrar el puerto
ser.close()
print("Conexión cerrada.")
