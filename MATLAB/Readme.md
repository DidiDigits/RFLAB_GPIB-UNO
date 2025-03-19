# **Instrucciones para MATLAB**  

Dentro de esta carpeta encontrarás **tres archivos .m**, cada uno con una función diferente:  

- **AR488_GPIB_FUNC.m** → Script principal para la comunicación GPIB.  
- **readcommand.m** → Función para leer respuestas del instrumento.  
- **sendcommands.m** → Función para enviar comandos al instrumento.  

### **Instrucciones:**  
1. Conecta el **controlador** con el programa cargado y la PCB instalada.  
2. Modifica el **puerto serial** y la **tasa de baudios** dentro del código.  
3. Carga el código.  
4. En la ventana de comandos, aparecerá la versión del **controlador** y la identificación del **instrumento**.  
5. Cambia la dirección **GPIB** del controlador para que coincida con la del instrumento:  
   - Escribe `++addr` y presiona **Enter** para ver la dirección actual.  
   - Luego, escribe `++addr X` (donde **X** es la dirección GPIB del instrumento) y presiona **Enter**.  
   - Guarda los cambios escribiendo `++savecfg` y presionando **Enter**.  
6. Para enviar comandos:  
   - En la ventana de comandos, escribe el comando y presiona **Enter**.  
7. Para salir:  
   - Escribe **"exit"** y presiona **Enter**.  
   - El programa cerrará la conexión.  
