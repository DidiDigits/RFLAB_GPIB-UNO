# **Instrucciones para Python**  

Dentro de esta carpeta encontrarás **varios archivos .py**, cada uno con una función diferente:  

### **1. cambioGPIB.py**  
Este código permite cambiar la dirección GPIB en el controlador AR488 con la finalidad de que tenga la misma que la del instrumento y poder comunicarnos, el script requiere de la función **send_commands.py** para poder funcionar correctamente.  

#### **send_commands.py**  
Esta **función** se encarga de enviar y recibir comandos del instrumento por medio de instrucciones dadas por el usuario, además de comprobar una correcta comunicación mostrando la identificación del instrumento conectado.
 
**IMPORTANTE**: Es necesario instalar las librerias **serial** y **pyserial**

---

### **2. claseGPIB_Arduino.py**  
Este código es la base principal para la comunicación con los instrumentos utilizados como **Rohde&Schwarz FSP40** y **BKPRECISION 9115** y el correcto funcionamiento de los codigos encontrados en este repositorio. ademas de ser clave para la creacion de futuros scripts que requieran esta clase.

---

### **3. GPIB_USB_Arduino.py**  
Este código permite enviar comandos de manera manual al instrumento.  

#### **Instrucciones:**  
1. Conecta el **controlador** con el programa cargado y la PCB instalada.  
2. Modifica la dirección **GPIB**, el **puerto serial** y la **tasa de baudios** dentro del código.  
3. Carga el código.  
4. El programa activa automáticamente el **control remoto** en el instrumento.  
5. En la terminal aparecerá un menú con diferentes opciones para enviar comandos:  
   - Escribe un número según la opción deseada y presiona **Enter**.  
6. Envía el comando al instrumento.  
7. Para salir:  
   - Presiona **"4"** y **Enter**.  
   - El programa cerrará la conexión y restaurará el **control local** del instrumento.  

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
