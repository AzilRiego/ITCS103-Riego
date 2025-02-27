import wx

class MyApp(wx.App):
    def OnInit(self):
        """Widgets"""
        frame = wx.Frame(None,title = "Quack", size=(300 , 200))
        panel = wx.Panel(frame)
        text = wx.StaticText(frame, label = "Welcome to wxPy", pos=(90,50))
        frame.Show()
        return True

app = MyApp()
app.MainLoop()