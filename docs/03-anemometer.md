## 3. Anemometer Power Supply

The SEN0170 anemometer requires a higher supply voltage than the Raspberry Pi can directly provide.

PiMaax uses the Texas Instruments PTN04050C boost converter to generate the required supply voltage.

The converter specifications are:

| Parameter             | Value                  |
| --------------------- | ---------------------- |
| Converter             | PTN04050C              |
| Input voltage         | 2.95 V to 5.5 V        |
| Output voltage        | 5 V to 15 V adjustable |
| Maximum output power  | 12 W                   |
| PiMaax output voltage | 12 V                   |

The converter can therefore take a low voltage input and generate the 12 V supply used by the anemometer.

The PTN04050C datasheet is available from Texas Instruments:

[PTN04050C Datasheet](https://www.ti.com/lit/gpn/PTN04050C?utm_source=chatgpt.com)

### 3.1 PTN04050C Connections

The PTN04050C has four connections:

| Pin   | Function                  |
| ----- | ------------------------- |
| Pin 1 | GND                       |
| Pin 2 | Input voltage             |
| Pin 3 | Output voltage adjustment |
| Pin 4 | Output voltage            |

The input and output use the same common ground.

### 3.2 Standard Circuit

The following circuit is based on the standard application circuit provided in the PTN04050C datasheet.

![PTN04050C standard application circuit](images/PTN04050C_standard_application.png)

The circuit requires:

```text
Input capacitor
100 uF electrolytic

Output capacitor
100 uF electrolytic

Output adjustment resistor
RSET
```

The capacitor polarity must be observed when using electrolytic capacitors.

### 3.3 Configure the Output for 12 V

The output voltage is configured using a resistor between Pin 3 and GND.

For a 12 V output, the PTN04050C datasheet specifies:

```text
RSET = 1.33 kOhm
```

Connect:

```text
Pin 3 to 1.33 kOhm resistor
1.33 kOhm resistor to GND
```

This produces an output of approximately:

```text
12.03 V
```

For PiMaax, this is treated as the 12 V anemometer supply.

### 3.4 Power Connections

The boost converter should be connected as follows:

```text
PTN04050C Pin 1
GND

PTN04050C Pin 2
Low voltage input

PTN04050C Pin 3
1.33 kOhm resistor to GND

PTN04050C Pin 4
12 V output to anemometer power input
```

The anemometer ground must connect to the same common ground used by the boost converter, ADS1015, and Raspberry Pi.

### 3.5 Check the Output Before Connecting the Anemometer

Before connecting the anemometer, power the boost converter and measure the voltage between:

```text
Pin 4
GND
```

The multimeter should measure approximately:

```text
12 V
```

Do not connect the anemometer if the output voltage is outside its acceptable supply range.

After confirming the output voltage, connect the 12 V output to the anemometer power input.
