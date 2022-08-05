from game_data import data
import art
import random

def random_choise(data):
    random_sample = random.sample(data, 2)
    choise_1 = random_sample[0]
    choise_2 = random_sample[1]
    print(art.logo)
    print(f"campare A: {choise_1['name']}, a     {choise_1['description']}, from {choise_1['country']}")
    print(art.vs)
    print(f"campare A: {choise_2['name']}, a {choise_2['description']}, from {choise_2['country']}")
    followers_a = choise_1['follower_count']
    followers_b = choise_2['follower_count'] 
    return (followers_a, followers_b)

def compare(two_samples):
    print(two_samples[0], two_samples[1])
    if two_samples[0] > two_samples[1]:
        return "A"
    else:
        return "B"

def game(higher, score):
    #while
    choise = input("Type 'A' or 'B'")
    if choise == higher:
        score +=1
        print(f" You win, your score is {score}")
        return score
    else:
        print("You lose, start again")
        return -1
    


score = 0
while score !=-1:  
    num_of_followers = random_choise(data)
    print("num_of_follwers")
    higher = compare(num_of_followers)
    score = game(higher, score)
