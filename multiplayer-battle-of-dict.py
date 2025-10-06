import random
import copy

def rollD6():
    return random.randint(1, 6)

def rollD10():
    return random.randint(1, 10)


# Dictionary template
player_info = {
    "Name": "",
    "Email": "",
    "Country": "",
    "Wins": 0,
    "rolls": []
}

players = []
round_history = []

print("🎲 Welcome to Battle of Dices! 🕹️ (Multiplayer Mode)")

winning_score = int(input("How many wins are needed to win the game? Pick a number: "))
num_players = int(input("How many players will play?: "))

# Register players
for i in range(num_players):
    player = copy.deepcopy(player_info)
    player["Name"] = input(f"What is the name of Player {i+1}? ")
    player["Email"] = input(f"What is the E-Mail of Player {i+1}? ")
    player["Country"] = input(f"What is the country of Player {i+1}? ")
    players.append(player)

round_number = 1

# Game loop
while True:
    print("\n--- Round " + str(round_number) + " --- ")
    input("Press ENTER to roll the dice...")

    rolls = []
    for i in range(num_players):
        roll = rollD6() + rollD10()
        rolls.append(roll)
        players[i]["rolls"].append(roll)
        print(players[i]["Name"] + " rolled: " + str(roll))

    highest_roll = max(rolls)
    winners = [i for i, r in enumerate(rolls) if r == highest_roll]

    # Update Wins and round history
    if len(winners) == 1:
        w = winners[0]
        players[w]["Wins"] += 1
        round_history.append({
            "Round": round_number,
            "Winner": players[w]["Name"],
            "Rolls": rolls.copy()
        })
        print(players[w]["Name"] + " wins this round!")
    else:
        tie_names = " & ".join([players[w]["Name"] for w in winners])
        round_history.append({
            "Round": round_number,
            "Winner": "Tie: " + tie_names,
            "Rolls": rolls.copy()
        })
        print("It's a tie between: " + tie_names)

    # Print Score Table
    print("\n--- Score Table ---")
    print("Player\tWins")
    for p in players:
        print(f"{p['Name']}\t{p['Wins']}")

    # Print Round History
    print("\n--- Round History ---")
    for r in round_history:
        print(f"Round {r['Round']}: {r['Winner']} | Rolls: {r['Rolls']}")

    # Check for overall winner
    game_winner = None
    for i, p in enumerate(players):
        if p["Wins"] >= winning_score:
            game_winner = i
            break

    if game_winner is not None:
        print("\n🏆 " + players[game_winner]["Name"] + " is the overall winner! 🏆")
        break

    round_number += 1

