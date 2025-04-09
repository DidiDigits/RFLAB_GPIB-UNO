import pyvisa
import serial
import time

def initialize_instrument(eq_idn, serial_port="COM3"):
    """
    Initialize the instrument using GPIB (pyvisa) first, then fallback to GPIB-UNO (pyserial).

    Parameters:
        eq_idn (str): Expected IDN string of the instrument.
        serial_port (str): Serial port for Arduino GPIB controller. Default is "COM3".

    Returns:
        object: Instrument object if connection is successful.
    """
    # Attempt GPIB connection using pyvisa
    try:
        rm = pyvisa.ResourceManager()
        resources = rm.list_resources()
        for resource in resources:
            try:
                inst = rm.open_resource(resource)
                buffer_size = (1601 * 16) + 4
                inst.timeout = 5000
                inst.chunk_size = buffer_size
                inst.clear()
                idn = inst.query('*IDN?').strip()
                print(f"Conectado a: {idn} en {resource}")
                if idn == eq_idn:
                    print(f"Instrumento correcto encontrado en {resource}")
                    return inst
                else:
                    inst.close()
            except Exception as e:
                print(f"No se pudo conectar a {resource} usando pyVisa: {e}")
    except Exception as e:
        print(f"Error al inicializar GPIB: {e}")

    # Fallback to Arduino GPIB using pyserial
    try:
        baud_rate = 115200  # Baud rate for Arduino GPIB
        ser = serial.Serial(serial_port, baud_rate, timeout=2)
        print("Conectado al dispositivo usando GPIB-UNO.")

        # Encontrar dirección GPIB automáticamente
        gpib_address = find_gpib_address(ser)
        ser.write((f"++addr {gpib_address}\n").encode())

        ser.write("*IDN?\n".encode())
        response = ser.readline().decode().strip()
        time.sleep(1)  # Allow time for response

        # Normalize and compare IDN strings
        normalized_response = response.strip().lower()
        normalized_eq_idn = eq_idn.strip().lower()
        
        if normalized_response == normalized_eq_idn:
            print("Instrumento correcto encontrado usando GPIB-UNO.")
            return ser
        else:
            print(f"IDN no coincide usando GPIB-UNO. Esperado: {normalized_eq_idn}, Recibido: {normalized_response}")
            ser.close()
    except Exception as e:
        print(f"Error al inicializar GPIB-UNO: {e}")

    raise RuntimeError("No se pudo inicializar el instrumento usando GPIB-UNO.")

def find_gpib_address(ser):
    """Scan GPIB addresses to find the correct one."""
    for address in range(1, 30):
        ser.write((f"++addr {address}\n").encode())
        ser.write(("++savecfg\n").encode())
        ser.write("*IDN?\n".encode())
        time.sleep(0.5)  # Allow time for response
        response = ser.readline().decode().strip()
        if response:
            print(f"Dispositivo encontrado en dirección GPIB {address}: {response}")
            return address
    raise RuntimeError("No se encontró ningún dispositivo en las direcciones GPIB disponibles. Para conectar con GPIB-UNO verifique que la dirección GPIB del instrumento es un número entre 1 y 29.")

if __name__ == "__main__":
    expected_idn = "HEWLETT PACKARD,8753ES,MY40001541,7.74"  # Expected IDN of the instrument
    try:
        instrument = initialize_instrument(expected_idn)
        print("Instrumento inicializado correctamente.")
    except Exception as e:
        print(f"Error al inicializar el instrumento: {e}")