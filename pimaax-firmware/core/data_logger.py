import os
from datetime import datetime
import json

class SensorDataLogger:
    def __init__(self, log_dir, webserver_data_path, tag="sensor_data", format="csv"):
        self.log_dir = log_dir
        self.webserver_data_path = webserver_data_path
        self.tag = tag.lower()
        self.format = format.lower()

        #create log dir
        os.makedirs(self.log_dir, exist_ok=True)
        os.makedirs(self.webserver_data_path, exist_ok=True)
        self.file_path = f"{self.log_dir}/D{datetime.now().strftime('%Y%m%d')}_T{datetime.now().strftime('%H%M%S')}_{self.tag}.{self.format}"


        #init header for sensor data
        self.headers = ["timestamp", "gps_data", "temp_data", "annometer_data"]
        if self.format == "csv":
            self._log_csv_(self.headers)

    def log(self, data):
        """
        Accepts data as list of dicts: [{'gps_data': ..., 'temp_data': ..., 'annometer_data': ...}]
        """

        for entry in data:
            timestamp = entry.get("timestamp", "")
            gps_data = entry.get("gps_data", "")
            temp_data = entry.get("temp_data", "")
            annometer_data = entry.get("annometer_data", "")

            #save data for analysis
            if self.format == "csv":
                row = [timestamp, gps_data, temp_data, annometer_data]
                self._log_csv(row)
            elif self.format == "json":
                json_entry = {
                    "timestamp": timestamp,
                    "gps_data": gps_data,
                    "temp_data": temp_data,
                    "annometer_data": annometer_data
                }
                self._log_json(json_entry)

            #save data for webserver
            self.log_webserver({
                "timestamp": timestamp,
                "gps": {"latitude": gps_data["latitude"], "longitude": gps_data["longitude"]},
                "temperature": sum(list(temp.values())[0] for temp in temp_data)/len(temp_data),
                "wind_speed": annometer_data['Wind_Speed']
            })

    def log_webserver(self, data):
        with open(self.webserver_data_path+'/sensor_data.json', 'w') as file:
            json.dump(data, file)
            file.write('\n')

    def _log_csv(self, row):
        with open(self.file_path, 'a') as file:
            file.write(','.join(map(str, row)) + '\n')
    
    def _log_json(self, entry):
        with open(self.file_path, 'a') as file:
            json.dump(entry, file)
            file.write('\n')


    
