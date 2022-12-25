import pyqtgraph as pg
import numpy as np

class PlotAcceleration(pg.PlotItem):
    def __init__(self, parent=None, name=None, labels=None, title="Accelerations (m/s²)", viewBox=None, axisItems=None, enableMenu=True, **kargs):
        super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)
        self.addLegend() # Enable Legend
        self.hideAxis("bottom")
        
        self.x_axis = self.plot(pen=(102, 252, 241), name='X')
        self.y_axis = self.plot(pen=(29, 185, 84), name='Y')
        self.z_axis = self.plot(pen=(203, 45, 111), name='Z')
        
        self.acc_x_data = np.linspace(0, 0)
        self.acc_y_data = np.linspace(0, 0)
        self.acc_z_data = np.linspace(0, 0)
        self.ptr = 0
        
    def update(self, ax, ay, az):
        # Basically Removing 0-indexed element and dublicating last-indexed element
        print(ax, ay, az)
        self.acc_x_data[:-1] = self.acc_x_data[1:]
        self.acc_y_data[:-1] = self.acc_y_data[1:]
        self.acc_y_data[:-1] = self.acc_y_data[1:]
        
        # Replacing last-indexed dublicate value with new value
        self.acc_x_data[-1] = float(ax)
        self.acc_y_data[-1] = float(ay)
        self.acc_z_data[-1] = float(az)
        self.ptr += 1
        
        self.x_axis.setData(self.acc_x_data)
        self.y_axis.setData(self.acc_y_data)
        self.z_axis.setData(self.acc_z_data)
        
        self.x_axis.setPos(self.ptr, 0) # Increasing X-Axis of GraphView
        self.y_axis.setPos(self.ptr, 0)
        self.z_axis.setPos(self.ptr, 0)