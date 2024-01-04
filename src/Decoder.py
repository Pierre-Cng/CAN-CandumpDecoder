import cantools 
from Data import Data
from matplotlib import pyplot as plt 

class Decoder:
    def __init__(self, dbc):
        self.dbase = cantools.database.load_file(dbc)
        self.data = Data()

    def add_msg(self, timestamp, frame_id, data):
        try:
            message = self.dbase.get_message_by_frame_id(frame_id)
            decoded_signals = message.decode(data, allow_truncated=True)            
        except Exception as e:
                print(f'Failed to parse data of frame: Id {frame_id}, Timestamp: {timestamp}, Raw data: {data}')
                print(f'(0x{frame_id:x}): {e}')

        for signal in decoded_signals:
            x = timestamp
            y = decoded_signals[signal]
            signal = message.name + '.' + signal
            self.data.add_value(signal, x, y)

    def plot(self):
        self.data.plot()
        plt.show()
