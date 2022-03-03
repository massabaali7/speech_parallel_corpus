import glob 
import collections
import os 
from similarity import TextSimilarity
#from textblob_ar import TextSimilarity


def sim_dub_trans_org(chunksOrg_Trans, chunksDub, sim_matrix_txt):
    trans_d = {}
    for i in glob.glob(chunksOrg_Trans+ "*.*", recursive=True):
        base=os.path.basename(i)
        kma, ex = os.path.splitext(base)
        result = ''.join([s for s in kma if s.isdigit()])
        file = open(i, mode='r', encoding = "utf-8")
        text = file.read()
        trans_d[int(result)] = text

    od_no = collections.OrderedDict(sorted(trans_d.items()))


    dub_d = {}
    for i in glob.glob(chunksDub+ "*.*", recursive=True):
        base=os.path.basename(i)
        kma, ex = os.path.splitext(base)
        result = ''.join([s for s in kma if s.isdigit()])
        file = open(i, mode='r', encoding = "utf-8")
        text = file.read()
        dub_d[int(result)] = text
    print("now")
    od = collections.OrderedDict(sorted(dub_d.items()))
    r = len(trans_d)
    c = len(dub_d)
    print(r)
    print(c)
    Matrix = [[-1 for x in range(c)] for y in range(r)] 
    w = -1
    h = 0
    sim = TextSimilarity()
    try:
        for i in od_no:
            w = w + 1
            h=0 
            for j in od:
                Matrix[w][h] = sim.similarity(od_no[i], od[j]) #Matrix[w][h] = 
                #xxz = Matrix[w][h]
                #file.write(str(Matrix[w][h])+" ")
                h = h + 1
    except:
        print("exception")
        print(w)
        print("\n")
        print(h)
    
    file = open(sim_matrix_txt, mode = 'w', encoding = "utf-8")

    for r in Matrix:
        #i = i + 1 
        for c in r:
            file.write(str(c)+" ")
        file.write("\n")