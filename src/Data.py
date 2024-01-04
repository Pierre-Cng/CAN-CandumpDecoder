from matplotlib import pyplot as plt 

status_dict = {'Active': 1, 'Inactive': 0}
class Data:
    def __init__(self):
        self.signals = {}
        self.fig = plt.figure()

    def add_value(self, signal, x, y):
        if signal not in self.signals:
            self.signals[signal] = Signal(signal)
        self.signals[signal].add_value(x, y)

    def plot(self):
        for signal in self.signals.values():
            if isinstance(signal.y, str):
                try:
                    signal.y = status_dict[signal.y]
                except:
                    print(signal.x, signal.y, signal.name)
            try:       
                plt.plot(signal.x, signal.y, label=signal.name)
            except:
                print(signal.x, signal.y, signal.name)

class Signal:
    def __init__(self, name):
        self.x=[]
        self.y=[]
        self.name = name
    
    def add_value(self, x, y):
        self.x.append(x)
        self.y.append(y)
