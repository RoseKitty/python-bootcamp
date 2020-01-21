#when importing
#looks first in current working directory
#this folder basically. 
#  import classes #don't have to write .py part


#if not in your current- it looks in a folder place where all the packages and where
#all the pip stuff comes from.. 
#unless told look somewhere else

#you can also import only parts of it. 

from classes import wheel, engine, body
#from classes import * #imports all 

tire = wheel(18)
print(tire.size)

camry_eng = engine(180,4)
print(camry_eng.horsepower)
print(f"my car's engine has: {camry_eng.cylinders} cylinders")

camry_body = body("silver")#, num_doors=5)
print(camry_body.boot_size)
