from claseGPIB_Arduino import GPIB_Interface


#Envio de comandos, se establece la direccion y/o puerto
if __name__ == "__main__":
    inst = GPIB_Interface(address="GPIB::7::INSTR", serial_port="COM12")
    inst.write("SYST:REMote")  #salir del control remoto
# Se realizó un ciclo (bucle) while para que el usuario pueda enviar comandos 
# las veces que lo requiera
# En la terminal se describen las opciones, el usuario elige un numero y presiona ENTER
# Revisar: existen diferentes tipos de comandos (write, read, query)
# El usuario debe saber que comando utilizar

    while True:
        print("\nOpciones:")
        print("1. Enviar un comando (write)")
        print("2. Leer respuesta del instrumento (read)")
        print("3. Enviar un comando y leer respuesta (query)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            comando = input("Ingrese el comando a enviar: ")
            inst.write(comando)
            print("Comando enviado.")

        elif opcion == "2":
            respuesta = inst.read()
            print("Respuesta del instrumento:", respuesta)

        elif opcion == "3":
            comando = input("Ingrese el comando para query: ")
            respuesta = inst.query(comando)
            print("Respuesta:", respuesta)

        elif opcion == "4":
            print("Cerrando conexión...")
            inst.write("SYST:LOCal")  #salir del control remoto
            inst.close()
            break

        else:
            print("Opción inválida. Intente de nuevo.")