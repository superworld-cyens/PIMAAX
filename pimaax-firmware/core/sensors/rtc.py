import time
import sys
import qwiic_rv8803

class RTC():
    """ Class for RTC initilization and reading"""

    def __init__(self, configuration, logger):
        self.rtc = qwiic_rv8803.QwiicRV8803()
        self.logger = logger

        self.logger.info("Initializing RV-8809 RTC module...")

        if self.rtc.is_connected():
            self.rtc.begin()
            self.logger.info(f"RTC module connected successfully and RV-8809 RTC(Address {hex(self.rtc.address)})")

            self.rtc.update_time()
            
            if self.rtc.get_year()<2024: #check if year is 2025
                self.logger.warning("RTC module year is not set to 2025, setting it now...")
                """Below set time will set current time based on system time. This will done only once when we setup in lab"""
                # now = time.localtime()
                # rtc_weekday = (now.tm_wday + 1) % 7

                # self.rtc.set_time(
                #     now.tm_sec,           # seconds
                #     now.tm_min,           # minutes
                #     now.tm_hour,          # hours
                #     rtc_weekday,          # weekday 
                #     now.tm_mday,          # date 
                #     now.tm_mon,           # month
                #     now.tm_year           # year 
                # )
            
                self.logger.error("RTC module need time synchronization. Please set the time manually in the lab.")

        else:
            self.logger.error(f"RV-8809 RTC module not found at address {hex(self.rtc.address)}")
        


    def get_currentdatetime(self):
        """ Get current date and time from RTC module """
        try:
            self.rtc.update_time()
            datetime_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
                            self.rtc.get_year(),
                            self.rtc.get_month(),
                            self.rtc.get_date(),
                            self.rtc.get_hours(),
                            self.rtc.get_minutes(),
                            self.rtc.get_seconds()
                            )
            return datetime_str
        except Exception as e:
            self.logger.error(f"Error reading RTC data: {e}")
            return None