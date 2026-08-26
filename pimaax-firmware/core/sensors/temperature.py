
import time
import qwiic_tmp117


class Temp117():
    """ Class for temperature sensor initialziign and reading  """
    def __init__(self, configuration, logger):
        self.config = configuration
        self.logger = logger
        self.temp_sensor_id = ["temp_sensor1","temp_sensor2","temp_sensor3"] 
        
        #init temp sesnors
        self.temp_sensor = []
        self.TMP117_ADDRESSES = self.config.sensors["temperature"]["addresses"]  #resoldered I2C addresses for TMP117
        for address in self.TMP117_ADDRESSES:
            sensor =  qwiic_tmp117.QwiicTMP117(address=address)
            if sensor.is_connected():
                sensor.begin()
                self.logger.info(f"TMP117 sensor at address {hex(address)} initialized successfully")
                self.temp_sensor.append(sensor)
            else:
                self.temp_sensor.append(None)
                self.logger.error(f"TMP117 sensor at address {hex(address)} not connected, check wiring or address")

    def get_temperature(self):
        temp_c = []
        for i, sensor in enumerate(self.temp_sensor):
            if sensor and sensor.is_connected():
                # print(dir(sensor))
                try:
                    temp_c.append({self.temp_sensor_id[i]:round(sensor.read_temp_c(),4)})
                except Exception as e:
                    temp_c.append(None)
                    self.logger.error(f"Error reading temperature from TMP117 sensor:{i} at address {hex(sensor.address)}: {e}")
            else:
                temp_c.append(None)
                self.logger.warning(f"Skipping uninitialized TMP117 sensor at index {i}")
        return temp_c