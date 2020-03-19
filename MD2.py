#!/usr/bin/env python
# coding: utf-8

# In[22]:


string=input() #THIS STING SAVES THE INPUT 
string=string.replace('"','') #ERASE THE "" FROM THE MSG IF NECESSARY 
array=[] #THIS ARRAY HELPS TO DO THE PADDING STEP
msg=[] #LIST THAT HAS THE INPUT

###PADDING####
if(len(string)>16):
    for i in range(0,len(string)):
        array.append(ord(string[i]))# GETTING THE ASCII VALUE AND SAVING IT IN ARRAY
        if(len(array)==16): #MAKING SURE THE ARRAY IS A BLOCK OF 16-B            
            msg.extend(array) #SAVING THE ASCII ARRAY INTO MSG 
            array=[] #"RESTARTING" THE BLOCK TO 0 
            
        if(len(array)>0 and i==(len(string)-1)): #IF WE GET TO THE END OF THE INPUT STRING AN WE HAVE AN INCOMPLETE 16-B BLOCK 
            if((len(array)%16!=0)): 
                aux=16-len(array) #AUX HAS THE VALUE THAT THE BLOCK NEEDS TO PAD INORDER TO BE 16-B 
            while((len(array)%16!=0)): #WHILE OUR BLOCK IS STILL INCOMPLETE AUX IS GOING TO BE ADDED TO OUR ARRAY  
                array.append(aux)
    msg.extend(array)#ADDING THE BLOCKS TO MSG 
else: #THIS IS FOR INPUTS OF < 16-B, IT HAS THE SAME LOGIC FROM THE CODE RIGHT ABOVE 
    for i in range(0,len(string)):
        
        msg.append(ord(string[i]))
    while((len(msg)%16!=0)):
        msg.append(16-len(string))
    if(len(string)==0):
        for i in range(0,16):
            msg.append(16)

S = [ 41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6,
     19, 98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188,
     76, 130, 202, 30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24,
     138, 23, 229, 18, 190, 78, 196, 214, 218, 158, 222, 73, 160, 251,
     245, 142, 187, 47, 238, 122, 169, 104, 121, 145, 21, 178, 7, 63,
     148, 194, 16, 137, 11, 34, 95, 33, 128, 127, 93, 154, 90, 144, 50,
            39, 53, 62, 204, 231, 191, 247, 151, 3, 255, 25, 48, 179, 72, 165,
            181, 209, 215, 94, 146, 42, 172, 86, 170, 198, 79, 184, 56, 210,
            150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241, 69, 157,
            112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2, 27,
            96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
            85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197,
            234, 38, 44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65,
            129, 77, 82, 106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123,
            8, 12, 189, 177, 74, 120, 136, 149, 139, 227, 99, 232, 109, 233,
            203, 213, 254, 59, 0, 29, 57, 242, 239, 183, 14, 102, 88, 208, 228,
            166, 119, 114, 248, 235, 117, 75, 10, 49, 68, 80, 180, 143, 237,
            31, 26, 219, 153, 141, 51, 159, 17, 131, 20

]


C=[0] * 16
L=0
X=[0] * 48

####CHECKSUM#####
for i in range(0,int(len(msg)/16)):
    for j in range(0,16):
        c=msg[16*i+j]
        C[j]=C[j]^S[c^L]
        L=C[j]
        
for a in range(0,len(C)):
    msg.append(C[a]) #ADDING THE 16-B CHECKSUM  TO THE MSG

#####THE HASH ######
for i in range (0,int(len(msg)/16)):
    for j in range(0,16):
        X[j+16]=msg[16*i+j]
        X[j+32]=X[j+16]^X[j]
    t=0
    for j in range(0,18):
        for k in range(0,48):
            t=X[k]^S[t]
            X[k]=t
        t=(t+j)%256
        
hash=""
for i in range(0,16):
    hash=hash+format(X[i], '02x')
print(hash)

