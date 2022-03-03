import pandas as pd 




def matchSegments(trcsv, arcsv, csvresult, txtsim): # two csv files tr ar return csv file for both 
    sumDurationAR = 0
    sumDurationTR = 0
    sumSegmentsAR  = 0
    sumSegmentsTR = 0 
    LstIndAR = []
    LstDuAR = []
    LststrtAR = []
    LststpAR = []
    LstlabAR = []
    LstIndTR = []
    LstDuTR = []
    LststrtTR = []
    LststpTR = []
    LstlabTR = []
    LstSim = [] 
    array2D = []
    param = [2,3]#[2,3] #[5,20]# 8,9
    tr = pd.read_csv(trcsv)
    ar = pd.read_csv(arcsv)
    res = open(csvresult,"w+")
    res.write("0")
    res.close()
    res = pd.read_csv(csvresult)
    #sim = open(txtsim,"r", encoding = "utf-8") # load file into array 2d 
    with open(txtsim, 'r') as f:
        for line in f.readlines():
            array2D.append(line.split(' '))

    l1 = dict()

    i = 0


    x = len(tr)
    y = len(ar)
    i = 0
    j = 0
    while i < x-1:
        j = 0
        while j < y:
            #j = i 
            if abs(int(tr['start'][i])-int(ar['start'][j])) <= param[1] and  abs(int(tr['Duration'][i])-int(ar['Duration'][j])) <= param[0] and tr['labels'][i] == ar['labels'][j] and ar['Speech Recognition'][j] == 1 and tr['Speech Recognition'][i] == 1: 
                if int(tr['Index1'][i]) not in l1 and int(ar['Index1'][j]) not in l1.values():
                    
                    l1[tr['Index1'][i]]= ar['Index1'][j]
                    #l1[X]= Y
                    X = int(tr['Index1'][i])
                    Y = int(ar['Index1'][j])
                    LstIndAR.append(Y)
                    LstIndTR.append(X)
                    LststrtAR.append(ar['start'][j])
                    LststrtTR.append(tr['start'][i])
                    LststpAR.append(ar['stop'][j])
                    LststpTR.append(tr['stop'][i])
                    sumDurationAR = sumDurationAR + int(ar['Duration'][j])
                    sumDurationTR = sumDurationTR + int(tr['Duration'][i])
                    LstDuAR.append(ar['Duration'][j])
                    LstDuTR.append(tr['Duration'][i])
                    LstlabAR.append(ar['labels'][j])
                    LstlabTR.append(tr['labels'][i])
                    RX = int(tr['Index SR'][i])
                    RY = int(ar['Index SR'][j])
                    LstSim.append(array2D[RX-1][RY-1])
                    sumSegmentsAR = sumSegmentsAR + 1
                    sumSegmentsTR = sumSegmentsTR+ 1
                    #l1[X]= Y
                    #print(X+ " "+ Y)
                    
                    
                
            j = j + 1 
        i = i + 1
        
    # 'start' with list of chunks no need for label
    # later step remove from dictionary same values 
    # create three dictionaries 1 for both 1 for tr vs. ar 1 for ar vs. tr
    # last step apply the filtration process which is if less < 2 secs and Index1in SR krmal 2D array 
    #similarity remve if less than <.45
    # remove speaker diarization
    print("---------------------------------------------------")

    i = 0
    j = 0
    du = [] 
    ch = []
    en = []
    l2 = dict()
    try:
        while i < x - 1: 
            j = 0
            z = 0
            du = []
            ch = []
            en = [] # end 
            strt = []
            lab = [] # label 
            simPr = []
            indSR = []
            while j < y:
				#j = i 
                if abs(int(tr['start'][i])-int(ar['start'][j])) <= param[1] and int(tr['stop'][i]) > int(ar['stop'][j]) and tr['labels'][i] == ar['labels'][j] and ar['Speech Recognition'][j] == 1 and tr['Speech Recognition'][i] == 1: 
                    print("passeD")
                    du.append(int(ar['Duration'][j]))
                    ch.append(str(ar['Index1'][j]))
                    en.append(str(ar['stop'][j]))
                    strt.append(str(ar['start'][j]))
                    lab.append(str(ar['labels'][j]))                
                    indSR.append(str(ar['Index SR'][j]))
                    z = j 
                    j = j + 1 
                    continue 
                elif z != 0 and abs(int(ar['stop'][z]) - int(ar['start'][j])) <= 1 and int(tr['stop'][i]) > int(ar['stop'][j]) and ar['labels'][j] != 'noEnergy' and ar['Speech Recognition'][j] == 1 and tr['Speech Recognition'][i] == 1: 
					
                    du.append(int(ar['Duration'][j]))
                    ch.append(str(ar['Index1'][j]))
                    en.append(str(ar['stop'][j]))
                    strt.append(str(ar['start'][j]))
                    lab.append(str(ar['labels'][j]))                
                    indSR.append(str(ar['Index SR'][j]))
                    z = j 
                    j = j + 1 
                    continue 
                elif z!= 0 and abs(int(ar['stop'][z]) - int(ar['start'][j])) <= 1 and abs(int(tr['stop'][i]) - int(ar['stop'][j])) <= 2 and ar['labels'][j] != 'noEnergy' and ar['Speech Recognition'][j] == 1 and tr['Speech Recognition'][i] == 1: 
					#print("passeD")
                    du.append(int(ar['Duration'][j]))
                    ch.append(str(ar['Index1'][j]))
                    en.append(str(ar['stop'][j]))
                    strt.append(str(ar['start'][j]))
                    lab.append(str(ar['labels'][j]))                
                    indSR.append(str(ar['Index SR'][j]))
                    bb = True 
                    if int(tr['Index1']	[i]) not in l2 and int(tr['Index1'][i]) not in l1 and int(ar['Index1'][j]) not in l2.values() and abs(sum(du)-int(tr['Duration'][i])) <= param[0]:
                        s = ';'.join(ch)
                        es = ';'.join(en)
                        rt = ';'.join(strt)
                        lb = ';'.join(lab)
                        du2 = []
                        sumDurationAR = sumDurationAR + sum(du)
                        sumDurationTR = sumDurationTR + int(tr['Duration'][i])
                        sumSegmentsTR = sumSegmentsTR + 1
                        for kz in du:
                            du2.append(str(kz))
                            sumSegmentsAR = sumSegmentsAR + 1
                        drt = ';'.join(du2)
                        
                        inS = ';'.join(indSR)
                        
                        for zzz in ch:
                            if zzz in l1: 
                                bb = False  
                        if bb == False:
                            break
                        l2[tr['Index1'][i]]= s
						#l1[X]= Y
                        X = int(tr['Index1'][i])
                        LstIndAR.append(s)
                        LstIndTR.append(X)
                        LststrtAR.append(rt)
                        LststrtTR.append(tr['start'][i])
                        LststpAR.append(es)
                        LststpTR.append(tr['stop'][i])
                        LstDuAR.append(drt)
                        LstDuTR.append(tr['Duration'][i])
                        LstlabAR.append(lb)
                        LstlabTR.append(tr['labels'][i])
                        RX = int(tr['Index SR'][i])
                        for k in indSR:
                            zi = int(k)
                            simPr.append(str(array2D[RX-1][zi-1]))
                        ziD = ';'.join(simPr)
                        LstSim.append(ziD)
						#Y = str(ar['Index1'][j])
						#l1[X]= Y
						#print(X + " " + s)
						#print(s)
				
					
                j = j + 1 
            i = i + 1
    except:
        print("error")
       
    i = 0
    j = 0
    du = [] 
    ch = []
    en = []
    l2_ar_tr = dict()
    print("---------------------------------------------------")
    while j < y: 
        i = 0
        z = 0
        du = []
        ch = []
        en = [] # end 
        strt = []
        lab = [] # label 
        simPr = []
        indSR = []
        
        while i < x -1:
            #j = i 
            if abs(tr['start'][i].astype(int)-int(ar['start'][j])) <= param[1] and tr['stop'][i].astype(int) < int(ar['stop'][j]) and tr['labels'][i] == ar['labels'][j] and ar['Speech Recognition'][j] == 1 and tr['Speech Recognition'][i] == 1: 
                du.append(int(tr['Duration'][i]))
                ch.append(str(tr['Index1'][i]))
                en.append(str(tr['stop'][i]))
                strt.append(str(tr['start'][i]))
                lab.append(str(tr['labels'][i]))
                indSR.append(str(tr['Index SR'][i]))
                
                z = i 
                i = i + 1
                continue 
            elif z != 0 and abs(tr['stop'][z].astype(int) - tr['start'][i].astype(int)) <= 1 and tr['stop'][i].astype(int) < int(ar['stop'][j]) and tr['labels'][i] != 'noEnergy' and ar['Speech Recognition'][j] == 1 and tr['Speech Recognition'][i] == 1: 
                du.append(int(tr['Duration'][i]))
                ch.append(str(tr['Index1'][i]))
                en.append(str(tr['stop'][i]))
                strt.append(str(tr['start'][i]))
                lab.append(str(tr['labels'][i]))
                indSR.append(str(tr['Index SR'][i]))
                z = i 
                i = i + 1
                continue 
            elif z!= 0 and abs(tr['stop'][z].astype(int) - tr['start'][i].astype(int)) <= 1 and abs(tr['stop'][i].astype(int) - int(ar['stop'][j]))<=2 and tr['labels'][i] != 'noEnergy' and ar['Speech Recognition'][j] == 1 and tr['Speech Recognition'][i] == 1: 
                du.append(int(tr['Duration'][i]))
                ch.append(str(tr['Index1'][i]))
                en.append(str(tr['stop'][i]))
                strt.append(str(tr['start'][i]))
                lab.append(str(tr['labels'][i]))
                indSR.append(str(tr['Index SR'][i]))
                bb = True 
                if ar['Index1'][j].astype(int) not in l2_ar_tr and int(ar['Index1'][j]) not in l1 and int(tr['Index1'][i]) not in l2_ar_tr.values() and abs(sum(du)-int(ar['Duration'][j])) <= param[0]:
                    s = ';'.join(ch)
                    es = ';'.join(en)
                    rt = ';'.join(strt)
                    lb = ';'.join(lab)
                    du2 = []
                    sumDurationAR = sumDurationAR + int(ar['Duration'][j])
                    sumDurationTR = sumDurationTR + sum(du)
                    sumSegmentsAR = sumSegmentsAR + 1
                    for kz in du:
                       du2.append(str(kz))
                       sumSegmentsTR = sumSegmentsTR + 1
                    drt = ';'.join(du2)
                    inS = ';'.join(indSR)
                    for zzz in ch:
                        if zzz in l1: 
                          bb = False  
                    if bb == False:
                        break
                    l2_ar_tr[ar['Index1'][j]]= s
                    #l1[X]= Y
                    X = int(ar['Index1'][j])
                    LstIndAR.append(X)
                    LstIndTR.append(s)
                    LststrtAR.append(ar['start'][j])
                    LststrtTR.append(rt)
                    LststpAR.append(ar['stop'][j])
                    LststpTR.append(es)
                    LstDuAR.append(ar['Duration'][j])
                    LstDuTR.append(drt)
                    LstlabAR.append(ar['labels'][j])
                    LstlabTR.append(lab)
                    RX = int(ar['Index SR'][j])
                    for k in indSR:
                        zi = int(k)
                        simPr.append(str(array2D[zi-1][RX-1]))   
                    ziD = ';'.join(simPr)
                    LstSim.append(ziD)
                    #Y = str(ar['Index1'][j])
                    #l1[X]= Y
                    
                    #print(X + " " + s)
                    #print(s)

                
            i = i + 1 
        j = j + 1   
    res.insert(1, "Dub", LstIndAR )
    res.insert(2, "startDub", LststrtAR )
    res.insert(3, "stopDub", LststpAR )
    res.insert(4, "DurationDub", LstDuAR )
    res.insert(5, "labelDub", LstlabAR )
    res.insert(6, "Org", LstIndTR )
    res.insert(7, "startOrg",LststrtTR  )
    res.insert(8, "stopOrg", LststpTR )
    res.insert(9, "DurationOrg", LstDuTR )
    res.insert(10, "labelOrg",LstlabTR )
    res.insert(11, "Similarity",LstSim )
    ####fiDu = open("/home/local/QCRI/mab87/dataset_TR_AR/New/fadileh/duration.txt", "a+")
    sumDuAR = 0
    sumDuTR = 0
    #for iduAR in LstDuAR:
      #  sumDuAR = sumDuAR + int(iduAR)
    #for iduTR in LstDuTR:
      #  sumDuTR = sumDuTR + int(iduTR)
    x = 0
    #fiDu.write("AR "+str(sumDurationAR)+ " TR " + str(sumDurationTR) + "\n" )
    #fiDu.close()
    #s.insert(3,"Duration", l)
    res.to_csv(csvresult, index= False)
    
    