# -*- coding: utf-8 -*-

from PIL import ImageGrab
import time

class ScrPic:
	def __init__(self):
		pass
		
	def Get(self,path):
		strtime = time.strftime('%d%H%M%S',time.localtime())
		pic = ImageGrab.grab()
		pic.save(path +strtime+".jpg")
		return path +strtime+".jpg"

if __name__=='__main__':
	sp = ScrPic()
	sp.Get("")