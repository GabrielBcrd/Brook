from base64 import encode
from encodings import utf_8
import string
import numpy as np
import pandas as pd

#frequence de référence
freqReference = 440
nb_octave_sup =12
nb_octave_inf = 5
freq = freqReference

noteslist = ['A#','B','C','C#','D','D#','E','F','F#','G','G#','A']
noteslistFr = ['la#','si','do','do#','ré','ré#','mi','fa','fa#','sol','sol#','la']
arr = ["","","","",""]
list = ["Note","Note_FR","octave","freq","color_notes"]


#--------------------------------------------------Process all frequency and parameters of note 

for i in range(nb_octave_inf-1,-1,-1):
    for j in range(len(noteslist)):
        note = noteslistFr[::-1][j]
        if "#" in note:
            color_note = "black_note"
        else:
            color_note = "white_note"
            
        arr = np.vstack((arr,np.array([noteslist[::-1][j]+str(i),note+str(i),i,freq,color_note])))
        freq = freq * 2 ** -(1/12)
         
freq = freqReference

for i in range(nb_octave_inf,nb_octave_sup-1): 
    for j in range(len(noteslist)):
        freq = freq * 2 ** (1/12)

        note = noteslistFr[j]
        if "#" in note:
            color_note = "black_note"
        else:
            color_note = "white_note"

        arr = np.vstack((arr,
                        np.array([noteslist[j]+str(i),note+str(i),i,freq,color_note])
                        ))
        
        
#------------------------------------------------write as csv

DF = pd.DataFrame(arr)
DF.columns = list

DF = DF.iloc[1:]
DF['freq'] = DF['freq'].astype(float)
DF = DF.sort_values(by=['freq'], ascending=True)

DF.to_csv("array_notes_frequency.csv",sep = ",",index=False,header=list)



