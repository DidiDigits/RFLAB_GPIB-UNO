# **Instructions for Python**  

Brief description of each function:

### **1. gpib_uno_console.py**  
This function sets up the GPIB-UNO connection and allows users to send manual commands.
It initializes the serial connection, identifies the GPIB address, configures the device, and enters a loop to send manual commands to the instrument.

IMPORTANT: The serial and pyserial libraries are required dependencies.

---
### 2. initialize_instrument.py
This function was created to initialize the instrument connection, regardless of whether you choose to work with pyVISA or pySerial. The function returns either a VISA or serial connection to the instrument, first attempting to connect via a conventional GPIB-USB adapter with pyVISA. If this connection fails, it defaults to establishing a connection via GPIB-UNO.

IMPORTANT: The serial, pyserial and pyVISA libraries are required dependencies.

---

### **2. claseGPIB_Arduino.py**  
Este código es la base principal para la comunicación con los instrumentos utilizados como **Rohde&Schwarz FSP40** y **BKPRECISION 9115** y el correcto funcionamiento de los codigos encontrados en este repositorio. ademas de ser clave para la creacion de futuros scripts que requieran esta clase.  

---

### **4. BKPrecision_IVMeas**  
Ejemplo de uso para **inyectar corriente en un diodo y medir su voltaje**, generando su **curva característica**.  

#### **Instrucciones:**  
1. Conecta el **controlador** con el programa cargado y la PCB instalada.  
2. Modifica la dirección **GPIB**, el **puerto serial** y la **tasa de baudios** dentro del código.  
3. Carga el código.  
4. El programa activa automáticamente el **control remoto** en el instrumento.  
5. En la terminal, ingresa los siguientes valores:  
   - **Corriente inicial**, **corriente final** y **número de puntos** a medir.  
6. El código enviará automáticamente los comandos para:  
   - Ajustar la corriente.  
   - Medir el voltaje.  
   - Guardar estos datos en vectores para graficar la curva característica del diodo.  
