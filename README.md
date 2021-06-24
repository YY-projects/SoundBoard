# SoundBoard
CIRCUIT
First, wire up the circuit according to the schematic (attached to the YouTube video description). It’s best to do this on a breadboard first. 

NOTE: The inductors and most capacitors are meant to improve the final audio quality. Using different values from those on the schematic, or excluding some of the caps and inductors may lead to worse quality, but most likely won’t cause the circuit to not work (so it’s ok to use the closest values you can get). 

This circuit uses a 5V power supply. The INPUT pin is where you can connect a sensor or button. It is triggered when the input pin is 0V, so if you’re using a button, make sure to add a pull-up resistor to that pin (not included in the schematic).


CODE:
The code for the PIC12F683 is attached to the YouTube video description. If you don’t have MPLAB X IDE downloaded, or are unfamiliar with the software, look up tutorials regarding it beforehand. 

DISCLAIMER: As I mentioned in the video, the 25A512 EEPROM is 64 kilobytes of ROM, which is 8 seconds worth of low quality audio (at an 8 kb/s sampling rate). However, there are complications with this setup (because of the way the DAC chip takes inputs) that requires the RAW audio file to be encoded a certain way, which reduces the duration to 4 seconds. Read the OPTIONAL EXPLANATION if you care about why this is, but if not, follow the steps below and you should be good to go. 

[OPTIONAL EXPLANATION: An ideal Digital to Analog Converter would require 8 bits clocked into the data pin, followed by a clock pulse, to output the corresponding voltage. Unfortunately, the MCP4901 takes 2 bytes of input (check out pages 24 and 25 of this datasheet https://ww1.microchip.com/downloads/en/DeviceDoc/22248a.pdf) The first 4 bits are control bits, the next 8 bits are the actual digital value to be converted, and the last 4 bits are garbage. So normally, the microcontroller would get the digital value from the EEPROM, and send it over to the DAC in this 2 byte format. However, not only would that be too slow (since we’re using a 20 MHz crystal clock), but there simply aren’t enough pins on the PIC12F683 for this. So, I made a simple python program that will take as input the original RAW audio file, and convert each byte to the 2 byte format required by the DAC. So, all the microcontroller needs to do is provide the clock pulse, and the EEPROM will transfer the data directly to the DAC, encoded in the format required by the MCP4901. Of course, this cuts the maximum audio length in half because the RAW file will double in size. Follow the steps below for the implementation.]

Download the PYTHON CODE for EEPROM in the YouTube video description
1. Open Visual Studio Code
2. Open the Python code by going to File > Open File … > (the file you just downloaded)
3. Place your RAW audio file in the same folder on your computer as the Python program.
4. At the top of the python file (line 5), where it says “with open(‘work.hex’, ‘r’) as f:” replace “work.hex” with the name of your RAW audio file (ex. “myrawaudio.hex”)
5. Run the program by going to Run > Run Without Debugging
6. Go back to the folder where the Python program and audio file are. You should see a HEX file called “final” This is what you upload directly onto the EEPROM.

NOTE ON AUDIO:
Once you pick a file, you need to lower the sampling rate. The original audio will likely be in the MP3 or WAV format. Keep it in this format, and lower the sampling rate to 8 kilobytes per second (I used Audacity). Next, convert it to the RAW format. KEEP IN MIND that the RAW format is much larger than MP3, and the RAW file you get at this point will double in size before you upload it onto the EEPROM (because of the above Python procedure). So whatever MP3 file you use, it needs to be pretty small.
