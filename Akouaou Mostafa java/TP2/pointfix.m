function alpha = pointfix(x0,epsilon,n_max)

tic
n_iter=0;
x=g(x0);
        
while(abs(x-x0)>epsilon && n_iter<n_max)        
x0=x;
x=g(x0);
n_iter=n_iter+1;
alpha=x;

end

t=toc;
%fprintf(' - La racine de f par la méthode du point fixe  est: alpha = %f \n', alpha);
fprintf('- Le nombre d''itérations nécessaires: n = %i \n',n_iter);
fprintf(' - Le temps nécessaire pour l''exécution: time = %f \n',t);

