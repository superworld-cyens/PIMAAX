# 01 Raspberry Pi Setup

This guide describes the initial Raspberry Pi setup required to run the PiMaax firmware.

Complete this setup before configuring the individual sensors.

The setup covers:

* Raspberry Pi OS
* System update
* I2C interface
* Required system packages
* Python virtual environment
* PiMaax Python dependencies

After completing this guide, the Raspberry Pi will be ready for the individual sensor setup steps.

## 1. Requirements

Before starting, make sure:

* Raspberry Pi OS is installed.
* The Raspberry Pi is connected to the internet.
* You can access the terminal directly or through SSH.
* Git is installed.

## 2. Update the Raspberry Pi

Update the package list:

```bash
sudo apt update
```

Upgrade the installed packages:

```bash
sudo apt upgrade -y
```

## 3. Enable I2C

PiMaax uses several I2C devices, including the TMP117 temperature sensors, RTC, and ADC.

Open the Raspberry Pi configuration tool:

```bash
sudo raspi-config
```

Select the following options in order:

```text
Interface Options
I2C
Enable
```

Exit `raspi-config`.

Reboot the Raspberry Pi if requested:

```bash
sudo reboot
```

After reconnecting, check that the I2C interface is available:

```bash
ls /dev/i2c*
```

The main Raspberry Pi I2C bus should normally appear as:

```text
/dev/i2c-1
```

## 4. Install Required System Packages

Install the system packages required by PiMaax:

```bash
sudo apt install -y \
    python3-venv \
    python3-dev \
    build-essential \
    swig \
    i2c-tools \
    gpsd \
    gpsd-clients
```

These packages provide the Python virtual environment, compilation tools, I2C utilities, and GPS support required by the system.

## 5. Clone the PiMaax Repository

Clone the PiMaax repository:

```bash
git clone <PIMAAX_GITHUB_REPOSITORY_URL>
```

Enter the project directory:

```bash
cd pimaax
```

The main repository contains the firmware, hardware files, documentation, and Python requirements.

## 6. Create the PiMaax Python Environment

PiMaax should run inside its own Python virtual environment.

Create the environment:

```bash
python3 -m venv ~/.pimaaxenv
```

Activate it:

```bash
source ~/.pimaaxenv/bin/activate
```

After activation, the terminal should show `.pimaaxenv` at the beginning of the command prompt.

Check the Python version:

```bash
python --version
```

Check the Python location:

```bash
which python
```

It should point to the `.pimaaxenv` environment.

For example:

```text
/home/user/.pimaaxenv/bin/python
```

## 7. Upgrade pip

Inside the virtual environment, upgrade the Python packaging tools:

```bash
python -m pip install --upgrade pip setuptools wheel
```

Make sure `.pimaaxenv` is active before continuing.

## 8. Install PiMaax Requirements

All required Python packages are listed in:

```text
requirements.txt
```

From the root of the PiMaax repository, install them with:

```bash
pip install -r requirements.txt
```

Python dependencies required by PiMaax should be added to `requirements.txt` so that the complete environment can be reproduced using this command.

## 9. Verify the Environment

Check the Python and pip locations:

```bash
which python
which pip
```

Both should point to `.pimaaxenv`.

Check the installed Python packages:

```bash
pip list
```

## 10. Check I2C

The connected I2C devices can be checked with:

```bash
i2cdetect -y 1
```

This displays the devices currently detected on the Raspberry Pi I2C bus.

The addresses shown will depend on which PiMaax sensors are currently connected.

## 11. Using the PiMaax Environment

Whenever a new terminal or SSH session is opened, enter the PiMaax repository:

```bash
cd ~/pimaax
```

Activate the environment:

```bash
source ~/.pimaaxenv/bin/activate
```

The PiMaax Python environment is now ready to use.

## 12. Leaving the Environment

To leave the virtual environment:

```bash
deactivate
```

The environment does not need to be recreated. Activate it again when working with PiMaax:

```bash
source ~/.pimaaxenv/bin/activate
```