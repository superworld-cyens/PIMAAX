# 04 RTC Setup

This guide describes how to connect and verify the SparkFun RV-8803 Real Time Clock used in PiMaax.

The RTC provides date and time information and continues keeping time when the Raspberry Pi is powered off.

## 1. Hardware

Required components:

* SparkFun RV-8803 Real Time Clock
* CR1225 backup battery
* SparkFun Qwiic HAT
* Qwiic cable
* Raspberry Pi

The RTC communicates with the Raspberry Pi using I2C.

The RV-8803 has a fixed I2C address:

```text id="t99g4j"
0x32
```

The address does not conflict with the other PiMaax I2C devices.

## 2. Install the Backup Battery

Install a CR1225 coin cell battery in the RTC battery holder.

Check the battery polarity before installation.

The battery allows the RTC to continue keeping time when the Raspberry Pi is powered off.

## 3. Connect the RTC

Connect the RV-8803 to the SparkFun Qwiic HAT using a Qwiic cable.

The connection is:

```text id="0f0tfb"
Raspberry Pi
Qwiic HAT
RV-8803 RTC
```

The Qwiic connection provides both power and I2C communication.

No additional wiring is required.

## 4. Check the RTC Connection

Run:

```bash id="53c4j9"
i2cdetect -y 1
```

The RTC should appear at:

```text id="ec4ygi"
0x32
```

With the other PiMaax devices connected, the I2C addresses are:

| Device          | I2C Address |
| --------------- | ----------- |
| RV-8803 RTC     | `0x32`      |
| ADS1015         | `0x48`      |
| TMP117 Sensor 1 | `0x49`      |
| TMP117 Sensor 2 | `0x4A`      |
| TMP117 Sensor 3 | `0x4B`      |

If `0x32` does not appear, check:

* Qwiic cable connection
* RTC connection
* Qwiic HAT connection
* I2C configuration

## 5. Setup Complete

The RTC setup is complete when:

* The CR1225 backup battery is installed.
* The RTC is connected through the Qwiic HAT.
* `i2cdetect -y 1` shows address `0x32`.

The RTC is now ready for use with the PiMaax firmware.

Continue with:

[05 GPS Setup](05-gps.md)
