function alpha= bissection(a,b,epsilon,n_max)
tic;
x=(a+b)/2;
n_iter=0;
while(abs(b-a)>epsilon && n_iter<n_max)
    x=(a+b)/2;
    n_iter=n_iter+1;
    if(f(a)*f(x)>0)
        a=x;
    elseif(f(a)*f(x)<0)
        b=x;
    else
        x=(a+b)/2;
        break
    end 
end
alpha=x;

t=toc;
%fprintf('- La racine de f par la m�thode de dichotomie est: alpha = %f \n', alpha);
fprintf('- Le nombre d''it�rations n�cessaires: n = %i \n',n_iter);
fprintf(' - Le temps n�cessaire pour l''ex�cution: time = %f \n',t);

