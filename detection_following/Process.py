import pyrealsense2 as rs
import torchvision
import torch
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
import rospkg
# Import Numpy for easy array manipulation
import numpy as np
# Import OpenCV for easy image rendering
import cv2
#import matplotlib.pyplot as plt
#from PIL import Image
from torchvision import transforms
import _thread
import threading
import time

print(torch.version.cuda)
print(torch.backends.cudnn.version())
use_gpu = torch.cuda.is_available()
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()
if(use_gpu):
    print(use_gpu)
    model = model.cuda()

print(torch.cuda.is_available())
print(torch.cuda.current_device())

COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

# Create a pipeline
pipeline = rs.pipeline()

# Create a config and configure the pipeline to stream
#  different resolutions of color and depth streams
config = rs.config()
#config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 6)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

profile = config.resolve(pipeline)
# Start streaming
profile = pipeline.start(config)

align_to = rs.stream.color
align = rs.align(align_to)

rospy.init_node('control', anonymous = False)

pub = rospy.Publisher('ControlMessage', Float64, queue_size=10)
forwardmessage = rospy.Publisher('ForwardMessage', Float64, queue_size=10)
rate = rospy.Rate(1000)
left = 0.15
right = -0.15
forward = 0.1

move_cmd = Twist()
move_cmd.linear.x = 0.0
move_cmd.linear.y = 0.0
move_cmd.linear.z = 0.0
move_cmd.angular.x = 0.0
move_cmd.angular.y = 0.0
move_cmd.angular.z = 0.0

def process():
    val_last = 0
    while True:
        frames = pipeline.wait_for_frames()
        # frames.get_depth_frame() is a 640x360 depth image

        # Align the depth frame to color frame
        aligned_frames = align.process(frames)

        # Get aligned frames
        aligned_depth_frame = aligned_frames.get_depth_frame()  # aligned_depth_frame is a 640x480 depth image
        color_frame = aligned_frames.get_color_frame()

        # Validate that both frames are valid
        if not aligned_depth_frame or not color_frame:
            continue

        #depth_image = np.asanyarray(aligned_depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        #img = Image.open(img_path)  # Load the image
        #print("i need to transform image")
        transform = transforms.Compose([transforms.ToTensor()])  # Defining PyTorch Transform
        img = transform(color_image)  # Apply the transform to the image
        img = img.cuda()
        #print("passing to model")
        pred = model([img])  # Pass the image to the model
        pred_class = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in list(pred[0]['labels'].cpu().numpy())]  # Get the Prediction Score

        #print("Original class length:")
        #print(len(pred_class))
        pred_boxes = [[(i[0], i[1]), (i[2], i[3])] for i in list(pred[0]['boxes'].detach().cpu().numpy())]  # Bounding boxes
        pred_score = list(pred[0]['scores'].detach().cpu().numpy())
        # pred_t = [pred_score.index(x) for x in pred_score if x > 0.5][-1]  # Get list of index with score greater than threshold.
        pred_index = [pred_score.index(x) for x in pred_score if x > 0.5]
        #print(np.array(pred_index).shape)
        if (len(pred_index) !=0):
            pred_t = pred_index[-1]
            #print (pred_t)
            print("ok!")


            pred_boxes = pred_boxes[:pred_t + 1]

            pred_class = pred_class[:pred_t + 1]

            # if(len(pred_class) != 0):
            if('person' in pred_class):
                #print("PERSON")
                forwardmessage.publish(forward)
                for i in range(len(pred_boxes)):
                    if(pred_class[i] == 'person'):
                        val = pred_boxes[i][0][0].item()
                        val2 = pred_boxes[i][1][0].item()
                        diff = (val + val2)/2
                        #print(diff)

                        dif = val_last - val
                        if(diff < 280.0):
                            print("moved left")
                            pub.publish(left)

                        if(diff > 380.0):
                            print("moved right")
                            pub.publish(right)

                        if(280.0 < diff < 380.0):
                            print("straight")
                            pub.publish(0.0)


                        val_last = val
                        rate.sleep()

                        cv2.rectangle(color_image, pred_boxes[i][0], pred_boxes[i][1], color=(0, 255, 0),
                                      thickness=2)  # Draw Rectangle with the coordinates
                        cv2.putText(color_image, pred_class[i], pred_boxes[i][0], cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0),
                                    thickness=2)  # Write the prediction class


            else:
                forwardmessage.publish(0.0)
                pub.publish(0.0)
                rate.sleep()

        else:
            forwardmessage.publish(0.0)
            pub.publish(0.0)
            rate.sleep()

        cv2.namedWindow('Align Example', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('Align Example', color_image)
        key = cv2.waitKey(1)
        #Press esc or 'q' to close the image window
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            pipeline.stop()
            break

process()
# process()
# talker()


