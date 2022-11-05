function [sol info res err] = triang_inferior(a,b,exa)
  bi=b;
  [m n] = size(a);
  if(m!=n)
    info=2;
    prinf('A matriz a não é quadrada!');
    sol=inf;
    res=inf;
    err=inf;
    return
   endif
   if(n!=size(b,1))
      display('As Dimesões de a e b não se correlacionam!')
      info=3;
      sol=inf;
      res=inf;
      err=inf;
      return
   endif
  %fiz somente um for para verificar se possui um 0 na diagonal
  for n=1:m
    if(a(n,n)==0)
        display('Possui um 0 na diagonal!')
        info=4;
        sol=inf;
        res=inf;
        err=inf;
        return
      endif
  endfor
  sol = zeros(n,1);
  sol(1) = b(1)/a(1,1);
  for k = 2:m
      b(k:m)=b(k:m)-a(k:m,k-1)*sol(k-1);
      sol(k)=b(k)/a(k,k);
  endfor
  res=norm(a*sol-bi);
  info = 1;
  err=(sol-exa);
endfunction