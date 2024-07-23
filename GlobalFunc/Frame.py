from abc import ABC, abstractmethod

import wx

from GlobalFunc.FileManage import Save
from GlobalFunc.Func import outCode
from GlobalFunc.Func import restartProgram


class AbstractFrame(ABC):
    def __init__(self, title, returntoback, aams, loc="0"):

        # ------------
        # aams,loc="0"根据我的情境需求添加的
        # ------------

        # 默认测试美化的带盒子和面板的实例
        self.frame = wx.Frame(None, title=title, size=(300, 400), style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self.frame)
        self.panel.SetSizer(self.vbox)
        self.menuBar = wx.MenuBar()
        # 提前绑定按钮
        self.frame.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=100)
        self.frame.Bind(wx.EVT_MENU, self.onClick, id=101, id2=200)
        # 面板相互跳转
        self.returnButton = wx.Button(self.panel, id=901, label="点击返回")
        self.frame.Bind(wx.EVT_BUTTON, self.comeToBack, id=901)
        self.frame.Bind(wx.EVT_MENU, self.onClickMenu, id=903, id2=907)
        self.returntoback = returntoback

        # ------------------------根据我的情境需求添加的
        self.aboutUs = wx.Menu()
        self.aboutUs.Append(903, "&联系作者")
        self.aboutUs.Append(904, "&更新日志")
        self.menuBar.Append(self.aboutUs, "&关于我们")
        self.funC = wx.Menu()
        self.funC.Append(905, "&返回主界面")
        self.funC.Append(906, "&手动保存")
        self.menuBar.Append(self.funC, "&功能")
        self.aams = aams
        self.loc = loc
        if loc == "0":
            self.code = outCode()
            self.codeButton = wx.Button(self.panel, id=902, label=f"{self.code}")
            self.frame.Bind(wx.EVT_BUTTON, self.reloadCode, id=902)
            self.keyCode = wx.TextCtrl(self.panel)
            self.keyCode.SetValue("请输入验证码")
            self.codeBox = wx.BoxSizer(wx.HORIZONTAL)
            self.codeBox.Add(self.keyCode, proportion=1, flag=wx.CENTER | wx.ALL, border=10)
            self.codeBox.Add(self.codeButton, proportion=1, flag=wx.CENTER | wx.ALL, border=10)
        # ------------------------根据我的情境需求添加的

        self.frame.Center()
        self.frame.SetMenuBar(self.menuBar)

    @abstractmethod
    def onClick(self, event):
        pass

    # 提前给下级面板封装的‘点击触发 会返回到上级面板’
    def comeToBack(self, event):
        self.frame.Hide()
        self.returntoback()

    # 要传递给下级面板的 用来返回当前面版的函数
    def returnToBack(self):
        self.frame.Show()

    def onClickMenu(self, event):
        eventId = event.GetId()
        if eventId == 903:
            showImg("0.jpg", "联系作者", "QQ:1364596766")
        elif eventId == 904:
            TextFrame(f"{self.aams.updateLog}")
        elif eventId == 905:
            restartProgram()
        elif eventId == 906:
            Save(self.aams)
            MessageFrame("手动保存成功!")

    def reloadCode(self, event):
        self.code = outCode()
        self.codeButton.SetLabel(f"{self.code}")


class MessageFrame(wx.Dialog):
    def __init__(self, message):
        super().__init__(None, title="提示信息", size=(300, 100), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        ExitButton = wx.Button(parent=panel, id=1, label=f"{message}", pos=(30, 10))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(ExitButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1)
        self.Center()
        self.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.Destroy()


class TextFrame(wx.Dialog):
    def __init__(self, info):
        super().__init__(None, title="信息如下", size=(700, 300), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)

        text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        text.SetValue(info)
        ExitButton = wx.Button(parent=panel, id=1, label=f"点击返回", pos=(30, 10))

        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(text, proportion=6, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(ExitButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1)
        self.Center()
        self.ShowModal()
        self.Destroy()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.Destroy()


class showImg(wx.Dialog):
    def __init__(self, img, title, info="0", buttonMessage="0"):
        super().__init__(None, title=f"{title}", size=(400, 400), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        createImg = wx.Image(f'{img}', wx.BITMAP_TYPE_ANY)
        createImg = createImg.Scale(300, 300, wx.IMAGE_QUALITY_HIGH)
        self.img = wx.StaticBitmap(panel, bitmap=createImg)
        vbox.Add(self.img, proportion=6, flag=wx.EXPAND | wx.ALL, border=10)

        if info != "0":
            text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
            text.SetValue(info)
            vbox.Add(text, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        if buttonMessage != "0":
            ExitButton = wx.Button(parent=panel, id=1, label=f"{buttonMessage}")
            vbox.Add(ExitButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1)
        self.Center()
        self.ShowModal()
        self.Destroy()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.Destroy()
