# GPIB-Arduino-RFLAB
AR488 adaptation for use in the RF and Microwave lab at CICESE. This project uses an Arduino UNO as a GPIB-USB interface. This version has been modified to improve compatibility with our instruments, development environment, and specific test setups.

## How to start working with Arduino UNO as a GPIB
1. Upload the code to the Arduino using the Arduino IDE and the AR488.ino file. You will need to download the entire AR488 archive. If the Arduino has already been updated with this program, you can skip this step.
2. Identify the COM() port in your device manager and set the baud rate to 115200.
3. Place the GPIB2Uno PCB with the components on top of the Arduino, as shown in the pictures in this repository.
4. Connect the controller to the GPIB instrument and the computer.
5. Check the GPIB address of the instrument (it must be between 1 and 29).
6. If the address is outside this range, adjust it on the instrument.
7. Use Python or MATLAB to send commands.
