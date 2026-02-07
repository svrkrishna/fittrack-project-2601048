
# Player Score Calculator
# Input Collection
Player_Name = input("Enter the Player Name: ")
# Numeric Input Processing
Games_Played = int(input("Enter the Games Played: "))
# Score Data Entry
Total_Score_Achieved = int(input("Enter Total Score: "))
# Computation
Average_Score = Total_Score_Achieved / Games_Played
# OutputDisplay
print(f"\nPlayer: {Player_Name}")
print(f"\nGames Played: {Games_Played}")
print(f"\nTotal Score: {Total_Score_Achieved}")
print(f"\nAverage Score: {Average_Score}")
