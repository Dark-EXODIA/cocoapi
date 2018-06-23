import sys
from coco import COCO
import os

annFile='%s/annotations/instances_%s.json'%("/content/darkflow/train","train2014")
labelnames=[""
,"person"
,"bicycle"
,"car"
,"motorbike"
,"aeroplane"
,"bus"
,"train"
,"truck"
,"boat"
,"traffic light"
,"fire hydrant"
,"stop sign"
,"parking meter"
,"bench"
,"bird"
,"cat"
,"dog"
,"horse"
,"sheep"
,"cow"
,"elephant"
,"bear"
,"zebra"
,"giraffe"
,"backpack"
,"umbrella"
,"handbag"
,"tie"
,"suitcase"
,"frisbee"
,"skis"
,"snowboard"
,"sports ball"
,"kite"
,"baseball bat"
,"baseball glove"
,"skateboard"
,"surfboard"
,"tennis racket"
,"bottle"
,"wine glass"
,"cup"
,"fork"
,"knife"
,"spoon"
,"bowl"
,"banana"
,"apple"
,"sandwich"
,"orange"
,"broccoli"
,"carrot"
,"hot dog"
,"pizza"
,"donut"
,"cake"
,"chair"
,"sofa"
,"pottedplant"
,"bed"
,"diningtable"
,"toilet"
,"tvmonitor"
,"laptop"
,"mouse"
,"remote"
,"keyboard"
,"cell phone"
,"microwave"
,"oven"
,"toaster"
,"sink"
,"refrigerator"
,"book"
,"clock"
,"vase"
,"scissors"
,"teddy bear"
,"hair drier"
,"toothbrush"]
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
        if (labelnames[anns[i]['category_id']] in neededlabels):
            bbox = anns[i]['bbox']
            xml += '<object>\n<name>' + str(labelnames[anns[i]['category_id']]) + '</name>\n'
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
