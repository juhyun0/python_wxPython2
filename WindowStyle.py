# -*- coding: utf-8 -*-
import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent=None, title="Window Style")
		self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButtonDown)
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRButtonDown)

	def OnMouseLButtonDown(self, event):
		self.SetWindowStyle(wx.SYSTEM_MENU | wx.FRAME_TOOL_WINDOW)
		self.Refresh()

	def OnMouseRButtonDown(self, event):
		frame.SetWindowStyle(wx.CAPTION | wx.MAXIMIZE_BOX)

if __name__=="__main__":
	app=wx.App()
	frame=MyFrame()
	frame.Show()

	app.MainLoop()
