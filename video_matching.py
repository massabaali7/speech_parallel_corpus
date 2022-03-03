import cv2
import imutils
import os
import image_similarity_measures
from sys import argv
from image_similarity_measures.quality_metrics import rmse, ssim, sre
from pydub import AudioSegment

def retDic(filename):
  cap = cv2.VideoCapture(filename)
  cnt = 0
  sec = 0
  seconds = []
  dicVideo1 = {}
  frameRate = 1 #capture image in each 1 sec
  while(cap.isOpened()):
      sec = sec + frameRate
      sec = round(sec,2)
      cap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
      ret, img = cap.read()
      if ret:
          img = imutils.resize(img, width=320)
          dicVideo1[sec] = img
          seconds.append(sec)
          pos_frame = cap.get(1)
          cnt = cnt + 1
          if cv2.waitKey(1) & 0xFF == ord('q'): #press q to quit
              break
      else:
          # The next frame is not ready, so we try to read it again
          cap.set(1, pos_frame-1)
          print ("frame is not ready")
          # It is better to wait for a while for the next frame to be ready
          cv2.waitKey(1000)
          #kill open cv things
          cap.release()
      if cv2.waitKey(10) == 27:
          break
  cap.release()
  cv2.destroyAllWindows()
  return dicVideo1, seconds

def retCorrupt_Consecu_frames(dicVid1,dicVid2,LenVid1,LenVid2,secVid1, secVid2):  
  cnt = 0
  corrupted_frames = {}
  consecutive_frames_end = {}
  # len of dictionary 
  if LenVid1 >= LenVid2:
    for s in secVid1:
      j = 0 
      if not s+j <= LenVid2:
        consecutive_frames_end[s] = dicVid1[s]
        y = list(dicVid1)[-1]
        consecutive_frames_end[y] = dicVid1[y]
        break
      while j <= 16: #and s+j <= LenVid2:
        z = ssim(dicVid1[s], dicVid2[s+j])
        if z >= 0.75:
          break 
        if j == 16:
          corrupted_frames[s] = dicVid1[s]
        j = j + 1
  elif LenVid2 > LenVid1:
    for s in secVid2:
      j = 0 
      if not s+j <= LenVid1:
        consecutive_frames_end[s] = dicVid2[s]
        y = list(dicVid2)[-1]
        consecutive_frames_end[y] = dicVid2[y]
        break
      while j <= 16: #and s+j <= LenVid1:
        z = ssim(dicVid1[s+j], dicVid2[s])
        if z >= 0.75:
          break 
        if j == 16:
          corrupted_frames[s] = dicVid2[s]
        j = j + 1
  return corrupted_frames, consecutive_frames_end

def Vid2Wav(filename):
  newAudio = AudioSegment.from_file(filename)
  fname = os.path.splitext(filename)[0]
  newAudio.export(fname+".wav", format="wav") #Exports to a wav file in the current path.

def rmv_consec_frames(consecutive_frames_end, LenVid1, LenVid2, filename1,filename2):
  if consecutive_frames_end and LenVid1 >= LenVid2:
    newAudio = AudioSegment.from_wav(filename1)
    endTime = list(consecutive_frames_end.keys())[0] * 1000
    newAudio = newAudio[0:endTime]
    newAudio.export(filename1, format="wav") #Exports to a wav file in the current path.
  elif consecutive_frames_end and LenVid2 > LenVid1:
    newAudio = AudioSegment.from_wav(filename2)
    endTime = list(consecutive_frames_end.keys())[0] * 1000
    newAudio = newAudio[0:endTime]
    newAudio.export(filename2, format="wav") #Exports to a wav file in the current path.

def rmv_corrupted_frames(corrupted_frames, LenVid1, LenVid2, filename1,filename2):
  if corrupted_frames and LenVid1 >= LenVid2:
    sound = AudioSegment.from_wav(filename1)
    t1 = 0
    chunks = []
    for cr in corrupted_frames: 
      t2 = cr
      chunks.append(sound[t1*1000 :t2*1000])
      t1 = t2 + 1
    s = sum(chunks)
    s.export(filename1, format = "wav")
  elif corrupted_frames and LenVid2 > LenVid1:
    sound = AudioSegment.from_wav(filename2)
    t1 = 0
    chunks = []
    for cr in corrupted_frames: 
      t2 = cr
      chunks.append(sound[t1*1000 :t2*1000])
      t1 = t2 + 1
    s = sum(chunks)
    s.export(filename2, format = "wav")
