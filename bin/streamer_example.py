#!/usr/bin/env python2
'''
	Author: Igor Maculan - n3wtron@gmail.com
	A Simple mjpg stream http server
'''
import cv2
import threading
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import StringIO
import time, sys
capture=None

class CamHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path.endswith(sys.argv[2]):
			self.send_response(200)
			self.send_header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
			self.end_headers()
			while True:
				try:
					rc,img = capture.read()
					if not rc:
						continue
					r, jpg = cv2.imencode('*.jpeg', img)
					tmpFile = StringIO.StringIO()
					self.wfile.write("--jpgboundary")
					self.send_header('Content-type','image/jpeg')
					self.send_header('Content-length',str(tmpFile.len))
					self.end_headers()
					self.wfile.write(jpg.tostring())
					time.sleep(0.05)
				except KeyboardInterrupt:
					break
				finally:
					capture.close()
			return
		else:
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write('<html><head></head><body>')
			self.wfile.write('<img src="http://127.0.0.1:8080/{0}"/>'.format(sys.argv[2]))
			self.wfile.write('</body></html>')
			return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

def main():
	global capture
	capture = cv2.VideoCapture(0)
	capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320); 
	capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240);
	capture.set(cv2.cv.CV_CAP_PROP_SATURATION,0.2);
	global img
	try:
		server = ThreadedHTTPServer(('localhost', 8080), CamHandler)
		print "server started"
		server.serve_forever()
	except KeyboardInterrupt:
		capture.release()
		server.socket.close()

if __name__ == '__main__':
	main()
