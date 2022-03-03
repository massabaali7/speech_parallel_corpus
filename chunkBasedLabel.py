# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:24:50 2020

@author: mab87
"""


import pandas as pd 
from pydub import AudioSegment 
import os 
import glob




def chunkizeSeg(pathChunks, pathCSV, pathwav, idseries):
    #splitAudio(file_nameT)
    kj = pd.read_csv(pathCSV)
    startSec = kj['start']
    endSec = kj['stop']

    k = 1
     
    # Time to miliseconds
    for i in range(len(kj)):
        startTime = startSec[i]*1000
        endTime = endSec[i]*1000
        
        # Opening file and extracting segment
        song = AudioSegment.from_file( pathwav ) #+'.mp4' pathT + 
        extract = song[startTime:endTime]
        base=os.path.basename(pathwav)
        s, ex = os.path.splitext(base)
        # Saving
        extract.export( pathChunks+idseries+"chunk"+str(i)+".wav", format="wav") 
