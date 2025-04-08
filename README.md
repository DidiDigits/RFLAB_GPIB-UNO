# RFLAB_GPIB-UNO
AR488 adaptation for use in the RF and Microwave lab at CICESE. This project uses an Arduino UNO as a GPIB-USB interface. This version has been modified to improve compatibility with our instruments, development environment, and specific test setups.

## How to start working with Arduino UNO as a GPIB
1. Download the AR488 folder (if not already done) and locate the AR488.ino file.
2. Open the file in the Arduino IDE and upload it to your Arduino board.
  Note: If the Arduino already has the AR488 program installed, you can skip these first two step.
3. Identify the COM() port in your device manager and set the baud rate to 115200.
4. Place the GPIB2Uno PCB with the components on top of the Arduino, as shown in the pictures in this repository in the Images folder.
5. Connect the controller to the GPIB instrument and the computer.
6. Check the GPIB address of the instrument (it must be between 1 and 29). If the address is outside this range, adjust it on the instrument.
7. Use Python or MATLAB to establish the instrument connection and send commands. For more details on each approach, refer to the corresponding folder in this repository.
