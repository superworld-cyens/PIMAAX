import time
import socket
from datetime import datetime
import subprocess

#userdefined class
from core.sensors import Anemometer, GPS, RTC, Temp117
from core.data_logger import SensorDataLogger
from core.utils import logger


class PiMaax():

    def __init__(self, configuration):
        self.config = configuration #configuration read as dict

        #initialize logger
        self.logger = logger(log_id=self.config.get("logging", {}).get("log_id", "PiMaax"),
                            log_dir=self.config.get("logging", {}).get("log_dir", "./logs"),
                            log_filename=self.config.get("logging", {}).get("log_filename", "event.log"),
                            log_level=self.config.get("logging", {}).get("log_level", "INFO"))

        self.logger.info("PiMaax controller initialized with config.yaml")

        #initialize sensors
        self.anemometer = Anemometer(configuration, self.logger) 
        self.temp117 = Temp117(configuration, self.logger)
        self.rtc = RTC(configuration, self.logger)
        self.gps = GPS(configuration, self.logger)

        #initialize sensor data logger
        self.sensor_data_logger = SensorDataLogger(log_dir=self.config.get("logging", {}).get("log_dir", "./logs"),
                                                    webserver_data_path=self.config.get("logging", {}).get("webserver_data_path", "~/webserver_data"),
                                                    format=self.config.get("logging", {}).get("log_format", "json"),
                                                    tag=self.config.get("logging", {}).get("tag", "sensor_data"))

    def read_sensors(self):
        """ call get methods from the sensors class  """
        gps_data = self.gps.get_gpsdata()
        # gps_data = {"latitude": 0.0, "longitude": 0.0, "altitude": 0.0, "speed": 0.0, "timestamp": datetime.now().isoformat()} #for testing purposes
        now = datetime.now()
        current_time_str = now.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp_data = self.temp117.get_temperature()
        annometer_data =  self.anemometer.get_windspeed()
        # annometer_data = {"Wind_Speed":0.0}

        return current_time_str, gps_data, temp_data, annometer_data

    def run(self):
        """ create infinite loop and call read_sensor method """
        while True:
            current_time_str, gps_data, temp_data, annometer_data = self.read_sensors()

            #log the sensor data and write to file
            self.sensor_data_logger.log([{"timestamp": str(current_time_str), "gps_data": gps_data, "temp_data": temp_data, "annometer_data": annometer_data}])

            time.sleep(1)

    def _is_internet_available(self, host="8.8.8.8",port=53, timeout=3):
        """ check the internet connection """
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except (socket.timeout, socket.error):
            return False
    