function [c n info]=newtonsimplesdemais(f,fl,x0,tol)
info=0;
n=0;
c= Inf;
error = Inf;
while (error > tol)
c = x0 - f(x0)/fl(x0);
error = abs(f(c))
x0=c
n=n+1
endwhile
info=1;
endfunction
format long
f=@(x) x^5+x^4-3.3
fl=@(x) 5*x^4+4*x^3
x0=1.1173
%x0=10
% f=@(x) x^3-5*x
% fl=@(x) 3*x^2-5
% x0=1
tol=10^-8
%tol=10^-14
[c n info]=newtonsimplesdemais(f,fl,x0,tol)
