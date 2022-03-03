# replace tabs with comma 
import pandas as pd 

def repcm(f):
    reading_file = open(f, "r")

    new_file_content = ""
    for line in reading_file:
      stripped_line = line.strip()
      new_line = stripped_line.replace("\t", ",")
      new_file_content += new_line +"\n"
    reading_file.close()

    writing_file = open(f, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
def addDu(f):
    s = pd.read_csv(f)
    i = 0
    l = []
    ind = []
    
    while i < len(s):
        l.append(s['stop'][i] - s['start'][i])
        ind.append(i)
        i = i + 1
        
    s.insert(3,"Duration", l)
    s.insert(4, "Index1", ind)
    s.to_csv(f,  index=False)