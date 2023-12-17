clear;
clc;
fprintf('\n  Recherche la racine de la fonction f sur [a,b] par les diff�rentes m�thodes: \n\n ');

a=input('- Donner la valeur de la borne inf: a=');
b=input(' - Donner la valeur de la borne sup: b=');
x0=input(' - Donner la valeur initiale: x0=');
epsilon=input(' - Entrer la valeur de la tolerence: epsilon=');
n_max=input(' - Entrer le nombre maximal d''it�rations: n_max=');

fprintf('\n Les r�sultats obtenus par la m�thode de dichotomie: \n\n ');
fprintf(' - La racine de f obtenue par cette m�thode: alpha = %.10f\n\n', bissection(a,b,epsilon,n_max));
fprintf('\n Les r�sultats obtenus par la m�thode du poit fixe: \n\n ');
fprintf(' - La racine de f obtenue par cette m�thode: alpha = %.10f \n\n', pointfix(x0,epsilon,n_max));
fprintf('\n Les r�sultats obtenus par la m�thode de Newton: \n\n ');
fprintf(' - La racine de f obtenue par cette m�thode: alpha = %.10f \n\n', newton(x0,n_max,epsilon));


