import time
import gpsd # Uses gpsd-py3 library​
# If using the gps module from gpsd itself, it might be:​
import gps


class GPS():
    """ Class for GPS initlization and reading """

    def __init__(self, configuration, logger):
        self.config = configuration
        self.logger = logger
        # self.gps_connection = False #why do we need this now?

        try:
            gpsd.connect() # using gpsd-py3 library
            # self.session = gps.gps(host="localhost", port="2947", mode=gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE) #using gps
            
            #report gps initialization
            self.logger.info("GPS module initialized")
        except Exception as e:
            self.logger.error(f"Failed to initialize GPS sensor: {e}")
            self.logger.error("Ensure gpsd service is runnign and configured for your GPS device")


    def get_gpsdata(self):
        """ Get GPS data from gpsd """
        try:
            packet = gpsd.get_current()  # using gpsd-py3 library
            # print(packet)
            # packet = self.session.next() # using gps
            if packet.mode >= 2:  # Check if the GPS has a fix
                gps_data = {
                    'latitude': packet.lat,
                    'longitude': packet.lon,
                    'altitude': packet.alt,
                    'speed': packet.speed(),
                    # 'timestamp': time.time()
                }
                return gps_data
            else:
                self.logger.warning("GPS signal not available or no fix")
                return None
        except Exception as e:
            self.logger.error(f"Error reading GPS data: {e}")
            return None



