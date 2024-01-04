import datetime
import pytz

class Timestamp:
    def __init__(self):
        self.started = False
    
    def duration(self, time):
        if not self.started:
            self.started = True 
            self.starttime = time
            return 0.00000
        else:
            return time - self.starttime
        
    def convert(self, time):
        arizona_tz = pytz.timezone('America/Phoenix')
        arizona_datetime = datetime.datetime.fromtimestamp(time, arizona_tz)
        # Format time as HH:MM:SS.ms
        formatted_time = arizona_datetime.strftime("%H:%M:%S.%f")
        return formatted_time
