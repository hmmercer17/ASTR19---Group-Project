#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:08:11 2026

@author: maddyjanebronson
"""
'''
y = m*x+b+A*np.sin(B*x + C)

y = m add rulle *b+ 

y = b + A*np.sin(B*x + C) error add

y = A * (B+C) error multply

y = B + C error add

y = B*x error m
 
y = b + c error add



Using error propagation, 
find out what the root mean squared uncertainty in your measurement of D 
and the transit time is. Don't forget to take into account both the uncertainty 
in the data and the uncertainty from your fits. 
    
then put those values into the og equation
the uncertainity values are from the perr fct above
'''

sigmam = 5.53228901e-04
sigmab = 1.03240464e-04
sigmaA = 1.47250729e-04
sigmaB = 2.89767358e-01
sigmaC = 5.24081955e-02

m = .03
b = 3
A = .1
B = -50
C = -20

sigmaCB = (sigmaB**2 + sigmaC**2)**5

sigmaBA = (sigmaCB/(C+B)) + (sigmaA/A)*(A*sigmaCB)

sigmaAb = (sigmab**2 + sigmaBA**2)**5

sigmafinal = (sigmam**2 + sigmaAb**2)**5

print(f"The Error Propagation for the whole data set is {sigmafinal}")


#error sigmafinal/0.003 that I found via the whole thing above
#errorprop(z) = sigmafinal(/0.003


errorprop = (sigmafinal/(m+b+A*(B+ C))) + (0.003/0.0003) * 0.003

print(f"The given uncertainty divided by the uncertainty found is {errorprop}")

    
'''
this is for the errorprop of D
D = (Rp/Rs)**2

Rp = np.sqrt(D) * Rs
Rp = D^(0.5)
'''

D = depth
Rp = rPlanet
Rs = rStar
sigmad = 0.5*(0.5/D)


print(f"The uncertainty of D is {sigmad}")

