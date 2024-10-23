import random
import emoji

score = 0
wickets = 0
deliveries_guide = ['yorker' , 'bouncer' , 'standard' , 'off-cutter' , 'leg-cutter']
deliveries = [1,2,3,4,5]
shots_guide = ['block/dodge' , 'cover-drive' , 'cut' , 'leg-glance' , 'pull']
shots = [1,2,3,4,5]

mic = emoji.emojize("\U0001F399")
bat = emoji.emojize("\U0001F3CF")

print("Hello")
name = input("Please enter your name: ")
print("Welcome, " , name)
print("Score 50 runs to win. You have 10 wickets. \nShots allowed: 1 , 2 , 3 , 4 , 5 . \n")
print("Shots Guide" , shots_guide)
print("Deliveries Guide" , deliveries_guide)

while wickets < 10 :
    if(score >= 50):
        print("Congratulations! You won! Your score is " , score , " / " , wickets)
        break
    delivery = random.choice(deliveries)
    user_input = input("Play a shot: ")
    try:
        shot = int(user_input)
        if shot < 1 or shot > 5:
            print("Please enter a number between 1 and 5 \n")
            continue
        print("PC says: " , delivery)
        if (delivery == 1):    
            match shot:
                case 1:
                    print(mic , ": Safely defended. No runs.")
                case 2:
                    print(mic , ": BOWLED!") ; wickets += 1
                case 3:
                    print(mic , ": BOWLED!") ; wickets += 1
                case 4:
                    print(mic , ": Risky shot, but he gets 2 runs!") ; score = score + 2
                case 5:
                    print(mic , ": BOWLED! What was he thinking? ") ; wickets += 1
        if (delivery == 2):    
            match shot:
                case 1:
                    print(mic , ": Bouncer! Safely dodged. WIDE!") ; score = score + 1
                case 2:
                    print(mic , ": Wrong shot! Gets hit in the head!")
                case 3:
                    print(mic , ": Nasty bouncer! Gets hit in the chest!") 
                case 4:
                    print(mic , ": Oh he gets hit in the shoulder!")
                case 5:
                    print(mic , ": What a shot! That's a big six!") ; score = score + 6
        if (delivery == 3):    
            match shot:
                case 1:
                    print(mic , ": Defended.")
                case 2:
                    print(mic , ": Beautiful cover-drive! 4 runs!") ; score = score + 4
                case 3:
                    print(mic , ": Cuts it and the batters run for 2.") ; score = score + 2
                case 4:
                    print(mic , ": Glances towards the Deep and they run fast! 3 runs.") ; score = score + 3
                case 5:
                    print(mic , ": Pulls that delivery for a flat six!") ; score = score + 6 
        if (delivery == 4):    
            match shot:
                case 1:
                    print(mic , ": Defended.")
                case 2:
                    print(mic , ": Edged and gone! Tries to drive but gets an outside edge. ") ; wickets += 1
                case 3:
                    print(mic , ": That's close! Outside edge flies away. Batters run for 2.") ; score = score + 1
                case 4:
                    print(mic , ": Beaten! Tries to glance it away, but fails.")
                case 5:
                    print(mic , ": A wild swing! The bat was nowhere near the ball.") 
        if (delivery == 5):    
            match shot:
                case 1:
                    print(mic , ": Defended.")
                case 2:
                    print(mic , ": BOWLED! Exposes his stumps for a drive and pays the price.") ; wickets += 1
                case 3:
                    print(mic , ": LBW! Gets hit on the pads.") ; wickets += 1
                case 4:
                    print(mic , ": Perfectly glanced for 4!") ; score = score + 4
                case 5:
                    print(mic , ": Hit in the air, but lands safe. 2 runs.") ;  score = score + 2
            print("Your score: " , score , " / " , wickets , "\n")
    except ValueError:
        print("Not a number! \n")