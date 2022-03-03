from googletrans import Translator
    
# In[11]:
from numpy import random
import glob
import os
translator = Translator()
preds = [] 

def trans2Trgt(pathOrg, pathTransDub, lang): # Translates original series to dubbed version to check the similarity 
    translator = Translator()
    for zaj in glob.glob(pathOrg + "*.*", recursive=True):
      iz = open(zaj, encoding="utf8")
      base=os.path.basename(zaj)
      kma, ex = os.path.splitext(base)
      ot = open(pathTransDub+kma+".txt", "w", encoding= 'utf-8')
      Lines = iz.readlines() 
      kzO = []
      
      for line in Lines:
        try:
          z = translator.translate(line, dest=lang)
          ot.write(z.text+"\n")
        except:
          print(line)
          continue
        
        
      iz.close()
      ot.close()


