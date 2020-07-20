
#using the manual method 
fluxes = [23.3, 42.1, 2.0, -3.2, 55.6]
m = sum(fluxes)/len(fluxes)
print(m)

#using the python statistics module 

from statistics import mean
fluxes = [23.3, 42.1, 2.0, -3.2, 55.6]
m = mean(fluxes)
print(m)


#writing a function to calculate the mean 
def calculate_mean(a):
  m = sum(a)/len(a)
  return(m);

mean = calculate_mean([1, 2.2, 0.3, 3.4, 7.9])
print(mean)
