#create a function that calculates the area of a right cylinder
#and one for a cone as well 
#pi = import math, and you get math.pi
import math

def vol_cylinder(h,r):
	area_cyl = 2*(math.pi)*r*h + 2*(math.pi)*(r**2)
	vol_cyl = math.pi *(r**2)*h
	return vol_cyl

#print(vol_cylinder(1,1)) #testing

def vol_cone(h,r):
	area_cone = (math.pi)*r*(r +((h**2)+(r**2))**(1/2))
	vol_co = (h/3) * math.pi*(r**2)
	return vol_co
#print(vol_cone(1,1)) #testing
