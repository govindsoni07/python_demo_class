user1=input("Enter player1 choice : ")
user2=input("Enter player2 choice : ")
if user1==user2:
    print("Tie")
elif(user1=='rock' and user2=="scissor" or user1=='paper' and user2=="rock" or user1=='scissor' and user2=="paper"):
    print("Player 1 win")
else:
    print("Player 2 win")