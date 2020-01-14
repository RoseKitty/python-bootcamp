import random

def org_game():
	#hard coded to 3 doors only
	door_contents = [1, 0, 0]
	random.shuffle(door_contents)
	
	for i in range(0, len(door_contents)):
		if door_contents[i] == 1:
			winning_door = i
	print(i)
	return door_contents, winning_door
	
#help(random.shuffle) #take a list and shuffles them
#kinda like deck shuffle, no return and shuffles list
def game_time():
	door_nums = [0, 1, 2]

	door_contents, winning_door = org_game()

	#user makes a choice. 
	door_choosen = random.choice(door_nums)

	#game show host opens another door, not winning_door or your pick
	univailable_door = [door_choosen, winning_door]
	door_opened = set(door_nums).difference(univailable_door)
	door_opened = door_opened.pop()
	switched_win = False
	stayed_win = False
	#final_choice = 
#game_time()
#org_game()

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

