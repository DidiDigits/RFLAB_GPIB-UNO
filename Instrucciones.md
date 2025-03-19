# **Instalación**  

1. Carga el código en el Arduino utilizando el archivo **AR488.ino**.  
2. Identifica el puerto **COM()** y ajusta la tasa de baudios a **115200 baudios**.  
3. Coloca la **PCB con los componentes** sobre el Arduino.  
4. Conecta el **controlador** al instrumento **GPIB** y a la computadora.  
5. Verifica la dirección **GPIB** del instrumento (debe estar entre **1 y 29**).  
   - Si la dirección no está dentro de este rango, ajústala en el instrumento.  
6. Utiliza **Python** o **MATLAB** para enviar los comandos.  