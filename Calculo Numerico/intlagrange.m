%
% INTERPOLAÇÃO POR LAGRANGE
%
function yint = intlagrange(x,y,xint)
% 
% DADOS DA TABELA --> 'x' e 'y'
% 
%x = [-40 0 20 50];
%y = [1.52 1.29 1.20 1.09];
% 
% PONTO PARA INTERPOLAÇÃO --> 'xint' e 'yint'
% 
%xint = 15;
n = 4;
% 
s = 0;
for i = 1:n
L = 1;
% 
for j = 1:n
if i~=j
L = L*(xint - x(j))/(x(i) - x(j));
endif
endfor
% 
s = s + y(i)*L;
%
endfor
% 
yint = s;
% 
endfunction