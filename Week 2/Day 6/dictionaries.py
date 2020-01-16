#in c++ map; hashtable
#it's a key and map... 
#used in data analysis and networking
#dataframes are nice dictionaries... 
#pandas better. no time though so... we're doing basics

my_pers_info = {
	"name" : "You",
	"DOB" : "15-1/20",
	"School" : "CCNY",
	"GPA" : 0.5
}
#dictionaries are known for their "key values" pair system
#need a comma after each key value pair. 
name1 = my_pers_info["name"]
print(name1)

if "job" in my_pers_info:
	print("Yep")
else:
	print("Nope")

if "name" in my_pers_info:
	print("Yep")
else:
	print("Nope")


#printing all keys
for key in my_pers_info:
	print(key)
	#if needed, you can comment out and write pass to get less outputs
#printing all vals (without key)
for value in my_pers_info.values():
	print(value)
