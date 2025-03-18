% Función para leer los comandos y enviar una respuesta
% Practicas profesionales
% 05 de marzo de 2025
function readCommand(s, cmd)
    writeline(s, cmd); % Enviar comando
    pause(0.5); % Esperar la respuesta
    try
        response = readline(s); % Intentar leer la respuesta
        disp("Respuesta: " + response);
    catch
        disp("Comando no reconocido o sin respuesta.");
    end
end