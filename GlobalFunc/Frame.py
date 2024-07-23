from abc import ABC, abstractmethod

import wx

from GlobalFunc.Func import outCode


class AbstractFrameC(ABC):
    def __init__(self, title, returntoback, aams):
        # 默认测试美化的带盒子和面板的实例
        self.frame = wx.Frame(None, title=title, size=(300, 400), style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self.frame)
        self.panel.SetSizer(self.vbox)
        self.code = outCode()
        # 提前绑定按钮
        self.frame.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=100)
        # 面板相互跳转
        self.returnButton = wx.Button(self.panel, id=101, label="点击返回")
        self.codeButton = wx.Button(self.panel, id=102, label=f"{self.code}")
        self.frame.Bind(wx.EVT_BUTTON, self.comeToBack, id=101)
        self.frame.Bind(wx.EVT_BUTTON, self.reloadCode, id=102)
        self.returntoback = returntoback

        self.aams = aams  # 根据情境需求 添加的参数 多出来的数组

        self.keyCode = wx.TextCtrl(self.panel)
        self.keyCode.SetValue("请输入验证码")

        self.codeBox = wx.BoxSizer(wx.HORIZONTAL)
        self.codeBox.Add(self.keyCode, proportion=1, flag=wx.CENTER | wx.ALL, border=10)
        self.codeBox.Add(self.codeButton, proportion=1, flag=wx.CENTER | wx.ALL, border=10)

    # 提前给下级面板封装的‘点击触发 会返回到上级面板’
    def comeToBack(self, event):
        self.frame.Hide()
        self.returntoback()

    # 要传递给下级面板的 用来返回当前面版的函数
    def returnToBack(self):
        self.frame.Show()

    def reloadCode(self, event):
        self.code = outCode()
        self.codeButton.SetLabel(f"{self.code}")

    @abstractmethod
    def onClick(self, event):
        pass


class AbstractFrame(ABC):
    def __init__(self, title, returntoback, aams, loc):
        # 默认测试美化的带盒子和面板的实例
        self.frame = wx.Frame(None, title=title, size=(300, 400), style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self.frame)
        self.panel.SetSizer(self.vbox)
        # 提前绑定按钮
        self.frame.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=100)
        # 面板相互跳转
        self.returnButton = wx.Button(self.panel, id=101, label="点击返回")
        self.frame.Bind(wx.EVT_BUTTON, self.comeToBack, id=101)
        self.returntoback = returntoback
        self.loc = loc
        self.aams = aams  # 根据情境需求 添加的参数 多出来的数组

    # 提前给下级面板封装的‘点击触发 会返回到上级面板’
    def comeToBack(self, event):
        self.frame.Hide()
        self.returntoback()

    # 要传递给下级面板的 用来返回当前面版的函数
    def returnToBack(self):
        self.frame.Show()

    @abstractmethod
    def onClick(self, event):
        pass


class MessageFrame(wx.Dialog):
    def __init__(self, message):
        super().__init__(None, title="提示信息", size=(300, 100), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        ExitButton = wx.Button(parent=panel, id=1, label=f"{message}", pos=(30, 10))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(ExitButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1)
        self.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.Destroy()


class TextFrame(wx.Dialog):
    def __init__(self, info):
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
