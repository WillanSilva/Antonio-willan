 function [c n info]=secantesimplesdemais(f,x0,x1,tol)
info=0;
n=0;
c= Inf;
error = Inf;
while (error > tol)
c = x1 - f(x1)*(x0-x1)/(f(x0)-f(x1));
error = abs(f(c))
x0=x1
x1=c
n=n+1
endwhile
info=1;
endfunction
tol=10^-6
f=@(x) x^5+x^4-3.3 % polinômio com apenas uma raiz real e 4 complexas
x0=1.1173,x1=1.1174 % convergência rápida
%x1=1.1173,x0=1.1174 % convergência rápida com troca de ordem
%x0=2,x1=3 % convergência para uma raiz
%x0=3,x1=2 % convergência para mesma raiz mas com outra aproximação
%f=@(x)(x-2)^2-1 % polinômio com duas raizes reais
%x1=4;x0=3.5; % raiz 3
%x0=4;x1=3.5; % raiz 3 em outra ordem
%x1=0,x0=.5; % raiz 1
%x0=4,x1=0; % secante paralela
%x0=4,x1=0.5; % uma ordem, foi para 1
%x0=.5,x1=4 % outra ordem , foi para 3
[c n info]=secantesimplesdemais(f,x0,x1,tol)
