from PyQt5.QtCore import *

class PeakObject :
    xloc = 0
    yloc = 0
    ident = ""
    selected = False

    def __init__(self, x, y) :
        self.xloc = x
        self.yloc = y


    def x(self) :
        return self.xloc
    def y(self) :
        return self.yloc

    """ setSelected will set the selected member to the boolean value
        defined by state
        """
    def setSelected (self, state) :
        self.selected = state
