from picamera import PiCamera
import time

class Camera():
	def __init__(self):
		global cam
		cam = PiCamera()
	def preview(self, t):
		cam.start_preview()
		time.sleep(t)
		cam.stop_preview()
	def pic(self, file_location):
		cam.start_preview()
		time.sleep(2)
		cam.capture(file_location)
		cam.stop_preview()
