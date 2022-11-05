function[ya] = mmqp2(x,y)
%
% DADOS DE ENTRADA (TABELA) --> 'x' e 'y'
% 
% y = a(1) + a(2) *x -- > sol(1) e sol(2)
% n - número de pontos da tabela
%
n = length(x);
a = zeros(2,2);
b = zeros(2);
sol = zeros(2);
%
% xaj - 'x' em que se deseja determinar a imagem
% yaj - 'y' obtido pelo ajuste linear
xa = 6;
% 
x = x(:);
y = y(:);
%
a(1,1) = n;
a(1,2) = sum(x);;
a(2,1) = a(1,2);
a(2,2) = x'*x;
%
b(1) = sum(x);
b(2) = x'*y;
%
sol = a\b;
ya = sol(1)+sol(2)*xa
endfunction