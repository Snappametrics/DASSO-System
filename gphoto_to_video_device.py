
import gphoto2 as gp
from subprocess import Popen, PIPE
import pdb
import cv2
camera = gp.Camera()
camera.init()
ffmpeg = Popen(['ffmpeg', '-r', '24', '-i', '-', '-vcodec', 'rawvideo', '-pix_fmt', 'yuv420p', '-f', 'v4l2', '-r', '24', '/dev/video0'], stdin=PIPE)

while True:
  capture = camera.capture_preview()
  filedata = capture.get_data_and_size()
  data = memoryview(filedata)
  #data.tolist()
  ffmpeg.stdin.write(data.tobytes())

      