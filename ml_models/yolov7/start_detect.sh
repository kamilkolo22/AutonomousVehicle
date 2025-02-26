# Run Yolo for default camera stream
#python detect.py --weights weights/yolov7.pt --conf 0.25 --img-size 640 --source 0 --project "runs" --no-trace

# Run Yolo for http stream with default output
# python detect.py --weights weights/yolov7.pt --conf 0.25 --img-size 640 --source "http://192.168.0.218:5000/video_feed" \
# --project "runs" --no-trace

# Run Yolo for http stream with http output
#python detect.py --weights weights/yolov7.pt --conf 0.25 --img-size 640 --source "http://192.168.0.218:5000/video_feed" \
#--project "runs" --no-trace --server-output "http://192.168.0.218:5000/video_output"

# Run Yolo on docker (weights in volume and output to volume)
#python detect.py --weights volume/yolov7.pt --conf 0.25 --img-size 640 \
#--source volume/solar_belgia.mp4 --project volume

# Run Yolo on docker (output to volume)
python detect.py --weights weights/yolov7.pt --conf 0.25 --img-size 640 \
--source volume/solar_belgia.mp4 --project volume
