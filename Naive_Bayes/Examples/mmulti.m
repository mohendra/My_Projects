
%% This is the 1st matrix,, Mohendra roy
clear all;
clc;
m=input('Input the number of Row of 1st matrix = ')
n=input('Input the number of coulomb of 1st matrix = ')

x=[];

for i=1:m
    for j=1:n
        
        
        display(['input the ', num2str(i), '  row   &  ', num2str(j), '  coulomb of 1st Matrix ']);
        x(i,j)=input('X=');
        
        
        
    end
end
 disp('The First Matrix  =  ')
 disp(x)

%% End of the 1st matrix

%% This is the 2nd Matrix


p=input('Input the number of Row of 2nd matrix = ')
q=input('Input the number of coulomb of 2nd matrix = ')

y=[];

for i=1:p
    for j=1:q
        
        
        display(['input the ', num2str(i), '  row   &  ', num2str(j), '  coulomb of 2nd Matrix']);
        y(i,j)=input('y=');
        
        
        
    end
end
 %% End of the 2nd matrix
 
 disp('The 2nd Matrix  =  ')
 disp(y)
 
 %% Matrix multiplication
 z=0;
 j=0;
 for i=1: m
     for j=1:q
        

         for k=1:p


             z=z+(x(i,k)*y(k,j));
           
         end
             
         fi(i,j)=z;
         z=0;
         
  
     end
     
 end
Prodct=fi;
  disp('product of the matrix is  ');
  disp(Prodct)