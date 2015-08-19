##It calculates ODE using Runge-Kutta 4th order method
##
def rk4(


h=1.5; # step size
x = range(0,3,h); # Calculates upto y(3)
y = zeros(1,length(x)); 
y(1) = 5;
F_xy = @(t,r) 3.*exp(-t)-0.4*r; #change the function as you desire

for i in range(0,(length(x)-1))   #calculation loop
    k_1 = F_xy(x(i),y(i));
    k_2 = F_xy(x(i)+0.5*h,y(i)+0.5*h*k_1);
    k_3 = F_xy((x(i)+0.5*h),(y(i)+0.5*h*k_2));
    k_4 = F_xy((x(i)+h),(y(i)+k_3*h));

    y(i+1) = y(i) + (1/6)*(k_1+2*k_2+2*k_3+k_4)*h;  #main equation
