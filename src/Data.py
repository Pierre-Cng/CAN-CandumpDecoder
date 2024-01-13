import pandas as pd 
import json 
from datetime import datetime

class Data:
    def __init__(self):
        self.raw_trace = []
        self.signals = {}

    def add_value(self, signal, x, y):
        if signal not in self.signals:
            self.signals[signal] = {'name': signal, 'x':[], 'y':[]}
        self.signals[signal]['x'].append(x)
        self.signals[signal]['y'].append(y)
    
    def add_raw_trace(self, timestamp, frame_id, data):
        self.raw_trace.append(f'{timestamp}, {frame_id}, {data}')

    def dict_obj_converter(self, obj):
        return obj.__dict__
    
    def save_raw_trace(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f'trace_can__{current_datetime}.txt', 'w') as trace:
            for line in self.raw_trace:
                trace.write(line + '\n')
    
    def convert_to_csv(self):
        master_df = pd.DataFrame(columns=['Signal', 'x', 'y'])  
        for signal in self.signals:
            x_values = self.signals[signal]['x']
            y_values = self.signals[signal]['y']
            master_df = master_df._append({'Signal': signal, 'x': x_values, 'y': y_values}, ignore_index=True)
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        master_df.to_csv(f'decoded_data__{current_datetime}.csv', index=False)
    
    def convert_to_json(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f'decoded_data__{current_datetime}.json', 'w') as json_file:
            json.dump(self.signals, json_file, default=self.dict_obj_converter, indent=4)
