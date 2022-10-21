from traceback import print_tb
from utils.plots import data_in_json
import glob
import cv2
import json

arr=[]
for i in glob.glob('runs/detect/crops/*'):
    path=i+'/'  
for j in glob.glob(path+'/*'):
    # path2 = j+"/"
    for k in glob.glob(j + "/*"):
        # print("what is j ",k)
        arr.append(k)
dic=dict()
for p in arr:
    dic[p.split('\\')[-2]]=cv2.imread(p)

result=data_in_json(dic)
json.dumps(result)
with open("readOCR.json", "w") as outfile:
    json.dump(result, outfile)
