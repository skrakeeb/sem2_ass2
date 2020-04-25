/*
coded by: rakeeb 
coded for: Implementation of Euler method in c code
*/

#include <stdio.h>
#include <math.h>
float f(float t ,float y);
float y_exact(float t);

int main()
{
	float t, t0, t1, y0, y, h, err_bound, err;
    t0 = 0;
    t1 = 2;
    y0 = 0.5;
    h = 0.2;
    
    t = t0;
    y = y0;

    while (t <= t1 + h)
    {
       err = (y_exact(t) - y);   // error
       err_bound = (exp(t)- 1) * 0.1 * (0.5 * exp(2) - 2);  // error bound calculated
       printf(" error at t = %f is %f \n",t ,err );
       printf(" error bound at t = %f is %f \n",t ,err_bound );
       y = y + h * f(t , y);
       t = t + h ;

    }
	return 0;
}

float f(float t ,float y)   //for solving y' = f(t,y)
{
	return (y - t * t + 1);
}

float y_exact(float t)  // exact solution given
{
  return  ((t + 1) * (t + 1) - 0.5 * exp(t));
}