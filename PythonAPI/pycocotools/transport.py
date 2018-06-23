import sys
from coco import COCO
import os

annFile='%s/annotations/instances_%s.json'%("/content/darkflow/train","train2014")

labelnames=[None]*91
labelnames[ 1 ]= "person" 
labelnames[ 2 ]= "bicycle" 
labelnames[ 3 ]= "car" 
labelnames[ 4 ]= "motorcycle" 
labelnames[ 5 ]= "airplane" 
labelnames[ 6 ]= "bus" 
labelnames[ 7 ]= "train" 
labelnames[ 8 ]= "truck" 
labelnames[ 9 ]= "boat" 
labelnames[ 10 ]= "traffic light" 
labelnames[ 11 ]= "fire hydrant" 
labelnames[ 13 ]= "stop sign" 
labelnames[ 14 ]= "parking meter" 
labelnames[ 15 ]= "bench" 
labelnames[ 16 ]= "bird" 
labelnames[ 17 ]= "cat" 
labelnames[ 18 ]= "dog" 
labelnames[ 19 ]= "horse" 
labelnames[ 20 ]= "sheep" 
labelnames[ 21 ]= "cow" 
labelnames[ 22 ]= "elephant" 
labelnames[ 23 ]= "bear" 
labelnames[ 24 ]= "zebra" 
labelnames[ 25 ]= "giraffe" 
labelnames[ 27 ]= "backpack" 
labelnames[ 28 ]= "umbrella" 
labelnames[ 31 ]= "handbag" 
labelnames[ 32 ]= "tie" 
labelnames[ 33 ]= "suitcase" 
labelnames[ 34 ]= "frisbee" 
labelnames[ 35 ]= "skis" 
labelnames[ 36 ]= "snowboard" 
labelnames[ 37 ]= "sports ball" 
labelnames[ 38 ]= "kite" 
labelnames[ 39 ]= "baseball bat" 
labelnames[ 40 ]= "baseball glove" 
labelnames[ 41 ]= "skateboard" 
labelnames[ 42 ]= "surfboard" 
labelnames[ 43 ]= "tennis racket" 
labelnames[ 44 ]= "bottle" 
labelnames[ 46 ]= "wine glass" 
labelnames[ 47 ]= "cup" 
labelnames[ 48 ]= "fork" 
labelnames[ 49 ]= "knife" 
labelnames[ 50 ]= "spoon" 
labelnames[ 51 ]= "bowl" 
labelnames[ 52 ]= "banana" 
labelnames[ 53 ]= "apple" 
labelnames[ 54 ]= "sandwich" 
labelnames[ 55 ]= "orange" 
labelnames[ 56 ]= "broccoli" 
labelnames[ 57 ]= "carrot" 
labelnames[ 58 ]= "hot dog" 
labelnames[ 59 ]= "pizza" 
labelnames[ 60 ]= "donut" 
labelnames[ 61 ]= "cake" 
labelnames[ 62 ]= "chair" 
labelnames[ 63 ]= "couch" 
labelnames[ 64 ]= "potted plant" 
labelnames[ 65 ]= "bed" 
labelnames[ 67 ]= "dining table" 
labelnames[ 70 ]= "toilet" 
labelnames[ 72 ]= "tv" 
labelnames[ 73 ]= "laptop" 
labelnames[ 74 ]= "mouse" 
labelnames[ 75 ]= "remote" 
labelnames[ 76 ]= "keyboard" 
labelnames[ 77 ]= "cell phone" 
labelnames[ 78 ]= "microwave" 
labelnames[ 79 ]= "oven" 
labelnames[ 80 ]= "toaster" 
labelnames[ 81 ]= "sink" 
labelnames[ 82 ]= "refrigerator" 
labelnames[ 84 ]= "book" 
labelnames[ 85 ]= "clock" 
labelnames[ 86 ]= "vase" 
labelnames[ 87 ]= "scissors" 
labelnames[ 88 ]= "teddy bear" 
labelnames[ 89 ]= "hair drier" 
labelnames[ 90 ]= "toothbrush" 
neededlabels=["person","dog","car","bicycle"]
coco=COCO(annFile)
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]

imgIds = coco.getImgIds()

takeXml=0
directory = './annotations_pascalformat/'
if not os.path.exists(directory):
    os.makedirs(directory)

for n in range(len(imgIds)):
    img = coco.loadImgs(imgIds[n])[0]
    annIds = coco.getAnnIds(imgIds=img['id'], iscrowd=None)
    anns = coco.loadAnns(annIds)

    xml = '<annotation>\n<folder>\nCOCO2014pascalformat\n</folder>\n<filename>'
    xml += img['file_name'] + '</filename>\n<source>\n<database>\nCOCO2014pascalformat\n</database>\n</source>\n<size>\n'
    xml += '<width>\n' + str(img['width']) + '\n</width>\n' + '<height>\n' + str(img['height']) + '\n</height>\n'
    xml += '<depth>\n3\n</depth>\n</size>\n<segmented>\n0\n</segmented>\n'

    for i in range(len(anns)):
        if (labelnames[int(anns[i]['category_id'])] in neededlabels):
            bbox = anns[i]['bbox']
            xml += '<object>\n<name>' + str(labelnames[int(anns[i]['category_id'])]) + '</name>\n'
            xml += '<bndbox>\n<xmin>\n' + str(int(round(bbox[0]))) + '\n</xmin>\n'
            xml += '<ymin>\n' + str(int(round(bbox[1]))) + '\n</ymin>\n'
            xml += '<xmax>\n' + str(int(round(bbox[0] + bbox[2]))) + '\n</xmax>\n'
            xml += '<ymax>\n' + str(int(round(bbox[1] + bbox[3]))) + '\n</ymax>\n</bndbox>\n'
            xml += '<truncated>\n0\n</truncated>\n<difficult>\n0\n</difficult>\n</object>\n'
            takeXml=1
    xml += '</annotation>'
    if(takeXml):
        f_xml = open(directory + img['file_name'].split('.jpg')[0] + '.xml', 'w')
        f_xml.write(xml)
        f_xml.close()
    takeXml=0
    print (str(n) + ' out of ' + str(len(imgIds)))