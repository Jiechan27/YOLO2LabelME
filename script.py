import os
import json
import base64

path = "I:\\yolov5-master\\run\\exp-seg"  # directory path that contains yolo txt file
label = ['person', 'bicycle']  # label names here
poly_point = 10  # the higher the number, the lesser the polygon point (!even numbers only)
img_width = 1280  # img size
img_height = 720

for i in os.listdir(path):
    if i.endswith(".txt"):
        file = open(path+"\\"+i, 'r')
        Lines = file.readlines()
        point = []
        for c, line in enumerate(Lines):
            content = line.split(" ")
            label = content[0]
            xy = []
            for r in range(1, len(content), poly_point):
                xy.append([float(content[r]) * img_width, float(content[r+1]) * img_height])
            point.append({
                "label": label,
                "points": [x for x in xy],
                "group_id": 0,
                "description": "",
                "shape_type": "polygon",
                "flags": {}
            })

        with open(path +"\\"+ i.split(".")[0]+".jpg", "rb") as image_file:
            base64format = (base64.b64encode(image_file.read())).decode("utf-8")

        x = {
            "version": "5.2.1",
            "flags": {},
            "shapes": [x for x in point],
            "imagePath": i.split(".")[0] + ".jpg",
            "imageData": base64format,
            "imageHeight": img_height,
            "imageWidth": img_width
        }

        json_object = json.dumps(x)
        # Writing to sample.json
        with open(path +"\\"+ i.split(".")[0] + ".json", "w") as outfile:
            outfile.write(json_object)
