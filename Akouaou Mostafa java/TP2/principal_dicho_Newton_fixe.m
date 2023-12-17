clear;
clc;
fprintf('\n  Recherche la racine de la fonction f sur [a,b] par les différentes méthodes: \n\n ');

a=input('- Donner la valeur de la borne inf: a=');
b=input(' - Donner la valeur de la borne sup: b=');
x0=input(' - Donner la valeur initiale: x0=');
epsilon=input(' - Entrer la valeur de la tolerence: epsilon=');
n_max=input(' - Entrer le nombre maximal d''itérations: n_max=');

fprintf('\n Les résultats obtenus par la méthode de dichotomie: \n\n ');
fprintf(' - La racine de f obtenue par cette méthode: alpha = %.10f\n\n', bissection(a,b,epsilon,n_max));
fprintf('\n Les résultats obtenus par la méthode du poit fixe: \n\n ');
fprintf(' - La racine de f obtenue par cette méthode: alpha = %.10f \n\n', pointfix(x0,epsilon,n_max));
fprintf('\n Les résultats obtenus par la méthode de Newton: \n\n ');
fprintf(' - La racine de f obtenue par cette méthode: alpha = %.10f \n\n', newton(x0,n_max,epsilon));


