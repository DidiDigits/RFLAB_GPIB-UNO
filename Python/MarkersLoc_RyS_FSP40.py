import time
from claseGPIB_Arduino import GPIB_Interface

# 26 de marzo de 2025
# Dentro de este programa ubicaremos o leeremos datos de los markers en el analizador de espectros
# En este caso de un "ROHDE&SCHWARZ FSP 40"
# El usuario ingresa una letra para ubicar o leer un marker
# se abren algunas opciones para markers, seleccionar el marker deseado con su numero
# Recordar: se debe cambiar la direccion GPIB y el puerto serial para un correcto funcionamiento#

#Envio de comandos, se establece la direccion y/o puerto
if __name__ == "__main__":
    inst = GPIB_Interface(address="GPIB::7::INSTR", serial_port="COM12")
    #inst.write("SYST:REMote")  # tomar control remoto, descomentar si no lo toma automaticamente
    # se toman las medidas para limitar la ubicacion de los markers y mostrar solo los de la pantalla
    fcenter = float(inst.query("FREQ:CENT?"))
    time.sleep(1.5)
    fspan = float(inst.query("FREQ:SPAN?"))
    time.sleep(1.5)
    fstart = fcenter - fspan / 2
    fstop = fcenter + fspan / 2
    
    def obtener_respuesta(mensaje):
        while True:
            respuesta = input(mensaje).strip().upper()
            if respuesta in ["Y", "N"]:
                return respuesta
            print("Por favor, responda con 'Y' o 'N'.")

    def obtener_opcion(mensaje):
        while True:
            respuesta = input(mensaje).strip().upper()
            if respuesta in ["U", "L"]:
                return respuesta
            print("Por favor, responda con 'U' o 'L'.")

    def obtener_numero(mensaje):
        while True:
            try:
                numero = float(input(mensaje))
                if numero > 0:
                    return numero
                else:
                    print("Por favor, ingrese un número válido.")
            except ValueError:
                print("Entrada no válida. Intente de nuevo.")

    #Funcion para activar y ubicar los markers
    def actmarker(opcion):
        while True:
            try:
                freq= float(input("Ingrese el valor de frecuencia (Hz): "))
                if fstart<=freq<=fstop:
                        #print(f"frecuencia central = {freq} Hz")
                        
                        inst.write(f"CALC:MARK{(opcion)}:X {(freq)}")
                        time.sleep(1.5)
                        if obtener_respuesta(f"Frecuencia= {float(freq)}, ¿es correcta? (Y/N): ") == "N":
                            continue 
                        print(f"Potencia del marker {(opcion)}= ",inst.query(f"CALC:MARK{(opcion)}:Y?")," dBm")
                        time.sleep(1.5)
                        print(f"Frecuencia del marker {(opcion)}= ",inst.query(f"CALC:MARK{(opcion)}:X?")," Hz")
                        time.sleep(1.5)
                        break                
                else:
                    print("Fuera de limite en pantalla")
            except ValueError:
                print("Intente de nuevo")

    # Funcion para localizar los markers y tomar lecturas
    def locmarker(opcion):
        time.sleep(1.5)
        print(f"Potencia del marker {(opcion)}= ",inst.query(f"CALC:MARK{(opcion)}:Y?")," dBm")
        time.sleep(1.5)
        print(f"Frecuencia del marker {(opcion)}= ",inst.query(f"CALC:MARK{(opcion)}:X?")," Hz")

    # Opciones
    print("Para ubicar manualmente un marker presione U")
    print("Para leer datos de un marker presione L")
    if  obtener_opcion("Opcion seleccionada: ") == "U":
        while True:
            print("\n Opciones para ubicar marcador:")
            print("1. MARKER 1")
            print("2. MARKER 2")
            print("3. MARKER 3")
            print("4. MARKER 4")
            print("5. Salir")
            opcion = input("Presiona un numero: ")

            if opcion == "1":
                #comando = input("Ingrese el comando a enviar: ")
                inst.write("CALC:MARK1:STAT ON")
                actmarker(opcion)

            elif opcion == "2":
                inst.write("CALC:MARK2:STAT ON")
                actmarker(opcion)

            elif opcion == "3":
                inst.write("CALC:MARK3:STAT ON")
                actmarker(opcion)

            elif opcion == "4":
                inst.write("CALC:MARK4:STAT ON")
                actmarker(opcion)

            elif opcion == "5":
                print("Cerrando conexión...")
                inst.write("SYST:LOCal")  #salir del control remoto
                inst.close()
                break

            else:
                print("Opción inválida. Intente de nuevo.")
    else:
        while True:
            print("\n Opciones para leer datos del marcador:")
            print("1. MARKER 1")
            print("2. MARKER 2")
            print("3. MARKER 3")
            print("4. MARKER 4")
            print("5. Salir")
            opcion = input("Presiona un numero: ")

            if opcion == "1":
                #comando = input("Ingrese el comando a enviar: ")
                inst.write("CALC:MARK1:STAT ON")
                locmarker(opcion)

            elif opcion == "2":
                inst.write("CALC:MARK2:STAT ON")
                locmarker(opcion)

            elif opcion == "3":
                inst.write("CALC:MARK3:STAT ON")
                locmarker(opcion)

            elif opcion == "4":
                inst.write("CALC:MARK4:STAT ON")
                locmarker(opcion)

            elif opcion == "5":
                print("Cerrando conexión...")
                inst.write("SYST:LOCal")  #salir del control remoto
                inst.close()
                break

            else:
                print("Opción inválida. Intente de nuevo.")

    inst.close()