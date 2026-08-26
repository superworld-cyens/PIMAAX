# 06 Firmware Setup and Running PiMaax

This guide describes the PiMaax firmware structure, configuration, and how to run the system.

Complete the previous hardware setup guides before running the firmware.

## 1. Firmware Structure

The firmware is located in:

```text
pimaax-firmware/
```

The main files and directories are:

1. `config/config.yaml` - Configuration for the PiMaax system.

2. `main.py` - Main entry point for the firmware.

3. `core/controller.py` - Handles sensor initialization and controls the main data collection process.

4. `core/sensors/` - Contains the individual sensor modules for the anemometer, GPS, RTC, and temperature sensors. Each module handles sensor initialization and data acquisition.

5. `core/data_logger.py` - Handles sensor data logging. JSON and CSV output formats are currently supported.

6. `core/utils/` - Contains supporting functions for configuration reading and event logging.

7. `data/` - Contains the collected sensor data and system logs.

## 2. Activate the Python Environment

Activate the PiMaax Python environment:

```bash
source ~/.pimaaxenv/bin/activate
```

## 3. Install Requirements

Enter the firmware directory:

```bash
cd pimaax-firmware
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This is normally required only during the initial setup or when the dependencies change.

## 4. Configuration

The firmware configuration is stored in:

```text
config/config.yaml
```

Review this file before running the system and update the settings if required.

## 5. Run PiMaax

From the `pimaax-firmware` directory, run:

```bash
python main.py
```

Use `Ctrl+C` to stop the program.

For normal use:

```bash
cd pimaax-firmware
source ~/.pimaaxenv/bin/activate
python main.py
```

## 6. Data Location

Sensor data are stored in:

```text
pimaax-firmware/data/logs/
```

The filename format is:

```text
D<YYYYMMDD>_T<HHMMSS>_sensordata.<filetype>
```

For example:

```text
D20250710_T172022_sensordata.json
```

The filename contains the date and time when the data file was created.

## 7. Event Logs

System events and sensor errors are recorded in the log files under:

```text
pimaax-firmware/data/logs/
```

Check the event log when troubleshooting sensor initialization, GPS connection, or data logging problems.
