# Voltage_sort-DC-circuit
Abstract
This lab explains the basic concepts of DC circuits. And we explore the internal resistance for the battery in the circuit, learn how to measure the EMF of a lemon, and derive the equation of Wheatstone bridge balance. In the first part of the experiment, we assemble the circuits and find the inner resistance of the battery using the fit curve of data, which is (0.460.003)ohm. In the second part of the experiment, we measure the voltage of a lemon which is  and find that its inner resistance is very large. In the last part of the experiment, we use virtual circuits to find out the principle of Wheatstone bridge is : , and we later derive this formula using basic understanding of voltage and current in the lab report.

Question 1 (5 points): How would you know that the circuit is properly setup? Hint: The ideal voltage of the battery in use is around 1.5V 
The voltage is 1.37v on the resistance box at the beginning when current I is 0A. Because the voltage of the battery is 1.5v, when the resistance box is closed, the voltage on the box should be a little bit smaller than the voltage of the battery because there is internal resistance. Thus, from the reading of the voltage around resistance box, we can determine the circuit is properly setup.

Question 2 (10 points): Tabulate the data and make a scatter plot of the two columns Vterminal (vertically) versus Iload (horizontally). Use the proper units and axis labels. What relationship between Vterminal and Iload do you observe? Does this make sense to you? Explain the physics. 


From the scatter plot, we can find the plot of V terminal and I load is decreasing linearly. To be specific, V terminal is decreasing as Iload is increasing. We also know VAB = V0 – IloadRinternal. Because V0 and Rinternal is constant, VAB is proportional to -Iload. Thus, the result of scatter plot is reasonable. 

Question 3 (10 points): The simplest analysis required here is to fit equation (1) to your data and find out the values of V0 and Rinternal. The vertical intercept will give you V0 and the magnitude of the slope will give Rinternal. State the values (along with the error bounds) of the internal resistance and open circuit voltage obtained from the fit. 


Thus, V0=(1.360.004)V; 
R internal=(0.460.003)ohm



Question 4 (15 points): What is the goodness of your fit? Perform a simple χ2/NDOF test to make your argument? As a reminder this is given as, where N = no. of data points, n = no. of fitting parameters, σyi is the error on the measured dependent variable VAB. This error can be obtained by adding σv = 0.02V in quadrature with the propagated error on VAB from equation (1). For the propagation you will need the error on ideal voltage and internal resistance which you should have from the previous question and error on the current which is σI = 0.04A 

We know that , and the error of measurement of . Thus, =. 
And we plug the value of  into the equation in python: 
And we get that Chisquare/NDOF=0.117, which means I overestimate the error, causing the fit is “too good”. This is probably caused because we overestimate the error of current. 
Question 5 (5 points): According to the maximum power transfer theorem, maximum power for a resistive load is obtained when the load resistance is equal to the source Rinternal. Calculate the maximum power that can be obtained from your D cell battery. Power is given by P = V 2/(4R) 
From the previous code we found that V0=1.36V; R internal=0.46ohm
Thus, Pmax=1.36^2/(0.46*4)= 1.01 w 

Question 6 (10 points): Derive the above equation using your knowledge on the physics of circuits. 
R1
R2Because we know R= resistance is proportional to the length. Thus, .
When there’s no current in ammeter, 
Question 7 (10 points): At what distance do you observe the zero deflection? (Note that S is measured from the negative end (black slot) of the scale) Calculate the EMF of the lemon using the equation (3) (Use the ideal voltage for VB you found out from the previous experiment). 
When S=47.5cm, there is 0 deflection. 
The total distance L=1m. 
And we know from the previous questions that V0=VB=1.36V.
 
Question 8 (15 points): What are the errors on the length measurements S and L? Propagate your error for the EMF of the lemon using the equation (3). There is an additional error on the answer which comes from the fact that we have ignored the internal resistance of the battery and the terminal voltage is not equal to the ideal voltage we are using for this calculation. This systematic error on the Vx is 11%. Calculate the total error by adding this in quadrature with the error you get from error propagation. Report the value of the EMF along with this error bound. 
Error of S and L are all caused by the scale of the ruler, thus the error of S and L are both 0.01m. 
Because 

Then we plug the value of in python:
 Thus, Vx=.
Question 9 (10 points): Derive this equation for the balanced Wheatstone bridge using Ohm’s law and basic understanding of voltages and currents. 
From Kirchhoff’s first rule we can get that the current flow through R3 is equal to the sum of current flow through Vg and Rx. Also, the current flow through R1 is equal to the sum of current flow through Vg and R2. And let’s assume current flows from D to B in Vg.
Thus: ; .
From Kirchhoff’s second rule: 
; . Thus, ; .
Because when Wheatstone bridge is balanced, . 
Thus,  and ; 
Thus, = . Because , and we can get: .
Question 10 (10 points): Set the voltage to 10V (double click to change values) in the virtual circuit and change the R1 = 1.4Ω, R3 = 3.4Ω and Rx = 1.7Ω. What value of the R2 will balance this Wheatstone bridge? Show in your report that the current through the ammeter is zero when you input the value in the virtual circuit. 
According to the previous question, we get that . When R3=3.4ohm, R1=1.4ohm, and Rx=1.7ohm, according to the formula, R2 has to be 0.7ohm to balance the Wheatstone bridge. So, we test its result using the virtual circuit. 
In the above picture, we can see that when R2=(700m) ohm=0.7ohm, the current flow through D and B is 0A. Thus, we can be sure that when R2=0.7ohm, the Wheatstone bridge is balanced. 







Raw Data & Recordings:
0	2.39	0.26
0.2	1.70	0.57
0.3	1.51	0.67
0.5	1.19	0.81
1	0.81	0.99
2	0.49	1.13
4	0.34	1.21
The voltage at the beginning: 1.37v

I+-0.01A; R+-0.1ohm
Resistance: 
0 ohm-> 2.39A  0.26v
0.2 ohm->1.70A 0.57v
0.3 ohm->1.51A 0.67v
0.5 ohm-> 1.19A 0.81v
1ohm-> 0.81A 0.99v
2 ohm->0.49A 1.13v
4 ohm->0.34A 1.21v

Sliding contact, S: 100-52.5 cm = 47.5

Length of resistor, L: 100cm
