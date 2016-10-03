from PyQt4 import QtCore, QtGui

##
# mySessionLogWidget
# This class inherits QListWidget.
# The QListWidget on the "Session Log" tab is promoted to the class
# The add Event method is used to add a timestamped string to that list widget
class mySessionLogWidget (QtGui.QListWidget) :
    def __init__(self, parent):
        QtGui.QListWidget.__init__(self,parent)
        date = QtCore.QDate.currentDate().toString()
        time = self.getTimeString()
        str = "%s\r\n%s : Session start time"%(date,time)
        self.addItem (str)



    def getTimeString (self) :
        t= QtCore.QTime.currentTime()
        s = t.toString ()
        return s

    def addEvent (self, str) :
        time = self.getTimeString()
        str = "%s : %s"%(time, str)
        self.addItem (str)