from claseGPIB_Arduino import GPIB_Interface
import numpy as np
import matplotlib.pyplot as plt
import time
from conf_SA_RyS_FSP40 import obtener_datos

# Dentro de este codigo se ajustan diferentes parametros para la visualizacion adecuada
# de un analizador de espectros "Rohde&Schwarz FSP40" con la finalidad de que el usuario
# pueda configurarlo a su gusto 
# Posteriormente guardar y graficar los datos (puntos) que se tomen del analizador
# estos datos y graficas corresponden a la frecuencia(X) v potencia en dBm(Y)
# Importante tener descargada la funcion (script) "conf_SA_RyS_FSP40" para un correcto funcionamiento#

if __name__ == "__main__":
    
    inst = GPIB_Interface(address="GPIB::7::INSTR", serial_port="COM12")
    #configuracion(inst)
    obtener_datos(inst)
    inst.close() #cerrar la conexion para "desocupar el puerto" y ocuparlo nuevamente en este codigo
    inst = GPIB_Interface(address="GPIB::7::INSTR", serial_port="COM12")

    # Configuración de frecuencia y span
    fcenter = float(inst.query("FREQ:CENT?"))
    time.sleep(1.5)
    fspan = float(inst.query("FREQ:SPAN?"))
    time.sleep(1.5)
    puntos=int(inst.query("SWE:POIN?"))

    # Configuración del barrido
    inst.write("SENS:SWE:COUN 1")  # Un barrido
    time.sleep(1.5)
    # Configuración del ancho de banda
    inst.write("BAND:AUTO OFF")
    time.sleep(1.5)

    # Iniciar adquisición de datos
    print("Iniciando adquisición de datos...")
    inst.write("INIT:IMM;*WAI")
    time.sleep(1.5)
    inst.write("FORM ASC")  # Formato en ascci
    time.sleep(1.5)
    meas=inst.query("TRAC:DATA? TRACE1;*WAI")
    #print(meas)

    # Leer datos 
    time.sleep(1)
    
    try:
        data = np.array(meas.split(','), dtype=np.float32)

    except ValueError:
        print("Error al convertir los datos. Verifica el formato de salida del analizador.")
        inst.close()
        exit()

    #Leer datos en binario, para esto hay que modificar la clase "GPIB_Interface"
    #data = inst.read_binary_values(datatype='f', is_big_endian=True)
    #data = np.array(data)

    # Configuración del eje de frecuencia
    fstart = fcenter - fspan / 2
    fstop = fcenter + fspan / 2
    resolution = fspan / puntos
    frequencies = np.linspace(fstart,fstop,puntos)
    Mark=((puntos/2)-.5)
    centMark=int(Mark)

    #Marker
    print("Marker")
    print(data[centMark]," dBm")
    print(frequencies[centMark]," Hz")

    # Guardar datos en un archivo CSV
    np.savetxt("datos_analizador251.csv", np.column_stack((frequencies, data)), delimiter=",", header="Frecuencia (Hz),  dBm", comments="")
    print("Datos guardados en 'datos_analizador251.csv'")
    
    # Graficar los datos adquiridos
    plt.plot(frequencies, data)
    plt.title("Adquisición de espectro SA")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Potencia (dBm)")
    plt.grid(True)
    plt.show()

    # Cerrar conexión
    inst.close()
