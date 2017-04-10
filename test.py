"""

test.py - Alex Green

Coding test for Liligo application, 10/04/17.

"""

import random

def genlist():
    """
	Generate the test data.
	"""
    random.seed(123)
    list = []
    for i in range(0,8999):
        list.append(random.random())
    return list


def calc(datain, percent):
    """
    Run the statistical calculations.
    
    Input:
		datain: List/array containing data.
		percent: Confidence interval required in percent, 90 or 95.
		
	Output:
	    Prints results to console:
	        1) Mean
	        2) Standard deviation
	        3) Confidence interval for the mean
    """

    # Z score for confidence intervals
    z90 = 1.645
    z95 = 1.96

    num = len(datain)  # Number of values in dataset
    sum = 0            # Sum of data
    sumsq = 0          # Sum of squares
    
    # Add up the data
    for i in range(0, num):
        sum = sum + datain[i]
        sumsq = sumsq + datain[i]**2
    
    num = float(num)      # Force floating point divison
    mean = sum / num
    meansq = sumsq / num  # Mean of the squares
    
    # Calculate standard deviation
    stddev = (meansq - mean**2)**0.5
    
    # Set the confidence interval required
    if percent == 90:
        z = z90
    else:
	if percent == 95:
        	z = z95
	else:
		print "Error: confidence interval not supported"
		return
        
    # Calculate confidence intervals    
    upper = mean + z * stddev / num**0.5
    lower = mean - z * stddev / num**0.5
    
    # Output results
    print "Mean =", mean
    print "Standard deviation:", stddev
    # Showing 5 d.p. as z-score not high precision
    print percent, "% confidence interval for the mean:", "%.5f" %lower, "-", "%.5f" %upper
    
    return

  
# Results
"""
>>> calc(list,90)
Mean = 0.501825068674
Standard deviation: 0.289771528727
90 % confidence interval for the mean: 0.49680 - 0.50685

>>> calc(list,95)
Mean = 0.501825068674
Standard deviation = 0.289771528727
95 % confidence interval for the mean: 0.49584 - 0.50781
"""
    
    
    
