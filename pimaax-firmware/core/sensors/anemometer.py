import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class Anemometer():
    """ Class for Anemometer initilization and reading"""
    def __init__(self, configuration, logger):
        self.logger = logger
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1015(self.i2c)
        self.chan = AnalogIn(self.ads, 0)
        self.ads.gain = 1

        self.logger.info(f"Anemometer Initialized")
        self.zero_offset = 0.006  # in volts (adjust as needed)

    def get_windspeed(self):
        voltage = self.chan.voltage
        corrected_voltage = max(0.0, voltage - self.zero_offset)
        wind_speed = corrected_voltage * 12

        annometer_value = {"Anemometer_ADC_Value": self.chan.value, "Anemometer_Voltage": voltage, "Anemometer_Cor_Voltage": corrected_voltage, "Wind_Speed": wind_speed}
        return annometer_value

