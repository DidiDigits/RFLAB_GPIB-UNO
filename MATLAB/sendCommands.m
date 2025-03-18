% Función para enviar los comandos
% Practicas profesionales
% 05 de marzo de 2025
function sendCommands(s)
    % Ejecuta comandos iniciales
    % Esto se realiza llamando a la funcion "readCommand"
    readCommand(s, "++ver");
    readCommand(s, "*IDN?");
    
    % Permitir envío de comandos en bucle
    while true
        command = input("Escribe un comando (o 'exit' para salir): ", "s");
        if strcmpi(command, "exit")
            break;
        end
        readCommand(s, command);
    end
end



