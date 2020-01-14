import random

def org_game():
	#hard coded to 3 doors only
	door_contents = [1, 0, 0] #1 door wins, others lose
	#this v shuffles indices of list
	random.shuffle(door_contents)
	
	#linear search to find winning_door
	for i in range(0, len(door_contents)):
		if door_contents[i] == 1:
			winning_door = i
	#	print(i)
	#return list of door contents and number of winning_door
	return door_contents, winning_door
	
#help(random.shuffle) #take a list and shuffles them
#kinda like deck shuffle, no return and shuffles list
def game_time():
	door_nums = [0, 1, 2] #3 doors
	#runs the prev function, puts contents behind door
	#tells "host" which is winning_door
	door_contents, winning_door = org_game()

	#user makes a choice. 
	door_chosen = random.choice(door_nums)

	#game show host opens another door, not winning_door or your pick
	univailable_door = [door_chosen, winning_door]
	#uses sets to find door leftover. 
	door_opened = set(door_nums).difference(univailable_door)
	door_opened = door_opened.pop()
	#opens door we just picked 
	opened_door = door_nums[door_opened]
	#declare variables to know about win from switch or stay 
	switched_win = False
	stayed_win = False
	#simulate 
	univailable_doors = [door_chosen, opened_door]
	switched_choice = set(door_nums).difference(univailable_doors)
	switched_choice = switched_choice.pop()

	#use index val from switched_choice variable to find door_contents
	if door_contents[switched_choice] == 1:
		switched_win = True
	if door_contents[door_chosen] == 1:
		stayed_win = True

	return int(switched_win), int(stayed_win)
	#final_choice = #this is from day 4, but turned into the switched choice above
def monte_carlo(n):
	total_switched_wins = 0
	total_stayed_wins = 0

	switched_win = 0
	stayed_win = 0
	for game_num in range(0,n):
		switched_win, stayed_win = game_time()
		if switched_win == 1:
			total_switched_wins += switched_win
		else:
			total_stayed_wins += stayed_win
	print(f"Out of {n} plays")
	print(f"switched wins = {(total_switched_wins/n) *100} %")
	print(f"stayed wins = {(total_stayed_wins/n) *100} %")
#game_time() #tests if runs or not
#org_game()
monte_carlo(1000)
#notice that the switched wins are like 2/3 
#vs stayed win 1/3 


##### notes on sets
	#sets: almost like a list, but.. 
	#lists cane have repeating numbers, strings, etc. 
	#sets are only unique numbers. list can turn into a set
	#list1 = [1,1,2,3,,5,5,5]
	#mylist = set(list1) 
	#outputs mylist = [1,2,3,5]
	#basically, hw problem, add both lists into a temp and use set(temp_list), easy solve
	#
	#list2 = [1,5,6]
	#list3 = set(list1).difference(list2) #need list 1 need to be set, second who cares
	#print(list3) #would output [2 and 3], sets = {}, list = []


#in research- monte carlo is a valid proof. 
