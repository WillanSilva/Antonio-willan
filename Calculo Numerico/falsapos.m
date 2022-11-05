function [c n info]=falsapos(f,a,b,tol)
info=0
n=0
error = inf
while (error > tol)
c=(a*f(b)-b*f(a))/(f(b)-f(a));
if (f(a)*f(c)<0)
b=c
elseif (f(b)*f(c)<0)
a=c
else
n=n+1
break
endif
error=abs(f(c))
n=n+1
endwhile
info=1
endfunction
format long
f=@(x) x^5+x^4-3.3
a=1.1173
b=1.1174
tol=10^-6
[c n info]=falsapos(f,a,b,tol)
