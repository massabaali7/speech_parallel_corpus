from inaSpeechSegmenter import Segmenter, seg2csv
from csvfrp import repcm
from csvfrp import addDu
import sys
import string
import os
dub = sys.argv[1] # dub wav file 
org = sys.argv[2] # org wav file 

dubName = os.path.splitext(dub)[0]
orgName = os.path.splitext(org)[0]
Dubcsv = open(dubName +".csv", "w+")
Dubcsv = dubName +".csv"
Orgcsv = open(orgName +".csv", "w+")
Orgcsv = orgName +".csv"
seg = Segmenter()
segmentation = seg(dub)
seg2csv(segmentation, Dubcsv) 
repcm(Dubcsv) # replace with tabs comma 

addDu(Dubcsv) # add duration colum


seg = Segmenter()
segmentation = seg(org)
seg2csv(segmentation, Orgcsv) 
repcm(Orgcsv) # replace with tabs comma 

addDu(Orgcsv) # add duration colum