import numpy as np
#load non-zero position on each new basis ket
#newket=[65536,192] int
newket = np.load("newket2.npy")
# load phases
#phase[65536,192] complex
phase = np.load("newphase.npy")
# find out the rotation on local axis
effect_op2 = np.loadtxt("effect_op2.tsv", dtype=int)
g1 = np.load("g1.npy")#1
g2 = np.load("g2.npy")#1
g3 = np.load("g3.npy")#2
g4 = np.load("g4.npy")#3
g5 = np.load("g5.npy")#3
g6 = np.load("g6.npy")#1
g7 = np.load("g7.npy")#1
g8 = np.load("g8.npy")#2
g9 = np.load("g9.npy")#3
g10 = np.load("g10.npy")#3
x1 = np.load("x1.npy")#6
x2 = np.load("x2.npy")#6
x3 = np.load("x3.npy")#6
x4 = np.load("x4.npy")#6
char=np.zeros((44,192),dtype=complex)
for i in range(0,192):
    char[0][i]=g1[i][0]
    char[1][i]=g2[i][0]
    for j in range(0,2):
        char[j+2][i]=g3[i][j][j]
    for j in range(0,3):
        char[j+4][i]=g4[i][j][j]
    for j in range(0,3):
        char[j+7][i]=g5[i][j][j]
    char[10][i]=g6[i][0]
    char[11][i]=g7[i][0] 
    for j in range(0,2):
        char[j+12][i]=g8[i][j][j]
    for j in range(0,3):
        char[j+14][i]=g9[i][j][j]
    for j in range(0,3):
        char[j+17][i]=g10[i][j][j]
    for j in range(0,6):
        char[j+20][i]=x1[i][j][j]
    for j in range(0,6):
        char[j+26][i]=x2[i][j][j]
    for j in range(0,6):
         char[j+32][i]=x3[i][j][j]
    for j in range(0,6):
        char[j+38][i]=x4[i][j][j]
### char[2] and 2
nvalue=np.zeros((65536),dtype=int)
# nplace define different positions of 192 new kets
nplace=np.zeros((192),dtype=int)
#uplace=np.zeros((192),dtype=int)
count=np.zeros((44),dtype=int)
length=np.zeros((192),dtype=float)
# symvec is the multiplication result of character table and new kets
symvec=np.zeros((44,65536),dtype=complex)
temp=np.zeros((44,65536),dtype=complex)
check=np.zeros((65536),dtype=complex)
# u_position defines different positions in each row in u matrix
# u_element defines the values of different positions in each row in u matrix
u_position=np.zeros((65536,192),dtype=int)
u_element=np.zeros((65536,192),dtype=complex)
# count defines the size of blocks
#11233112336666
count=np.zeros((45),dtype=int)
count[0]=0
count[1]=count[0]+383
count[2]=count[1]+371
for i in range (0,2):
    count[i+3]=count[i+2]+774
for i in range(0,3):
    count[i+5]=count[i+4]+1081
for i in range(0,3):
    count[i+8]=count[i+7]+1085
count[11]=count[10]+335
count[12]=count[11]+335
for i in range (0,2):
    count[i+13]=count[i+12]+682
for i in range(0,3):
    count[i+15]=count[i+14]+957
for i in range(0,3):
    count[i+18]=count[i+17]+957
for i in range(0,6):
    count[i+21]=count[i+20]+2038
for i in range(0,6):
    count[i+27]=count[i+26]+2042
for i in range(0,6):
    count[i+33]=count[i+32]+2038
for i in range(0,6):
    count[i+39]=count[i+38]+2042

for i in range (32768,32769):
    if (nvalue[i]==0):
#        print(i)
        # define vec(192,65536) with different position in 65536
        vec=np.zeros((65536,192),dtype=complex)
        for j in range(0,192):
# newket[i][j] stores all 192 positions of 65536 original kets
            nplace[j]=newket[i][j]
        uplace = np.unique(nplace)
        print(uplace)

        length=np.zeros((44),dtype=float)

        for k in range (0,len(uplace)):
#            print(uplace[k])
#            nvalue[uplace[k]-1]=1
            for j in range (0,192):
                if (newket[i][j]==uplace[k]):
#                    print('k',k)
#                    print('j',j)
                    vec[uplace[k]-1][j]+=phase[i][j]
#        print(char[2])
        print(vec[32767])
        count=0
        for j in range(0,192):
            check=char[2][j]*vec[1][j]
            if(check!=0):
                print('j',j,'char',char[2][j],'vec[2][j]',vec[1][j],'check',check)
            if (vec[1][j]!=0):
                count=count+1
        print('count',count)
        check=0
        check=char[2].dot(vec[1])
        check=np.linalg.norm(check)
        print('check',check)


#        print('m',m)
        del vec
   


