# send_commands.py
def send_command(ser, cmd):
    ser.write((cmd + '\n').encode())  # Enviar comando
    try:
        response = ser.readline().decode().strip()  # Leer respuesta
        if response:
            print("Respuesta:", response)
        else:
            print("Comando no reconocido o sin respuesta.")
    except serial.SerialTimeoutException:
        print("Error: Tiempo de espera agotado.")

def send_commands_loop(ser):
    # Enviar comandos de inicio
    send_command(ser, "++ver")
    send_command(ser, "*IDN?")
    
    # Permitir el envío de múltiples comandos
    while True:
        command = input("Escribe un comando (o 'exit' para salir): ")
        if command.lower() == "exit":
            break
        send_command(ser, command)
