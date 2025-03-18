% AR488_GPIB
% Configurar el puerto serie
serialPort = "COM12"; % Puerto actual, modificar si es necesario
baudRate = 115200; % Velocidad de comunicación
s = serialport(serialPort, baudRate);
pause(2); % Esperar a que el puerto esté listo
disp("Conectado al dispositivo.");

% Llamar a la función para enviar comandos
sendCommands(s);

% Cerrar el puerto cuando se termine
clear s;
