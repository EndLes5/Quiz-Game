#Code by <\Endless> 
#A simple python quiz game that utilizes loops(for loop), functions and inbuilt python modules(time & system)


#Modules & score variable
import time
import os
score = 0

#Function for clearing a previous output
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

#Questions(variables)
q1 = {"How many time zones are there in the world?\na. 20\nb. 24\nc. 12\nd. 7"}
q2 = {"How many continents are there in the world?\na. 7\nb. 8\nc. 6\nd. 5"}
q3 = {"Which is the smallest country in the world?\na. Monaco\nb. Nauru\nc. Vatican city\nd. Tuvalu"}
q4 = {"Which is the largest ocean in the world?\na. Pacific ocean\nb. Atlantic ocean\nc. Indian ocean\nd. Arctic ocean"}
q5 = {"Which of these countries/cities is not in Africa!\na. Cameroon\nb. Cape town\nc. Lagos\nd. Estonia"}


#Question 1 starts here
for one in q1:
	print(one)
	player = input("Select the correct option : ")
	ans = player
	clear()
	#If correct
	if ans.lower() == "b":
			print("Correct!\nThere are 24 time zones in the world\nLoading next question...")
			score += 1
			time.sleep(1.5)
			clear()
	#If incorrect
	if ans.lower() != "b":
			print("Incorrect!\nb(24) is the correct answer\nLoading next question...")
			time.sleep(1.5)
			clear()
			
	#Question 2 starts here			
	for two in q2:
		print(two)
		player2 = input("Select the correct option : ")
		ans2 = player2
		clear()
		#If correct
		if ans2.lower() == "a":
			print("Correct!\nThere are 7 continents in the world\nLoading next question...")
			score += 1
			time.sleep(1.5)
			clear()
		#If incorrect
		if ans2.lower() != "a":
			print("Incorrect!\na(7) is the correct answer\nLoading next question...")
			time.sleep(1.5)
			clear()
		
		#Question 3 starts here		
		for three in q3:
			print(three)
			player3 = input("Select the correct option : ")
			ans3 = player3
			clear()
			#If correct
			if ans3.lower() == "c":
				print("Correct!\nVatican city is the smallest country in the world\nLoading next question...")
				score += 1
				time.sleep(1.5)
				clear()
			#If incorrect
			if ans3.lower() != "c":
				print("Incorrect!\nc(Vatican city) is the correct answer\nLoading next question...")
				time.sleep(1.5)
				clear()

			#Question 4 starts here						
			for four in q4:
				print(four)
				player4 = input("Select the correct option : ")
				ans4 = player4
				clear()
				#If correct
				if ans4.lower() == "a":
					print("Correct!\nPacific ocean is the largest ocean in the world\nLoading next question...")
					score += 1
					time.sleep(1.5)
					clear()
				#If incorrect
				if ans4.lower() != "a":
					print("Incorrect!\na(Pacific ocean) is the correct answer\nLoading next question...")
					time.sleep(1.5)
					clear()

				#Question 5 starts here
				for five in q5:
					print(five)
					player5 = input("Select the correct option : ")
					ans5 = player5
					clear()
					#If correct
					if ans5.lower() == "d":
						print("Correct!\nEstonia is not located in Africa\nLoading next question...")
						score += 1
						time.sleep(1.5)
						clear()
					#If incorrect
					if ans5.lower() != "d":
						print("Incorrect!\nd(Estonia) is the correct answer\nLoading next question...")
						time.sleep(1.5)
						clear()

#Final result output
print("Quiz completed\nTotal score : " + str(score) + "/5\nThanks for playing...")			