# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:03:14 2023

@author: tonya
"""

  
#Question a
#Shear force(v) and bending moment(M) at the 1st end is 0,x=0
w = 10   
Load_intensity = w

L = 12   
beam_length = L

x = 0    



M = (w * (-6*x**2 + 6*L*x - L**2))/12


V = w * ((L/2) - x)

print(f'a) Moment when x = 0 is {M}KN/m') 
print() 
print(f'V when x = 0 is V = {V}KN')


x = 12
M = (w * (-6*x**2 + 6*L*x - L**2))/12
print()
print(f'Moment when x = 12 is {M}KN/m')

V = w * ((L/2) - x) 
print()
print(f'V when x = 12 is {V}KN')


#Question b

a = -6
b = 72
c = -144

com_square = b/(2*a)


constant = -c/a + com_square**2

 

contraflexure_a = (constant**0.5 - com_square)
contraflexure_b = (-constant**0.5 - com_square)

print()
print(f'b)The distances at which the bending moment will be zero are x1 = {contraflexure_a} and x2= {contraflexure_b}') 

#Question c
V = 0 
x = V + (L/2) 
point_of_zero_shear_force = x 
print()
print('c) ' + str(point_of_zero_shear_force) + ' is the point at which the Shear Force is = 0')

#Question d
import numpy as np
beam_length = 12  
steps = 0.01 
w = 10
span_of_beam = np.arange (0, beam_length + steps, steps) 
x = span_of_beam 
M = w * (-6*x**2 + 6*L*x - L**2)/12 
print()
print('e) The Moment for each step along the span is {0}'.format(M))




#Question e
start = 0 
step = 0.01 
k = L + step 
x = np.arange(start,k,step)
V = w*(L/2 - x) 
print()
print('(e) The shear force for each step along the span is {}'.format(V))


#Question f
"""
Let the absolute value of the bending moment array be AM
Also let the minimum AM be m_AM
"""
AM = abs(span_of_beam) 
m_AM = min(AM)
"""
When the bending moment is m_AM, we get an expression x**2 - Lx + (L**2/6)+(2*m_AM)/w = 0
"""

#from the above expression
a = 1
b = -L
c = (L**2/6)+(2*m_AM)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a
print()
print(f'f)The points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(root_1f,root_2f))     


#Question g
"""
Let the relative errors be r_error
"""
r_error_1 = ((9.464101615137753-9.46)/9.464101615137753*100)
r_error_2 = (( 2.539999999999999-2.5358983848622456)/2.539999999999999*100)
print()
print('(g) The relative errors between estimated points of contra-flexure are {0}% and {1}%'.format(r_error_1,r_error_2))



#Question h
import numpy as np
def calculate_M(w, L, x):
    return(w * (-6*x**2 + 6*L*x - L**2)/12)

beam_length = 12
steps = 10
BMoment_values = []

for x in span_of_beam:
    M = calculate_M(w, L, x)
    BMoment_values.append(M) 
    
max_Y = max(BMoment_values) 
min_Y = min(BMoment_values)
print()
print("h) Maximum bending moment:", max_Y) 


print()
print("Minimum bending moment:", min_Y) 
https://github.com/Tonyame10