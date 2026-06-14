# World Cup Tournament Simulation
# Author: Aita Joshua Prince (aitajprince100@gmail.com)
# Topic: nested loops, break, continue, pass

team_strength = 60
team_morale = 50
injuries = 0
group_points = 0
tournament_won = False
tournament_lost = False


def future_feature():
	pass


print("===============================")
print("WORLD CUP TEAM MANAGER v0.0.1")
print("===============================\n")

print("Pre-tournament preparation\n")

for day in range(1, 4):
	print(f"Preparation day {day}")
	print("1. Training")
	print("2. Friendly match")
	print("3. Recovery")
	print("4. Future feature")

	while True:
		try:
			choice = int(input("Choose an activity\n"))
			break
		except ValueError:
			print("Please enter a number")

	if choice == 1:
		team_strength += 4
		team_morale += 2
		print("Training improved the team")

	elif choice == 2:
		team_strength += 1
		team_morale += 3
		print("The friendly match built confidence")

	elif choice == 3:
		if injuries > 0:
			injuries -= 1
		team_morale += 2
		print("Recovery day completed")
		continue

	elif choice == 4:
		future_feature()

	else:
		print("Invalid option, no change made")

	print(f"Strength: {team_strength}, Morale: {team_morale}, Injuries: {injuries}\n")


print("Group stage begins\n")

for match in range(1, 4):
	print(f"Group match {match}")

	for half in range(1, 3):
		print(f"Half {half}")
		print("1. Attack")
		print("2. Balance")
		print("3. Defend")
		print("4. Future feature")

		while True:
			try:
				tactic = int(input("Choose a tactic\n"))
				break
			except ValueError:
				print("Please enter a number")

		if tactic == 1:
			team_strength += 2
			team_morale += 1
		elif tactic == 2:
			team_morale += 2
		elif tactic == 3:
			team_strength += 1
			print("The team stays compact")
			continue
		elif tactic == 4:
			future_feature()
		else:
			print("Invalid tactic")

	team_power = team_strength + team_morale - (injuries * 5)
	opponent_power = 68 + (match * 4)

	print(f"Team power: {team_power}")
	print(f"Opponent power: {opponent_power}")

	if team_power >= opponent_power + 5:
		print("Match won")
		group_points += 3
		team_morale += 3
	elif team_power >= opponent_power:
		print("Match drawn")
		group_points += 1
	else:
		print("Match lost")
		team_morale -= 3
		injuries += 1

	print(f"Group points: {group_points}\n")

	if match == 3 and group_points < 4:
		print("The team failed to qualify from the group stage")
		tournament_lost = True
		break


if not tournament_lost:
	print("Knockout stages begin\n")

	knockout_rounds = ["Round of 16", "Quarter-final", "Semi-final", "Final"]

	for round_name in knockout_rounds:
		print(round_name)
		print("1. Attack")
		print("2. Balance")
		print("3. Defend")
		print("4. Future feature")

		while True:
			try:
				tactic = int(input("Choose a knockout tactic\n"))
				break
			except ValueError:
				print("Please enter a number")

		if tactic == 1:
			team_strength += 3
			team_morale += 1
		elif tactic == 2:
			team_morale += 2
		elif tactic == 3:
			team_strength += 1
		elif tactic == 4:
			future_feature()
		else:
			print("Invalid tactic")

		round_power = team_strength + team_morale - (injuries * 5)
		round_target = 74

		if round_name == "Quarter-final":
			round_target += 3
		elif round_name == "Semi-final":
			round_target += 6
		elif round_name == "Final":
			round_target += 9

		print(f"Team power: {round_power}")
		print(f"Target power: {round_target}")

		if round_power >= round_target:
			print(f"{round_name} won\n")
			team_morale += 3

			if round_name == "Final":
				tournament_won = True
				break
		else:
			print(f"{round_name} lost\n")
			tournament_lost = True
			break


print("Tournament summary\n")
print(f"Strength: {team_strength}")
print(f"Morale: {team_morale}")
print(f"Injuries: {injuries}")
print(f"Group points: {group_points}")

if tournament_won:
	print("Your team won the World Cup")
elif tournament_lost:
	print("Your team was eliminated")
else:
	print("Tournament ended without a winner")

