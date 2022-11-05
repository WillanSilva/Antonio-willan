function simp38 
format long
disp('Digite o intervalo de integração - [a,b]')
a = input('Limite inferior - ');
b = input('Limite superior - ');
n = input('Número de blocos (cada um com 4 pontos) - ');
h = (b-a)/(3*n); 
x = a:h:b;
soma = 0;
for i = 1:n 
v1 = fint(x(3*i-2));
v2 = fint(x(3*i-1));
v3 = fint(x(3*i));
v4 = fint(x(3*i+1));
soma = soma + v1 + 3*v2 + 3*v3 + v4; 
endfor
int = (3*h/8)*soma 
endfunction
%
% FUNÇÃO A SER INTEGRADDA
%
function [f] = fint(x)
  if(x==1)
  f=0.974;
  endif
 if(x==2)
  f=0.936;
 endif
 if(x==3)
  f=0.882;
 endif
 if(x==4)
  f=0.814;
 endif
 if(x==5)
  f=0.732;
 endif
 if(x==6)
  f=0.637;
 endif
 if(x==7)
  f=0.532;
 endif
 %só trocar a função!
end