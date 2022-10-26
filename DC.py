from cmath import pi
import math
import operator
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

Data=np.loadtxt("/Users/angelaxing/Desktop/2022spring/Phys 19B/Lab3/lab3.txt",delimiter='\t').transpose()
Resistance=Data[0] 
Vlotage=Data[2] #Voltage is the reading of V terminal
Current=Data[1] #Current is the reading of I load

plt.scatter(Current, Vlotage) #scatter plot of V terminal and I load
plt.xlabel("Current [A]")
plt.ylabel("Voltage [v]")
plt.title('I load VS V terminal' )
plt.show()

def Vab(I,R,V0):
    return V0-(I*R)
params,extras=curve_fit(Vab,Current,Vlotage)
R,V0=params #???R is parameter??
plt.plot(Current,Vlotage,"o")
plt.plot(Current,Vab(Current,R,V0))
err = np.sqrt(np.diag(extras))
print("Error of R and V0=",err)
print("R=",R)
print("V0=",V0)
plt.xlabel("Current [A]")
plt.ylabel("Voltage [v]")
plt.title('I load VS V terminal' )
plt.show()

VAB=V0-Current*R
errorCurrent=0.04
errorMeasureV=0.02
errorVlotage=np.sqrt(errorCurrent**2*Resistance**2+err[0]**2*Current**2+err[1]**2+errorMeasureV**2)
print("Error of Vab=",errorVlotage)
Chisquare=np.sum((Vlotage-VAB)**2/errorVlotage**2)
ChisquareNDOF=Chisquare/(len(Vlotage)-2) 
print("ChisquareNDOF=",ChisquareNDOF)

errorL=0.01
errorS=0.01
errorVb=err[1]
errorVx=0.65
percentage=0.11
S=0.475
L=1
Vb=V0
errorVx=np.sqrt(errorL**2*(S/(L**2)*Vb)**2+errorS**2*(Vb/L)**2+errorVb**2*(S/L)**2+(percentage*errorVx)**2)
print("Error of Vx=",errorVx)

