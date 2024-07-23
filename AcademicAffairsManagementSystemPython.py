
import GlobalPanel
import wx

from FileManage import initList
from Frame.StartFrame import StartFrame
from Person.Teacher import Teacher




gp = GlobalPanel.GlobalPanel
initList(gp)







app = wx.App()
frm = StartFrame(gp)
frm.Show()

app.MainLoop()
