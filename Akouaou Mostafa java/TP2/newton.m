function alpha= newton(x0,n_max,epsilon)
tic
n_iter=0;
x=x0-(f(x0)/df(x0));
while(abs(x-x0)>epsilon && n_iter<n_max)
   if(f(x)==0)
        alpha=x;
        break;
   elseif(df(x)==0)
       fprintf('la deriv�e est nulle');
        break;
   else
        x0=x;
        x=x-(f(x)/df(x));
        alpha=x;
   end    
n_iter=n_iter+1;

t=toc;
%fprintf(' - La racine de f par la m�thode de newton  est: alpha = %f \n', alpha);
fprintf('- Le nombre d''it�rations n�cessaires: n = %i\n',n_iter);
fprintf(' - Le temps n�cessaire pour l''ex�cution: time = %f \n',t);
end