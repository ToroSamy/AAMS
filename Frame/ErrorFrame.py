import wx
class ErrorFrame(wx.Dialog):
    def __init__(self,message):
        super().__init__(None, title="提示信息", size=(300, 100), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        ExitButton = wx.Button(parent=panel, id=1, label=f"{message}", pos=(30, 10))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(ExitButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1)

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.Destroy()

class MessageFrame(wx.Dialog):
    def __init__(self,info):
        super().__init__(None, title="信息如下", size=(600, 600), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)

        text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        text.SetValue(info)
        ExitButton = wx.Button(parent=panel, id=1, label=f"点击返回", pos=(30, 10))


        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(text, proportion=6, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(ExitButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1)
        self.ShowModal()
        self.Destroy()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.Destroy()