# 05 GPS Setup

This guide describes how to connect and configure the USB GPS receiver used in PiMaax.

The GPS connects to the Raspberry Pi through USB. The `gpsd` service manages communication between the GPS receiver and the PiMaax firmware.

## 1. Connect the GPS

Connect the GPS receiver to a USB port on the Raspberry Pi.

The GPS is powered directly through USB.

Check which serial device was created:

```bash id="km4g13"
ls -l /dev/ttyACM* /dev/ttyUSB* 2>/dev/null
```

For the PiMaax setup, the GPS normally appears as:

```text id="as0i1j"
/dev/ttyACM0
```

If a different device name appears, use that device name in the following configuration.

## 2. Configure gpsd

The `gpsd` packages were installed during the Raspberry Pi setup.

Open the configuration file:

```bash id="jvphb0"
sudo nano /etc/default/gpsd
```

Configure:

```text id="u6z8nj"
START_DAEMON="true"
USBAUTO="false"
DEVICES="/dev/ttyACM0"
GPSD_OPTIONS="-n"
```

If the GPS uses a different serial device, change the `DEVICES` value.

Save and close the file.

## 3. Restart gpsd

Restart the services:

```bash id="rld6wl"
sudo systemctl restart gpsd
sudo systemctl restart gpsd.socket
```

Enable them to start automatically:

```bash id="2mabho"
sudo systemctl enable gpsd
sudo systemctl enable gpsd.socket
```

Check the service:

```bash id="fpfr0i"
systemctl status gpsd --no-pager
```

After this configuration, gpsd should start automatically when the Raspberry Pi boots. The GPS does not need to be manually started before running PiMaax.

## 4. Check the GPS

Run:

```bash id="qg7e8m"
cgps -s
```

When the GPS has acquired a position fix, information such as the following should appear:

```text id="xbpjrc"
Time
Latitude
Longitude
Altitude
Speed
Status
```

If the status shows:

```text id="4nnfwc"
NO FIX
```

the GPS may be connected correctly but has not yet acquired enough satellites.

Place the GPS where it has a clear view of the sky and wait for a position fix. Initial acquisition can take several minutes.

Use `Ctrl+C` to exit `cgps`.

## 5. Check gpsd Port

gpsd normally provides GPS data through port `2947`.

Check that the port is active:

```bash id="q3wlvj"
sudo ss -ltnp | grep 2947
```

If gpsd is running correctly, the port should be listed.

The PiMaax firmware connects to this service to access GPS data.

## 6. Troubleshooting

If `cgps -s` cannot connect, check:

```bash id="5pphdh"
systemctl status gpsd
```

If necessary, restart the service:

```bash id="mh7uvm"
sudo systemctl restart gpsd
sudo systemctl restart gpsd.socket
```

If manually starting gpsd gives:

```text id="ldmqq7"
Address already in use
```

another gpsd instance is already running.

Do not start a second gpsd instance manually.

Check the existing service instead:

```bash id="tvnk7k"
systemctl status gpsd
```

## 7. Setup Complete

The GPS setup is complete when:

* The GPS is connected through USB.
* The GPS appears as `/dev/ttyACM0` or another serial device.
* gpsd is configured for the correct device.
* gpsd starts automatically.
* `cgps -s` connects successfully.
* Latitude and longitude appear after the GPS obtains a fix.

The GPS is now ready for use with the PiMaax firmware.

Continue with:

[06 Complete System Test](06-system-test.md)
