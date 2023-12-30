import time
import cv2
import glob
import shutil
from toolbox.find_camera import find_camera


camera = find_camera()

camera.listen(lambda image: image.save_to_disk('../test_videos/temp_images/%06d.jpg' % image.frame))

print("Recording started, press ctr+C to stop recording...")

# Record data until key interrupt
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    camera.stop()
    print("KeyboardInterrupt: Recording stopped!")

frameSize = (800, 600)

out = cv2.VideoWriter('../test_videos/output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, frameSize)

for filename in glob.glob('../test_videos/temp_images/*.jpg'):
    img = cv2.imread(filename)
    out.write(img)

out.release()

shutil.rmtree('../test_videos/temp_images')
print("Record saved, temporary images deleted.")
time.sleep(2)
