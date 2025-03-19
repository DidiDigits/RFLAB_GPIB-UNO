# **Instrucciones para Python**  

Dentro de esta carpeta encontrarás **dos archivos .py**, cada uno con una función diferente:  

### **1. GPIB**  
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

### **2. Graficar**  
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
