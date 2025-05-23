# Comunicacion con GPIB o Arduino, la deteccion se hace automaticamente
# Considerando que el usuario sabe la dirección GPIB y el puerto que está utilizando
import pyvisa
import serial
import time
class GPIB_Interface:
    def __init__(self, address="GPIB::7::INSTR", serial_port="COM12", baudrate=115200):
        """Intenta conectarse primero a GPIB-USB, si falla, usa Arduino (AR488)."""
        self.inst = None
        self.use_serial = False  # Por defecto, asumimos que estamos usando GPIB-USB

        try:
            # Intentar conexión con GPIB-USB
            rm = pyvisa.ResourceManager()
            self.inst = rm.open_resource(address)
            self.inst.timeout = 5000  # Configurar timeout en ms
            print("Conectado a GPIB-USB.")
        except Exception as e:
            # Si falla, intentar con Arduino (AR488)
            try:
                self.inst = serial.Serial(serial_port, baudrate, timeout=1)
                time.sleep(2)  # Espera a que Arduino se inicialice
                self.use_serial = True
                print("Conectado a AR488 (Arduino).")
            except serial.SerialException as se:
                print(f"Error al abrir el puerto serial: {se}")

    def write(self, command):
        """Escribe un comando en GPIB o Serial."""
        if self.inst:
            if self.use_serial:
                self.inst.write(f"{command}\n".encode())  # Convertir string a bytes
            else:
                self.inst.write(command)
        else:
            print("No hay conexión establecida.")

    def read(self):
        """Lee la respuesta del instrumento."""
        if self.inst:
            if self.use_serial:
                return self.inst.readline().decode().strip()
            else:
                return self.inst.read()
        return "No hay conexión."

    def query(self, command):
        """Envía un comando y devuelve la respuesta."""
        self.write(command)
        return self.read()

    def close(self):
        """Cierra la conexión."""
        if self.inst:
            self.inst.close()
