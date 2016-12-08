import math
import numpy as np
x=[1,1,1,2,2,2]
xx=x
xxx=(np.array(x)).astype(float)
N=0
c=[]
M=[]
for i in range (0,len(xxx)):
    p=np.sum(xxx)
    if p != 0 and xxx[i] !=0:
        N=N+1
        y=np.divide(xxx,xxx[i])

        z=np.where(y==1)
        zz=z[0]
        LZ=float(len(zz))
        LX=float(len(xxx))
        cc=np.divide(LZ,LX)
        c.append(cc)
        MM=x[i]
        M.append(MM)
        xxx[z]=0

clsss=M
prior=c

#second part for calculatind
import numpy as np
I=[[3.567,3.52,3.117,2.813],[3.569,3.53,3.118,2.812],[3.568,3.54,3.119,2.814],[2.70,2.936,2.856,2.782],[2.71,2.937,2.857,2.783],[2.72,2.938,2.858,2.784]]
y=np.array(I)
NClss=len(clsss)
Nrows=len(y[0,:])
AA=np.zeros((NClss,Nrows))
BB=np.zeros((NClss,Nrows))
xx=np.array(xx)
for i in range (0,len(y[0,:])):
    yy=y[:,i]

    for j in range (0,len(clsss)):
        n=clsss[j]
        zz=np.where(xx==n)
        zz=zz[0]

        tt=yy[zz]
        nnn=np.mean(tt)
        qqq=np.std(tt)
        AA[j,i]=nnn
        BB[j,i]=qqq

#code for test
tes=[0.0,2.0,0.856,0.782]
tesl=len(tes)
posp=np.zeros(tesl)
po=np.zeros((NClss))
Sum_posp=np.zeros((NClss))
men2=len(AA[1,:])
#prd=np.zeros((NClss))
prd=np.zeros((NClss,men2))
summm=po
pospk=po
import scipy.stats as sp
for i in range(0,len(clsss)):
    men1=AA[i,:]
    sten1=BB[i,:]
    for j in range(0,len(men1)):
        gdpdf=sp.norm(men1[j],sten1[j]).pdf(tes[j])

        posp[j]=gdpdf
    
    prd[i]=posp
    Sum_posp[i]=sum(prd[i])
    
    po[i]=np.prod(posp)*prior[i]
Sum_posp1=sum(Sum_posp) 
if Sum_posp1>0:
    summm[i]=sum(po)
    pospk[i]=np.divide(po[i],summm[i])
    maxxx=np.where(pospk==max(pospk))
    maxxx1=maxxx[0]
    result=clsss[maxxx1]
    print result
else: 
    print ('No such material')
