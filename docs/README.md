# PiMaax Setup Guide

This documentation provides step-by-step instructions for assembling, configuring, and testing the PiMaax environmental sensing system.

PiMaax is built around a Raspberry Pi and includes:

* Three TMP117 temperature sensors
* Anemometer with ADS1015 ADC
* RV-8803 real-time clock
* USB GPS receiver
* SparkFun Qwiic HAT

## Installation

Follow the setup guides in the order listed below. Each component should be configured and tested before proceeding to the next one.

### 1. Raspberry Pi Setup

Prepare the Raspberry Pi, enable the required interfaces, create the Python virtual environment, and install the PiMaax dependencies.

[01 Raspberry Pi Setup](01-raspberry-pi-setup.md)

### 2. TMP117 Temperature Sensors

Configure the I2C addresses of the three TMP117 sensors, connect them to the Qwiic HAT, and test the temperature measurements.

The sensors use the following addresses:

* Sensor 1: `0x49`
* Sensor 2: `0x4A`
* Sensor 3: `0x4B`

[02 TMP117 Temperature Sensors](02-temperature-sensors.md)

### 3. Anemometer and ADS1015

Connect the anemometer through the ADS1015 ADC and test the wind speed measurements.

[03 Anemometer Setup](03-anemometer.md)

### 4. Real-Time Clock

Connect and configure the RV-8803 real-time clock and verify the date and time readings.

[04 RTC Setup](04-rtc.md)

### 5. GPS

Connect the USB GPS receiver, configure `gpsd`, and verify that GPS data can be accessed from Python.

[05 GPS Setup](05-gps.md)

### 6. Firmware Setup and Running PiMaax

Review the PiMaax firmware structure, configure the system, install the required Python dependencies, and run the data collection firmware.

[06 Firmware Setup and Running PiMaax](06-firmware-setup.md)