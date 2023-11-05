# python detect.py --weights weights/yolov7.pt --conf 0.25 --img-size 640 --source "http://192.168.0.218:5000/video_feed" --project "runs" --no-trace
python detect.py --weights weights/yolov7.pt --conf 0.25 --img-size 640 --source "http://192.168.0.218:5000/video_feed" \
--project "runs" --no-trace --server-output "http://192.168.0.218:5000/video_output"
