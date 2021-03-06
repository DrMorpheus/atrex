
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import *

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar


from matplotlib.figure import Figure
import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt
from scipy import interpolate
import math
rcParams['font.size'] = 9


class MyPlotWidget (QWidget) :
    def __init__(self, parent):
        QWidget.__init__(self,parent)
        self.figure = Figure()
        self.canvas = FigureCanvas (self.figure)
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.axes = self.figure.add_subplot(111)
        #self.createCosData ()
        self.pType = 1
        self.tstr = "Atrex Plot"
        self.xstr = "X Data"
        self.ystr = "Y Data"
        self.olayFlag = False
        self.plotDataFlag = False
        self.plotData()



    def sizeHint(self):
        w, h = self.get_width_height()
        return QSize(w, h)

    def minimumSizeHint(self):
        return QSize(10, 10)


    def plotData (self):
        #self.setXYData (xarr, yarr, 2)
        self.axes.cla()
        self.axes.set_title (self.tstr)
        self.axes.set_xlabel (self.xstr)
        self.axes.set_ylabel(self.ystr)
        if (self.plotDataFlag==False) :
            self.canvas.draw()
            return
        if self.pType==0 :
            self.axes.plot (self.xarr, self.yarr)
        if self.pType == 1 :
            self.axes.plot (self.xarr, self.yarr, 'gD')
        if self.pType == 2 :
            self.axes.plot (self.x10, self.yarrSpline, 'b+')
        if self.pType == 3 :
            self.axes.plot (self.xarr, self.yarr, 'gD', self.x10, self.yarrSpline,'b-')
        if self.olayFlag :
            self.axes.plot (self.xarrOlay, self.yarrOlay, 'y^')
        self.canvas.draw()


    def plotDataXY2 (self, xarr, yarr, yarrFit):
        self.axes.cla()
        self.axes.set_title (self.tstr)
        self.axes.set_xlabel (self.xstr)
        self.axes.set_ylabel(self.ystr)
        self.axes.plot(xarr, yarr, 'g-', xarr, yarrFit,'b-')
        self.canvas.draw()


    """ MyPlotWidget.setXYData (xarr, yarr, int type)
        type values of
            0 - for points
            1 - connected segments
            2 - spline connect
    """
    def setXYData (self, xarr, yarr) :
        self.plotDataFlag = True
        self.xarr = xarr
        self.yarr = yarr

        npts10 = len(xarr)*10
        #interp by factor of 10
        self.x10 = np.linspace (xarr[0], xarr[-1], npts10)
        sfcn = interpolate.interp1d (xarr, yarr, kind='cubic')
        self.yarrSpline = sfcn(self.x10)
        self.plotData ()

    def setOverlayXYData (self, xarr, yarr, secFlag) :
        self.xarrOlay = xarr
        self.yarrOlay = yarr
        self.olayFlag = True ;
        self.plotData ()

    def setXYData_Integrate (self,xarr, yarr) :
        self.tstr =  "Image Integration"
        self.xstr = "2 Theta"
        self.ystr = "Average Intensity"
        self.xarr = xarr
        self.yarr = yarr
        self.pType = 0
        self.plotDataFlag = True
        self.plotData()


    def createCosData (self) :
        self.xarr = np.arange (-math.pi, math.pi, math.pi/16.)
        self.yarr = self.xarr.copy()
        for i in range( len(self.xarr)) :
            self.yarr[i] = math.cos(self.xarr[i])
        xarr = self.xarr
        yarr = self.yarr
        npts10 = len(xarr)*10
        #interp by factor of 10
        self.x10 = np.linspace (xarr[0], xarr[-1], npts10)
        sfcn = interpolate.interp1d (xarr, yarr, kind='cubic')
        self.yarrSpline = sfcn(self.x10)

        #ftest = open ("/home/harold/cosxy.txt", 'w')
        #for i in range (npts10) :
        #   line = "%f %f\n"%(self.x10[i], self.yarrSpline[i])
        #  ftest.write (line)
        #ftest.close()


    def setpType (self, type):
        self.pType = type

    def setLabels (self, titleString, xString, yString):

        self.tstr = titleString
        self.xstr = xString
        self.ystr = yString


    def outputToFile (self, fname) :
        self.figure.savefig (fname)