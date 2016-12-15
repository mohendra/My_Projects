import math
import numpy as np
x=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
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
I=[[3.567,3.52,3.117,2.813],[3.569,3.53,3.118,2.812],[3.568,3.54,3.119,2.814],[2.70,2.936,2.856,2.782],[2.71,2.937,2.857,2.783],[2.72,2.938,2.858,2.784],[2.72,1.575,1.93,1.032],[2.73,1.578,1.932,1.033],[2.74,1.58,1.935,1.039],[2.71,2.3,1,1.35],[2.715,2.35,1.6,1.41],[2.78,2.4,1.7,1.5],[2.9,2.6,1.8,1.5],[2.95,2.62,1.83,1.57],[3,2.7,1.9,1.6]]
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


#code for test
#tes=[3,2.7,1.9,1.6]
print "input the text d values "
tes = [float(x) for x in raw_input().split()]
tesl=len(tes)
posp=np.zeros(tesl)
po=np.zeros((NClss))
summm=po
pospk=po
import scipy.stats as sp
for i in range(0,len(clsss)):
    men1=AA[i,:]
    sten1=BB[i,:]
    for j in range(0,len(men1)):
        gdpdf=sp.norm(men1[j],sten1[j]).pdf(tes[j])

        posp[j]=gdpdf
    po[i]=np.prod(posp)*prior[i]
potest=np.sum(posp)

if potest>0:
    summm[i]=sum(po)
    pospk[i]=np.divide(po[i],summm[i])
#if sum(pospk)>=0:
    maxxx=np.where(pospk==max(pospk))
    maxxx=maxxx[0]
    summax=sum(maxxx)
    result=clsss[maxxx]
    print "The Tentetive material is %d"%result
else:
    print ('No material exist with this D value')
