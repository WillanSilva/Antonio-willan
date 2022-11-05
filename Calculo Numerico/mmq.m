% MÉTODO DOS MÍNIMOS QUADRADOS - REGRESSÃO LINEAR
%
function [coef] = mmq(x,y)
%
% DADOS DE ENTRADA (TABELA) --> 'x' e 'y'
% 
% y = a(1) + a(2) *x -- > sol(1) e sol(2)
% n - número de pontos da tabela
%
n = length(x)
a = zeros(3,3);
b = zeros(3,1);
sol = zeros(3,1);
som11=0;
som12=0;
som13=0;
som21=0;
som22=0;
som23=0;
som31=0;som32=0;
som33=0;
som1f=0;
som2f=0;
som3f=0;
x(1)
%g1(x)=log(x) x^2, g2(x)=cos(x)  x , g3(x)=exp(x) 1;
cont=1;
while (cont<=7)
  som11= som11 + x(cont)^2*2;
  som12= som12 + x(cont)^2*x(cont);
  som21=som12;
  som13=som13 + (x(cont)^2);
  som31=som13;
  som22=som22+x(cont);
  som23= som23 + x(cont);
  som32=som23;
  som33= som33+1;
  som1f=som1f + x(cont)^2*y(cont);
  som2f=som2f + x(cont)*y(cont);
  som3f=som3f + y(cont);
  cont+=1
endwhile
som11=som11
a(1,1)=som11;
a(1,2)=som12;
a(1,3)=som13;
a(2,1)=som21;
a(2,2)=som22;
a(2,3)=som23;
a(3,1)=som31;
a(3,2)=som32;
a(3,3)=som33;
b(1)=som1f;
b(2)=som2f;
b(3)=som3f;
a=a
b=b
sol=a\b;
res=zeros(3,1);
res(1)=-1.135816;
res(2)=-1.298939;
res(3)=0.036826;
coef=sol;
% xaj - 'x' em que se deseja determinar a imagem
% yaj - 'y' obtido pelo ajuste linear
endfunction
