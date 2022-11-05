% NEWTON
%
function yint = interpola_newton(x,y,xint)
% 
% 
a = zeros(3,3);
b = zeros(3,1);
yaux = zeros(3,1);
%
a(:,1) = 1;
a(2,2) = x(2) - x(1);
a(3,2) = x(3) - x(1);
a(4,2) = x(4) - x(1);
a(3,3) = a(3,2)*(x(3) - x(2));
%a(4,3) = a(4,2)*(x(4) - x(2));
%
%a(4,4) = a(4,3)*(x(4) - x(3));
%
b(:) = y(:);
yaux = a\b;
%
n1 = xint - x(1);
n2 = n1*(xint - x(2));
n3 = n2*(xint - x(3));
%n4 = n3*(xint - x(4));
%
sol = yaux(1)+n1*yaux(2)+n2*yaux(3)%+n3*yaux(4);
yint = sol;
%
endfunction