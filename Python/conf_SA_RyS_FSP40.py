import time
from claseGPIB_Arduino import GPIB_Interface

#if __name__ == "__main__":
#   inst = GPIB_Interface(address="GPIB::7::INSTR", serial_port="COM12")

def obtener_respuesta(mensaje):
    while True:
        respuesta = input(mensaje).strip().upper()
        if respuesta in ["Y", "N"]:
            return respuesta
        print("Por favor, responda con 'Y' o 'N'.")

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

def obtener_datos(inst):
    print("Kilo 'K' = valor+E3")
    print("Mega 'M' = valor+E6")
    print("Giga 'G' = valor+E9")

        # Datos de frecuencia
    while True:
        try:
            freq= float(input("Ingrese el valor de frecuencia central (Hz): "))
            if 9E3<=freq<=40E9:
                            #print(f"frecuencia central = {freq} Hz")
                    freqHz = inst.write(f"FREQ:CENT {freq}") 
                    time.sleep(1.5)
                    mfreq = inst.query("FREQ:CENT?")
                    print("Frecuencia medida:", mfreq," Hz")
                    if obtener_respuesta(f"Frecuencia= {float(freq)}, ¿es correcta? (Y/N): ") == "N":
                        continue 
                    break
            else:
                print("Fuera de limite: 9KHz a 40GHz")
        except ValueError:
            print("Intente de nuevo")


        # Pedir el numero de puntos "sweep points"
    while True:
            try:
                points= float(input("Ingrese el numero de puntos (Sweep points): "))
                if 125<=points<=8001: 
                    #print(f"Numero de puntos = {points} ")
                    sweep_points = inst.write(f"SWE:POIN {points}") 
                    time.sleep(1.5)
                    m_npoints = inst.query("SWE:POIN?")
                    print("Numero de puntos ajustado:", m_npoints)
                    if obtener_respuesta(f"Puntos= {float(m_npoints)}, ¿es correcto? (Y/N): ") == "N":
                        continue
                    break
                else:
                    print("Fuera de limite: 125 a 8001")
            except ValueError:
                print("Intente de nuevo")
        

        # Pedir el valor de SPAN
    while True:
        try:
            span= float(input("Ingrese el valor de 'SPAN' (Hz): "))
            if 0<=span<=40E9:
                #print(f"SPAN = {span} Hz")
                spanHz = inst.write(f"FREQ:SPAN {span}") 
                time.sleep(1.5)
                mspan = inst.query("FREQ:SPAN?")
                print("Frecuencia SPAN:", mspan," Hz")
                if obtener_respuesta(f"Frecuencia SPAN= {float(mspan)}, ¿es correcta? (Y/N): ") == "N":
                    continue 
                break
            else:
                print("Fuera de limite: 0Hz a 40GHz")
        except ValueError:
            print("Intente de nuevo")

        # Pedir el valor del nivel de referencia
    while True:
        try:
            ampt= float(input("Ingrese el nivel de referencia (dBm): "))
            if -130<=ampt<=30:
                #print(f"nivel de referencia= {ampt} dBm")
                reflev = inst.write(f"DISP:WIND:TRAC:Y:RLEV {ampt}") 
                time.sleep(1.5)
                mampt = inst.query("DISP:WIND:TRAC:Y:RLEV?")
                print("Nivel de referencia:", mampt, " dBm")
                if obtener_respuesta(f"Nivel de referencia ajustado= {float(mampt)}, ¿es correcto? (Y/N): ") == "N":
                    continue 
                break
            else:
                print("Fuera de limite: -130dBm a 30dBm")
        except ValueError:
            print("Intente de nuevo")
        

        # Pedir el valor de la resolucion de ancho de banda
    while True:
        try:
            RBW= float(input("Ingrese el valor de RBW (Hz): "))
            if 10<=RBW<=10E6:
                #print(f"RBW = {RBW} Hz")
                RBWMHz = inst.write(f"BAND:RES {RBW}") 
                time.sleep(1.5)
                mrbw = inst.query("BAND:RES?")
                print("frecuencia de RBW aproximada:", mrbw, " Hz")
                if obtener_respuesta(f"Frecuencia RBW= {float(mrbw)}, ¿es correcta? (Y/N): ") == "N":
                    continue 
                break
            else:
                print("Fuera de limite: 10Hz a 10KHz")
        except ValueError:
            print("Intente de nuevo")
        
        
        # Pedir el valor de video bandwidth
    while True:
        try:
            VBW= float(input("Ingrese el valor de VBW (Hz): "))
            if 10<=VBW<=10E6:
                VBWHz = inst.write(f"BAND:VID {VBW}") 
                time.sleep(1.5)
                mvbw = inst.query("BAND:VID?")
                print("Frecuencia de VBW aproximada:", mvbw," Hz")
                if obtener_respuesta(f"Frecuencia VBW= {float(mvbw)}, ¿es correcta? (Y/N): ") == "N":
                    continue 
                break
            else:
                print("Fuera de limite: 10Hz a 10KHz")
        except ValueError:
            print("Intente de nuevo")
            print(f"VBW = {VBW} Hz")
        
    inst.write("SYST:LOCal")  # Salir del control remoto
    inst.close()

#obtener_datos()