from flask import Flask, render_template, Response, request
import cv2
import carla
import numpy as np
import argparse

app = Flask(__name__)
img_storage = None


def rgb_callback(image, data_dict):
    img = np.reshape(np.copy(image.raw_data), (image.height, image.width, 4))  # Reshaping with alpha channel
    img[:, :, 3] = 255  # Setting the alpha to 255
    data_dict['rgb_image'] = img


def carla_start_out_img():
    """Video streaming generator function."""

    # Get world
    client = carla.Client('localhost', 2000)
    world = client.get_world()
    world.tick()

    # Find camera
    actors = world.get_actors()
    camera = None

    for a in actors:
        if a.type_id == "sensor.camera.rgb":
            camera = a
            break

    if camera is None:
        raise Exception("No camera detected!")

    image_w = int(camera.attributes["image_size_x"])
    image_h = int(camera.attributes["image_size_y"])

    sensor_data = {'rgb_image': np.zeros((image_h, image_w, 4))}
    camera.listen(lambda image: rgb_callback(image, sensor_data))

    while True:
        # Output camera display
        ret, jpeg = cv2.imencode('.jpg', sensor_data['rgb_image'])
        frame = jpeg.tobytes()
        yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'


def start_video_out_img():
    """Function to stream video from a mp4 file"""
    camera = cv2.VideoCapture(args.video_path)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'


app.config["CACHE_TYPE"] = "null"


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    if args.video_path is None:
        return Response(carla_start_out_img(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return Response(start_video_out_img(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_output', methods=['POST'])
def upload_file():
    # Check if the 'image' file is in the request
    if 'image' in request.files:
        uploaded_file = request.files['image']
        # Read the content of the uploaded file
        file_content = uploaded_file.read()
        # Display the content of the uploaded file
        return f'File Content: {file_content.decode()}'
    else:
        return 'No file uploaded'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000, help='video stream port')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='video stream host')
    parser.add_argument('--video-path', type=str, help='path to video to stream')
    args = parser.parse_args()
    print(args)

    app.run(host='0.0.0.0',
            port=args.port,
            debug=True,
            # threaded=True
            )
