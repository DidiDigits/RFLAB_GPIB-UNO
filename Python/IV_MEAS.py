# BK Precision_IVMEAS
import numpy as np
import matplotlib.pyplot as plt
import time
from claseGPIB_Arduino import GPIB_Interface

# Este codigo es un ejemplo de uso para inyectar corriente en un diodo 
# y leer el voltaje del mismo desde la misma fuente para despues guardar 
# los datos de corriente asi como la lectura del voltaje y a partir de 
# estos valores graficar la "curva caracteristica del diodo"
# Para esto utilizamos una fuente de alimentacion "BK_PRECISION 9115"

if __name__ == "__main__":
# Pedir los datos al usuario    
    inst = GPIB_Interface(address="GPIB::2::INSTR", serial_port="COM12")
    corriente_inicial = float(input("Ingrese la corriente inicial (mA): "))
    corriente_final = float(input("Ingrese la corriente final (mA): "))
    num_puntos = int(input("Ingrese el número de puntos: "))
    mA_ini=(corriente_inicial/1000)
    mA_fin=(corriente_final/1000)
    # Crear vectores para almacenar los datos
    corrientes = np.linspace(mA_ini, mA_fin, num_puntos)
    voltajes = []
    inst.write("SYST:REMote")  # Tomar el control remoto}

    print(f"Corriente: {corrientes} ")
    for i in corrientes:
        inst.write(f"CURR {i}") 
        time.sleep(1.5)
        volt = inst.query("MEAS:VOLT?")
        print("voltaje:", volt)
        V = float(volt)
        voltajes.append(V)
        print(f"I = {i:.6f} A, V = {V:.3f} V")
    
    # Grafica de la curva
    plt.plot(voltajes, corrientes)
    plt.xlabel('Voltaje (V)')
    plt.ylabel('Corriente (A)')
    plt.xlim(0.55)
    plt.title('Curva característica del diodo')
    plt.grid(True)
    plt.show()

    inst.write("SYST:LOCal")  # Salir del control remoto
    inst.close() 