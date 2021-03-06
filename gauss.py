'''
    Just contains the gaus_dist function for now, see that docstring for more info
'''
import math

def gauss_dist(length : int):
    '''
    Input: Length (Integer)
    Output: An array of that length.
    The values in the array correspond to a gaussian distribution.
    The middle value of the list is the peak of the distribution.
    The values have been normalized so that the sum of the entries = 1.
    Length must be odd to have single peak value
    '''
    mean = (length-1)/2
    std_dev = (length-1)/5
    dist = []
    #y = math.e**(-0.5*(x-mean)**2/(std_dev**2))/(std_dev*math.sqrt(2*math.pi))
    for i in range(length):
        dist.append(
            math.e**(-0.5*(i-mean)**2/(std_dev**2))/
            (std_dev*math.sqrt(2*math.pi))
        )
    initial_sum = sum(dist)
    dist = [entry/initial_sum for entry in dist]
    # dist is normalized. AKA sum(dist) = 1.0
    return dist

