%This section is to determine the number of class and prior of a class
% from a given vector Developed by Dr. Mohendra Roy
clc, clear all
x=[1,1,1,1,2,2,2,2];
xx=x;

N=0;

for i=1:length(x)
    
    if sum(x) ~=0 && x(i) ~=0
        N=N+1; % Total number of classes 
        y=x./x(i);
        
        
        z=find(y==1);
        c(N)=length(z)/length(x);
        M(N)=x(i);
        x(z)=0;
               
    end
       
end
clsss=M;
prior=c;

%End of the class determination 


% This section will deal with the Frequency of the substances. 

y=[6,180,12; 5.92,190,11; 5.58,170,12; 5.92,165,10;5,100,6;5.5,150,8;5.42,130,7;5.75,150,9 ];
AA=[];
BB=[];


for i=1:length(y(1,:))
     
    yy=y(:,i);
    
    for j=1:length(clsss)
       
      n=clsss(j);
    
       zz=find(xx==n);
       
       tt=yy(zz);
       
       AA(j,i)=mean(tt);
       BB(j,i)=std(tt);
       

              
    end

    
end

%AA=AA+1;
%BB=BB+1;
% code for test 

tes=[6,180,10];
%Postp=1;
posp=[];
po=[];

for i=1:length(clsss)
    Men1=AA(i,:);
    Sten1=BB(i,:);
    
    for j=1:length(Men1)
        
        gpdf=normpdf(  tes(j),Men1(j),Sten1(j) );
        posp(j)=gpdf
        
    end
    
   po(i)=prod(posp)*prior(i);
    
end
summm=sum(po);
 pospk= po/summm;
hari=find([pospk==max(pospk)])

ommm=clsss(hari)
