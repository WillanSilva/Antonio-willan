% MÉTODO DOS MÍNIMOS QUADRADOS - REGRESSÃO LINEAR
%
function [coef] = mmq(x,y)
%
% DADOS DE ENTRADA (TABELA) --> 'x' e 'y'
% 
% y = a(1) + a(2) *x -- > sol(1) e sol(2)
% n - número de pontos da tabela
%
x = [0.3 0.7 1.2 2 2.3 3 3.9 4.1 4.6 5.2 6.0 6.1];
y = [4.062 4.006 3.983 3.684 3.711 3.339 1.879 2.760 2.208 
1.792 1.504 1.808];
n = length(x);
a = zeros(3,3);
b = zeros(3);
sol = zeros(3);
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
for i=0:n
  som11+=log(x(n))*log(x(n))
  som12+=log(x(n))*cos(x(n));
  som21=som12;
  som13+=log(x(n))*exp(x(n));
  som31=som13;
  som22+=cos(x(n))*cos(x(n));
  som23+=cos(x(n))*exp(x(n));
  som32=som23;
  som33+=exp(x(n))*exp(x(n));
  som1f+=log(x(n))*y(n);
  som2f+=cos(x(n))*y(n);
  som3f+=exp(x(n))*y(n);
endfor
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
sol=a/b;
% xaj - 'x' em que se deseja determinar a imagem
% yaj - 'y' obtido pelo ajuste linear
xa = 6.8;
% 
x = x(:);
y = y(:);
%
a(1,1) = n;
a(1,2) = sum(x);;
a(2,1) = a(1,2);
a(2,2) = x’*x;
%
b(1) = sum(y);
b(2) = x'*y;
%
sol = a\b;
ya = sol(1)+sol(2)*xa
endfunction
