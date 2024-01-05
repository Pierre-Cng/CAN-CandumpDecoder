import pandas as pd 
import json 

class Data:
    def __init__(self):
        self.signals = {}

    def add_value(self, signal, x, y):
        if signal not in self.signals:
            self.signals[signal] = {'name': signal, 'x':[], 'y':[]}
        self.signals[signal]['x'].append(x)
        self.signals[signal]['y'].append(y)

    def dict_obj_converter(self, obj):
        return obj.__dict__ 
    
    def convert_to_csv(self):
        master_df = pd.DataFrame(columns=['Signal', 'x', 'y'])  
        for signal in self.signals:
            x_values = self.signals[signal]['x']
            y_values = self.signals[signal]['y']
            master_df = master_df._append({'Signal': signal, 'x': x_values, 'y': y_values}, ignore_index=True)
        master_df.to_csv('master_data.csv', index=False)
    
    def convert_to_json(self):
        with open('json_output.json', 'w') as json_file:
            json.dump(self.signals, json_file, default=self.dict_obj_converter, indent=4)
