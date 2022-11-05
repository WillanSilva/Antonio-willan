function [sol info niter err]=bissecao(f,a,b,tol,maxiter,exa)
fa=f(a);
fb=f(b);
if (fa*fb>0)
        info=3;
        sol=inf;
        niter=0;
        err=inf;
        return
    endif
sol=(a*fb-b*fa)/(fb-fa);
fc=f(sol);
niter=1;
while ((abs(fc)> tol)&&(niter<maxiter))
    if (fc*fa>0)
        a=sol;
        fa=fc;
    else
        b=sol;
        fb=fc;
    endif
    sol=(a*fb-b*fa)/(fb-fa);
    fc=f(sol);
    niter=niter+1;
endwhile
 if ((f(a)==fc)|| (f(b)==fc))
    info=4;
    sol=fc;
    niter=0;
    err=0;
    return
endif
if((niter>=maxiter && (f(exa)!=0)||(abs(fc)>10^6)))
    info=2;
    sol=inf;
    niter=inf;
    err=inf;
    return
endif
if(abs(sol-exa)<=0||(fc<=0))
    info=1;
    sol=fc;
    err=abs(sol-exa);;
    return
endif
endfunction
