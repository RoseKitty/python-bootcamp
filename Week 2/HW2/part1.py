

def find_gpa_avg(gpas):
	avg_tot = 0
	for i in range(len(gpas)):
		avg_tot += gpas[i]
	avg_gpa = int(avg_tot/len(gpas))
	return avg_gpa
def find_max(outs):
	max_abs = 0
	for x in range(len(outs)):
		if outs[x] > max_abs:
			max_abs = outs[x]
	return max_abs

#problem 1
#create a dictionary
#	and ignore the questionable major of assuming, Joe?v
# oh crap, assumed gpa and majors line up, Joe has 4.0 
# pray for people
students = {
	"Name" : ["Bob", "Alice", "Charlie", "Delilah", "Joe", "Esperanza"] ,
	"Major" : ["EE", "CpE", "ChemE", "Journalism", "Stalking", "MechE"],
	"GPA" : [1.5, 2.5, 3.8, 2.1, 4.0, 3.0]
}
#part 3
#avg gpa
gpas = students["GPA"]
print(find_gpa_avg(gpas))

## problem 2 
#add a section to the dictionary 
absences = [1298, 5, 3, 1, 0, 2] 
students["Num of absences"] = absences
#part 4
#find max
print(find_max(absences))

#part 5
#reset absence
students["Num of absences"].clear()
for values in students.values():
	print(values)
	#pass
#part 6
#add a newbie
students["Name"].append("Fernando")
students["Major"].append("EE")
students["GPA"].append(3.2)
#students["Num of absences"].append(0)
absences.append(0)
#both of these work since they are lists defined prev
#kinda weird place for it since now there is a val in absences
for values in students.values():
	print(values)
	
