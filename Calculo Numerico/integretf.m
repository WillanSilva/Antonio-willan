function integretf
%
% INTEGRA��O - M�TODO DOS RET�NGULOS
%
format long
disp('Digite o intervalo de integra��o - [a,b]')
a = input('Limite inferior - ');
b = input('Limite superior - ');
n = input('N�mero de subintervalos - ');
%
h = (b - a)/n;
%
for i=1:n
xa(i) = a + (i - 1)*h;
xa(i+1) = a + i*h;
x(i) = (xa(i)+xa(i+1))/2;
[f(i)] = fint(x(i)); 
end
%
soma = 0;
%
for i=1:n;
soma = soma + f(i)*h;
end
printf('O resultado da integral � %d \n', soma)
end
%
% FUN��O A SER INTEGRADDA
%
function [f] = fint(x)
f = x * log(x);
end
