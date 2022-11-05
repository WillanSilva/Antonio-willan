
% INTEGRAÇÃO POR TRAPÉZIOS
%
function int = inttrap(x,y)
% 
format long
% DADOS DA TABELA --> 'x' e 'y'
% 
%formando a tabela -> (a-b)/n = intervalo em x
%
b=1;
a=0;
n=4;
h = (b-a)/(n); 
x0 = a;
x1 = x0 + h
x2 = x1 + h
x3 = x2 + h
x4 = x3 + h
%x5 = x4 + h
%x6=x5+h
%x7=x6+h
x=[x0,x1,x2,x3,x4]%x5,x6,x7];
f=@(x)-x^2+2*x+2;
y=[f(x0),f(x1),f(x2),f(x3),f(x4)]%,f(x5),f(x6),f(x7)];
n = length(x);
xa = x(1);
xb = x(n);
ya = y(1);
yb = y(n);
dx = (xb - xa)/(n - 1);
n1 = n - 1;
%
y1 = 0;
y2 = 0;
%
for j=2:n1
y1 = y1 + y(j);
end
y1 = 2*y1;
%
int = (ya + yb + y1)*dx/2;
%
endfunction