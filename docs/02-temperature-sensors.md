# 02 TMP117 Temperature Sensors Setup

This guide describes how to configure, connect, and test the three SparkFun TMP117 temperature sensors used in PiMaax.

Complete the Raspberry Pi setup before following this guide.

The three sensors use the following I2C addresses:

| Sensor          | I2C Address |
| --------------- | ----------- |
| TMP117 Sensor 1 | `0x49`      |
| TMP117 Sensor 2 | `0x4A`      |
| TMP117 Sensor 3 | `0x4B`      |

## 1. Hardware

Required components:

* 3 SparkFun TMP117 temperature sensors
* SparkFun Qwiic HAT for Raspberry Pi
* Qwiic cables
* Raspberry Pi

The TMP117 sensors communicate with the Raspberry Pi using I2C through the Qwiic HAT.

All three sensors share the same I2C bus, so each sensor must have a unique address.

## 2. Configure the I2C Addresses

The default TMP117 I2C address is:

```text
0x48
```

PiMaax also uses an ADS1015 ADC at `0x48`. The three TMP117 sensors must therefore be configured with different addresses.

The required configuration is:

| Sensor   | Connection  | I2C Address |
| -------- | ----------- | ----------- |
| Sensor 1 | ADDR to VCC | `0x49`      |
| Sensor 2 | ADDR to SDA | `0x4A`      |
| Sensor 3 | ADDR to SCL | `0x4B`      |

### Step 1. Cut the Default Trace

Locate the address selection jumper on the underside of the TMP117 board.

The default configuration connects the address jumper to GND.

Carefully cut the small trace connecting the address jumper to GND.

Repeat this for all three sensors.

Use a multimeter in continuity mode to confirm that the original GND connection has been broken.

### Step 2. Solder the New Address

Create the required solder bridge on each sensor.

For Sensor 1:

```text
ADDR to VCC
Address 0x49
```

For Sensor 2:

```text
ADDR to SDA
Address 0x4A
```

For Sensor 3:

```text
ADDR to SCL
Address 0x4B
```

Inspect each solder connection before connecting the sensors to the Raspberry Pi.

## 3. Connect the Sensors

Mount the SparkFun Qwiic HAT on the Raspberry Pi.

Connect the first TMP117 sensor to the Qwiic HAT.

The TMP117 sensors can then be connected in series using Qwiic cables.

The connection order is:

```text
Raspberry Pi
Qwiic HAT
TMP117 Sensor 1 at 0x49
TMP117 Sensor 2 at 0x4A
TMP117 Sensor 3 at 0x4B
```

The Qwiic connection provides power and I2C communication, so no additional wiring is required for the TMP117 sensors.

## 4. Check the Sensors

Make sure all three sensors are connected.

Run:

```bash
i2cdetect -y 1
```

The I2C scan should show:

```text
49
4a
4b
```

For example:

```text
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
40:                         -- 49 4a 4b -- -- -- --
```

This confirms that all three TMP117 sensors are visible to the Raspberry Pi.

If an address is missing, check:

* The Qwiic cable
* The solder bridge
* The address configuration
* Whether the original GND trace was completely cut

All three addresses should be detected before continuing.

## 5. Activate the PiMaax Environment

Activate the Python environment created during the Raspberry Pi setup:

```bash
source ~/.pimaaxenv/bin/activate
```

The required Python packages should already be installed through:

```bash
pip install -r requirements.txt
```

The TMP117 library used by PiMaax is:

```text
sparkfun-qwiic-tmp117
```

## 6. Test the Temperature Sensors

Create a test file named:

```text
test_tmp117.py
```

Add the following code:

```python
import time
import qwiic_tmp117


SENSOR_ADDRESSES = [
    0x49,
    0x4A,
    0x4B,
]

sensors = []

for address in SENSOR_ADDRESSES:
    sensor = qwiic_tmp117.QwiicTmp117(address)

    if sensor.is_connected():
        sensor.begin()
        sensors.append((address, sensor))
        print(f"TMP117 at {hex(address)} connected")
    else:
        print(f"TMP117 at {hex(address)} not found")


while True:

    for address, sensor in sensors:
        temperature = sensor.get_temperature_celsius()

        print(
            f"Sensor {hex(address)}: "
            f"{temperature:.2f} C"
        )

    print()

    time.sleep(2)
```

Run the test:

```bash
python test_tmp117.py
```

A successful output should look similar to:

```text
TMP117 at 0x49 connected
TMP117 at 0x4a connected
TMP117 at 0x4b connected

Sensor 0x49: 25.31 C
Sensor 0x4a: 25.27 C
Sensor 0x4b: 25.35 C

Sensor 0x49: 25.32 C
Sensor 0x4a: 25.28 C
Sensor 0x4b: 25.36 C
```

Use `Ctrl+C` to stop the test.

## 7. Setup Complete

The TMP117 setup is complete when:

* Sensor 1 is detected at `0x49`.
* Sensor 2 is detected at `0x4A`.
* Sensor 3 is detected at `0x4B`.
* `i2cdetect -y 1` shows all three sensors.
* Python can read temperature values from all three sensors.
