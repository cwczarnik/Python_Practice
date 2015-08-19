import numpy as np

      
fwlist = ['cinema', 'host', 'aba', 'train']
swlist = ['iceman', 'shot', 'bab', 'rain']


def anagram(fw, sw):
    wordnum = 0
    while wordnum < len(fw):
        letterslist = []
        letterslist2 = []

        for i in fw[wordnum]:
            letterslist.append(i)
            
        letterslist.sort()
        
        for j in sw[wordnum]:
            letterslist2.append(j)
            
        letterslist2.sort()

        if letterslist == letterslist2:
            print 1
        else:
            print 0
        

        wordnum +=1

anagram(fwlist,swlist)



    