nvalue=np.zeros((65536),dtype=int)
# nplace define different positions of 192 new kets
nplace=np.zeros((192),dtype=int)
#uplace=np.zeros((192),dtype=int)
count=np.zeros((44),dtype=int)
length=np.zeros((192),dtype=float)
# symvec is the multiplication result of character table and new kets
symvec=np.zeros((44,65536),dtype=complex)
temp=np.zeros((44,65536),dtype=complex)
check=np.zeros((65536),dtype=complex)
# u_position defines different positions in each row in u matrix
# u_element defines the values of different positions in each row in u matrix
u_position=np.zeros((65536,192),dtype=int)
u_element=np.zeros((65536,192),dtype=complex)
# count defines the size of blocks
#11233112336666
count=np.zeros((45),dtype=int)
count[0]=0
count[1]=count[0]+383
count[2]=count[1]+371
for i in range (0,2):
    count[i+3]=count[i+2]+774
for i in range(0,3):
    count[i+5]=count[i+4]+1081
for i in range(0,3):
    count[i+8]=count[i+7]+1085
count[11]=count[10]+335
count[12]=count[11]+335
for i in range (0,2):
    count[i+13]=count[i+12]+682
for i in range(0,3):
    count[i+15]=count[i+14]+957
for i in range(0,3):
    count[i+18]=count[i+17]+957
for i in range(0,6):
    count[i+21]=count[i+20]+2038
for i in range(0,6):
    count[i+27]=count[i+26]+2042
for i in range(0,6):
    count[i+33]=count[i+32]+2038
for i in range(0,6):
    count[i+39]=count[i+38]+2042

for i in range (32767,32768):
    if (nvalue[i]==0):
#        print(i)
        # define vec(192,65536) with different position in 65536
        vec=np.zeros((65536,192),dtype=complex)
        for j in range(0,192):
# newket[i][j] stores all 192 positions of 65536 original kets
            nplace[j]=newket[i][j]
        uplace = np.unique(nplace)
        print(uplace)
#        print(uplace)

#        print(nplace[:])
#        print(nplace[:])

 #       print(i)
 #       for i in range (0,65536):
 #           if (nvalue[i]!=0):
 #               print(i)
            
        length=np.zeros((44),dtype=float)
#        print(char[0])
#        print(vec[0])
#        print(vec[65535])
#        ele=0
#        for j in range(0,192):
#            ele=char[0][j]*vec[0][j]+ele
#        print('ele',ele)

#        print(i)
#        for n in range(0,45):
#            print(count[n])
#        p=len(uplace)
        for k in range (0,len(uplace)):
#            print(uplace[k])
#            nvalue[uplace[k]-1]=1
            for j in range (0,192):
                if (newket[i][j]==uplace[k]):
#                    print(j)
                    vec[uplace[k]-1][j]+=phase[i][j]
#        print(char[2])
#        print(vec[1])

        for k in range (0,len(uplace)):
#            print(uplace[k])
#            nvalue[uplace[k]-1]=1
            for j in range (0,192):
                if (newket[i][j]==uplace[k]):
#                    print(j)
                    vec[uplace[k]-1][j]+=phase[i][j]
            m=0
#            check=0
            for l in range(0,44):
#                check=char[l].dot(vec[uplace[k]-1]) 
#                check=char[l].dot(vec[uplace[k]-1]) 
                check=0
                for j in range(0,192):
                    check=char[l][j]*vec[uplace[k]-1][j]+check
                length[l]=np.linalg.norm(check)
#                print('uplace[k]-1',uplace[k]-1)
#                print(char[3])
#                print(vec[uplace[k]-1])
#                print('i',i,'l',l,'k',k)
#                print('i',i,'l',l,'length',length[l])
                if (length[l]>0.000001):
                    print('i',i,'l',l,'k',k,'uplace',uplace[k])
                    m=m+1
                    nvalue[uplace[k]-1]=1 
            print('how many blocks', m)
            print('uplace[k]',uplace[k],'m',m)
        m=0
        for n in range(0,65536):
            if (nvalue[n]!=0):
                m=m+1
#                print('n',n)
        print('# of flag',m)
        m=0
        for l in range(0,44):
            check=np.zeros((65536),dtype=complex)
            for n in range(0,65536):
                check[n]=char[l].dot(vec[n]) 
            length[l]=np.linalg.norm(check)
#            print('i',i,'l',l)
#            print('i',i,'l',l,'length',length[l])
            
            if (length[l]>0.0000001):
#                    print(uplace[k])
#                print('i',i,'l',l,'length',length[l])
                m=m+1

#                if (m<len(uplace)):
#                    nvalue[uplace[p]-1]=1
        print('# of nonzero',m)
        for l in range(0,44):
#            temp=np.zeros((44,65536),dtype=complex)
            for n in range(0,65536):    
                temp[l][n]=char[l].dot(vec[n]) 
            length[l]=np.linalg.norm(temp[l])
            if (length[l]>0.000001):
                temp[l]=temp[l]/length[l]
                count[l]=count[l]+1                                   
                if (count[l]>65536):
                    print('i',i,'l',l,'k',k)
                    print('count',count[l])
#                    if (temp!=0):                        
#                    print('count',count[l])
#                        print(n,temp[n])
                m=0
                for n in range(0,65536):
                    if (temp[l][n]!=0):                        
                        u_position[count[l]-1][m]=n+1
                        u_element[count[l]-1][m]=temp[l][n]
                        m=m+1
#                print(u_position[count[l]])
#                    for n in range(0,65536):

            
#        print('m',m)
        del vec
   



