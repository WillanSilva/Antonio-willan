function simp13 
disp('Digite o intervalo de integração - [a,b]')
a = input('Limite inferior - ');
b = input('Limite superior - ');
%7 numero de blocos!
n=7;
x=[0.33,0.46,0.59,0.72,0.85,0.98,1.11]
y=[0.946,0.896,0.831,0.752,0.66,0.557,0.445]
h = (x(7)-x(1))/(n); 
x0 = a;
x1 = x0 + h
x2 = x1 + h
x3 = x2 + h
x4 = x3 + h
x5 = x4 + h
%x6=x5+h
%x7=x6+h
%x8=x7+h
%x9=x8+h;
%x10=x9+h %só trocar aqui
soma1=0.946+0.445;
soma2=0.896+0.752+0.557;
soma3 = 0.831+0.66;
resp=(h/3)*(soma1 + 4*soma2 + 2*soma3)
endfunction