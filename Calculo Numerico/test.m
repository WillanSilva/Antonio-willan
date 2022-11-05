% MÉTODO DOS MÍNIMOS QUADRADOS - REGRESSÃO LINEAR
%
function [coef] = test(x,y)
%
% DADOS DE ENTRADA (TABELA) --> 'x' e 'y'
% 
% y = a(1) + a(2) *x -- > sol(1) e sol(2)
% n - número de pontos da tabela

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
%g1(x)=log(x), g2(x)=cos(x) , g3(x)=exp(x);
cont=1;
som11=log(x(1))^2 + log(x(2))^2+log(x(3))^2 + log(x(4))^2 ...
 + log(x(5))^2 + log(x(6))^2 + log(x(7))^2 + log(x(8))^2 + log(x(9))^2 + log(x(10))^2;
som12=log(x(1))*cos(x(1))+log(x(2))*cos(x(2))+log(x(3))*cos(x(3))+log(x(4))*cos(x(4))+log(x(5))*cos(x(5))...
+log(x(6))*cos(x(6))+log(x(7))*cos(x(7))+log(x(8))*cos(x(8))+log(x(9))*cos(x(9))+log(x(10))*cos(x(10));
som21=som12;
som13=log(x(1))*exp(x(1))+log(x(2))*exp(x(2))+log(x(3))*exp(x(3))+log(x(4))*exp(x(4))+log(x(5))*exp(x(5))...
+log(x(6))*exp(x(6))+log(x(7))*exp(x(7))+log(x(8))*exp(x(8))+log(x(9))*exp(x(9))+log(x(10))*exp(x(10));
som31=som13;
som22=cos(x(1))^2+cos(x(2))^2+cos(x(3))^2+cos(x(4))^2+cos(x(5))^2+cos(x(6))^2+cos(x(7))^2 ...
+cos(x(8))^2+cos(x(9))^2+cos(x(10))^2;
som23=cos(x(1))*exp(x(1))+cos(x(2))*exp(x(2))+cos(x(3))*exp(x(3))+cos(x(4))*exp(x(4))+...
cos(x(5))*exp(x(5))+cos(x(6))*exp(x(6))+cos(x(7))*exp(x(7))+cos(x(8))*exp(x(8))+cos(x(9))*exp(x(9))+cos(x(10))*exp(x(10));
som32=som23;
som33=exp(x(1))^2+exp(x(2))^2+exp(x(3))^2+exp(x(4))^2+exp(x(5))^2+exp(x(6))^2+exp(x(7))^2+...
exp(x(8))^2+exp(x(9))^2+exp(x(10))^2;
som1f=log(x(1))*y(1)+log(x(2))*y(2) +log(x(3))*y(3) +log(x(4))*y(4) +log(x(5))*y(5) +log(x(6))*y(6) +...
log(x(7))*y(7) +log(x(8))*y(8) +log(x(9))*y(9)+log(x(10))*y(10);
som2f=cos(x(1))*y(1)+cos(x(2))*y(2)+cos(x(3))*y(3)+cos(x(4))*y(4)+cos(x(5))*y(5)+cos(x(6))*y(6)+...
cos(x(7))*y(7)+cos(x(8))*y(8)+cos(x(9))*y(9)+cos(x(10))*y(10);
som3f=exp(x(1))*y(1)+exp(x(2))*y(2)+exp(x(3))*y(3)+exp(x(4))*y(4)+exp(x(5))*y(5)+exp(x(6))*y(6)+...
exp(x(7))*y(7)+exp(x(8))*y(8)+exp(x(9))*y(9)+exp(x(10))*y(10);
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
coef=sol;
% xaj - 'x' em que se deseja determinar a imagem
% yaj - 'y' obtido pelo ajuste linear
endfunction
