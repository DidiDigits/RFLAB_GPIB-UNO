import serial
import time

def gpib_uno_console():
    """Main function to set up the GPIB-UNO connection and send manual commands.
    This function initializes the serial connection, finds the GPIB address,
    configures the device, and enters a loop to send commands to the device.
    """
    
    # Configure the serial port
    serial_port = "COM3"    # Serial port for Arduino GPIB controller. Change according to your setup.
    baud_rate = 115200  # Baud rate for Arduino GPIB
    ser = serial.Serial(serial_port, baud_rate, timeout=2)
    print("Conectado a GPIB-UNO.")

    # Automatically find GPIB address
    gpib_address = find_gpib_address(ser)
    print(f"Usando dirección GPIB: {gpib_address}")

    # Configure the GPIB address and save configuration
    send_command(ser, f"++addr {gpib_address}")
    send_command(ser, "++savecfg")

    # Display device information
    send_command(ser, "++ver")
    send_command(ser, "*IDN?")

    # Sending commands in a loop
    send_commands_loop(ser)

    # Close the port
    ser.close()
    print("Conexión cerrada.")


def find_gpib_address(ser):
    """Scan GPIB addresses to find the correct one."""
    for address in range(1, 30):
        ser.write((f"++addr {address}\n").encode())
        ser.write("*IDN?\n".encode())
        time.sleep(0.5)  # Allow time for response
        response = ser.readline().decode().strip()
        if response:
            print(f"Dispositivo encontrado en dirección GPIB {address}: {response}")
            return address
    raise RuntimeError("No se encontró ningún dispositivo en las direcciones GPIB disponibles. Para conectar con GPIB-UNO verifique que la dirección GPIB del instrumento es un número entre 1 y 29.")

def send_command(ser, cmd):
    """Sends a command to the GPIB device and displays the response"""
    ser.write((cmd + '\n').encode())  # Send command
    try:
        response = ser.readline().decode().strip()  # Read response
        if response:
            print(f"Comando {cmd} enviado.")
            print("Respuesta:", response)
            print("########")
        else:
            print(f"Comando {cmd} enviado. Sin respuesta.")
            print("########")
    except serial.SerialTimeoutException:
        print("Error: Tiempo de espera agotado.")

def send_commands_loop(ser):
    """Loop to send commands to the GPIB device."""
    
    # Allow sending multiple commands
    while True:
        command = input("Escribe un comando (o 'exit' para salir): ")
        if command.lower() == "exit":
            break
        send_command(ser, command)


if __name__ == "__main__":
    gpib_uno_console()
