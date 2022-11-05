function [ints38] = integsimp38(x,y)
% 
x = x(:);
y = y(:);
%
n = length(x);
%
xa = x(1);
xb = x(n);
%
ya = y(1);
yb = y(n);
%
dx = (xb - xa)/(n - 1);
%
n1 = (n - 1)/3;
n2 = (n - 1)/3;
n3 = (n - 4)/3;
y1 = 0;
y2 = 0;
y3 = 0;
%
for j=1:n1
jj = 3*j - 1;
y1 = y1 + y(jj);
end
y1 = 3*y1;
%
for k=1:n2
kk = 3*k;
y2 = y2 + y(kk);
end
y2 = 3*y2;
%
for i=1:n3
ii = 3*i + 1;
y3 = y3 + y(ii);
end
y3 = 2*y3;
%
ints38 = (ya + yb + y1 + y2 + y3)*3*dx/8
%
endfunction
%