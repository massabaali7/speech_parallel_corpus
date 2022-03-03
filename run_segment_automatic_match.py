#from inaSpeechSegmenter import Segmenter, seg2csv
from csvfrp import repcm
from csvfrp import addDu
from chunkBasedLabel import chunkizeSeg
from SST import STTI
from google_trans import trans2Trgt
from text_similarity_ar_dialect import sim_dub_trans_org
from automated_match import matchSegments
import string
import os
import sys 

def setPaths(newpath, idA, filenameDub,filenameOrg):
  ARcsv = open(newpath + filenameDub+".csv")
  ARcsv = newpath + filenameDub+".csv"
  os.mkdir(newpath+filenameDub+"/")
  os.mkdir(newpath+filenameOrg+"/")
  pathChunksAR = os.mkdir(newpath+filenameDub+"/Speech/")
  pathChunksAR = newpath+filenameDub+"/Speech/"
  transPathAR = os.mkdir(newpath+filenameDub+"/transcript/")
  transPathAR = newpath+filenameDub+"/transcript/"
  ENcsv = open(newpath + filenameOrg +".csv")
  ENcsv = newpath + filenameOrg +".csv"
  pathChunksEN =  os.mkdir(newpath+filenameOrg+"/Speech/")
  pathChunksEN =  newpath+filenameOrg+"/Speech/"
  transPathEN = os.mkdir(newpath+filenameOrg+"/transcript/")
  transPathEN = newpath+filenameOrg+"/transcript/"
  newtransPathAR = os.mkdir(newpath + "transOrg/")
  newtransPathAR = newpath + "transOrg/"
  filenameSim = open(newpath+"simDub_OrgTrans.txt", "w+")
  filenameSim = newpath+"simDub_OrgTrans.txt"
  csvresult = open(newpath+"result"+".csv", "w+")
  csvresult = newpath+"result"+".csv"
  return newpath, ARcsv,pathChunksAR,transPathAR,ENcsv,pathChunksEN,transPathEN,newtransPathAR,filenameSim,csvresult
  
def seg_chunk(pathChunks,csvpath,mediawav,idA):
    chunkizeSeg(pathChunks, csvpath, mediawav, idA)


idA = "sponge"

newpath = sys.argv[1]
filenameDub = sys.argv[2]
filenameOrg = sys.argv[3]
langOrg = sys.argv[4]
langDub = sys.argv[5]
newpath, ARcsv,pathChunksAR,transPathAR,ENcsv,pathChunksEN,transPathEN,newtransPathAR,filenameSim,csvresult=setPaths(newpath, idA, filenameDub,filenameOrg)
print("Segmenting the wav file based on VAD ")
seg_chunk(pathChunksEN, ENcsv,newpath+filenameOrg+".wav",idA)
seg_chunk(pathChunksAR, ARcsv,newpath+filenameDub+".wav",idA)

print("Transcribing the Original and the Dubbed audio ")

STTI(ARcsv, transPathAR, pathChunksAR, langDub) 
STTI(ENcsv, transPathEN, pathChunksEN, langOrg) 
print("Translating the original audio to the dubbed audio")
try:
	trans2Trgt(transPathEN,newtransPathAR,langDub) 
except:
	print("failed to translate")
print("Similarity between Original_translated & Dubbed ")
sim_dub_trans_org(newtransPathAR,transPathAR,filenameSim ) 
print("Matching the segments")
matchSegments(ENcsv, ARcsv, csvresult, filenameSim) 
