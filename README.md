# 2017FRCSerialCommunicationTest

This project aims to demonstrate how RoboRIO and RaspberyPi could communicate through serial ports. 

To do this, you will need to wire the UART TDX, RDX and ground pins on raspberrypi with corresponding pins on the MXP of the RoboRIO. Then you need to deploy and run code on both sides (use sudo for code running on Raspberrypi).

For more information, please read [this wiki](https://github.com/WilliamHuang-cn/2017FRCVisionTrial/wiki/Using-a-coprocessor-with-RoboRIO).

# Using Serial Port with Pi2

## Disabling system serial port usage for Pi2

Open up a console on Raspberrypi and run the following code to disable the serial getty service:

`systemctl mask serial-getty@ttyAMA0.service`

Remove "console=ttyAMA0,115200" and "kgdboc=ttyAMA0,115200" configuration parameters from the "/boot/cmdline.txt" configuration file using nano editor.

`sudo cp /boot/cmdline.txt /boot/cmdline.bak`

`sudo nano /boot/cmdline.txt`

# Using Serial Port with Pi3

Raspberry Pi3 has a complete different layout from the Pi2. The default full capacity serial ports are used by system bluetooth service, and leaves us with an alternative on-board mini-UART.

## Using the mini-UART port for Pi3

To use the mini-UART port, you need to change the port in your code to `/dev/ttyS0`

## Using the normal UART port for Pi3

Though the alternative mini_UART port is made avaliable, it is limited in the rate of transmittion. To use the UART ports with full capcity, you need to disable bluetooth. 
