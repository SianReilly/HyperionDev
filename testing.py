team1_score = 3
team2_score = 4
game = "Over"


if (team1_score > team2_score) and (game == "Over"):
    print("Congratulations Team 1, you have won the match!")
else:
    print ("Congratulations Team 2, you've won the match")

speed = int(input("How many kilometres per hour are you travelling at?"))
belt = input("Are you wearing a safety belt?")

if (speed > 80) or (belt != "Yes"):
    print("Sorry Bean, but I have to give you a traffic fine.")