from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
)
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, interval=0, updateFunc=lambda: None):
        self.fig = Figure()
        # self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        if interval == 0:
            return
        self.timer = self.new_timer(interval, [(updateFunc, (), {})])
        self.timer.start()
