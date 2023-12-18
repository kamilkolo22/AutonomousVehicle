# Run monoloco on webcam with default port
python3 -m monoloco.run predict --webcam -o data/output --output_types 'multi' \
--checkpoint /home/kamil/Pulpit/AV/ml_models/monoloco/checkpoints/shufflenetv2k30-201104-224654-cocokp-d75ed641.pkl

#python3 -m monoloco.run predict --webcam "http://192.168.0.218:5000/video_feed" -o data/output --output_types 'front' \
#--checkpoint /home/kamil/Pulpit/AV/ml_models/monoloco/checkpoints/shufflenetv2k30-201104-224654-cocokp-d75ed641.pkl
