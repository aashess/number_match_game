# import required function
import random

# use required input for user and computer.
def inpuut():
    user = int(input("Choose Your Number: "))
    computer1 = random.randint(1, 10)
    computer2 = random.randint(1, 10)
    computer3 = random.randint(1, 10)
    leader = random.randint(1, 2)
    print(f"l={leader} u={user} c1={computer1} c2={computer2} c3={computer3}")
    return user, computer1, computer2, computer3, leader

# make required function 
# user, computer1, computer2, computer3, leader
def gameplay():
    players = {'user': 0, 'computer1': 0, 'computer2': 0, 'computer3': 0}
    
    while max(players.values()) < 3:
        # Call inpuut() once per iteration, store the results
        user, computer1, computer2, computer3, leader = inpuut()

        if user == leader:
            players['user'] += 1
        elif computer1 == leader:
            players['computer1'] += 1
        elif computer2 == leader:
            players['computer2'] += 1
        elif computer3 == leader:
            players['computer3'] += 1

    winner = max(players, key=players.get)
    print(f"The winner is: {winner} with a total of {players[winner]}")

# Run the game
gameplay()
