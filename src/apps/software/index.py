import random
import sys
import time
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

from App import App

# import resources


app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("src/favicon.png"))

widget = App()
widget.show()


#################################
# value = 100
# i = 0
# x, y = [], []
# maxPoints = 5

# # init
# for i in range(maxPoints):
#     value += random.randint(-1, 1)
#     value = max(min(110, value), 90)
#     x += [i]
#     y += [value]

# widget.currentWidget().drawLine(x, y)


# def update():
#     global value, i, x, y, maxPoints
#     value = max(min(110, value + random.randint(-1, 1)), 90)
#     i += 1
#     x += [i]
#     y += [value]
#     if i >= maxPoints:
#         x = x[-maxPoints:]
#         y = y[-maxPoints:]

#     widget.currentWidget().drawLine(x, y)


# while True:
#     update()
#     # time.sleep(0.5)


# anim = FuncAnimation(widget.currentWidget().mpl_canvas.fig, update, interval=100)
# widget.currentWidget().mpl_canvas.fig.tight_layout()
# widget.currentWidget().mpl_canvas.show()
# anim.save()
# update()
# time.sleep(0.5)
# update()
# time.sleep(0.5)
# update()
# time.sleep(0.5)
# update()
# time.sleep(0.5)
# update()
# time.sleep(0.5)
# update()
# time.sleep(0.5)
# update()
# time.sleep(0.5)


#################################

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
