def maxCandiesCount(candies):
    alice_left = 0
    bob_right = len(candies) - 1
    
    alice_candies = 0
    bob_candies = 0
    
    while True:
        if alice_left > bob_right:
            break
        if alice_candies <= bob_candies:
            alice_candies += candies[alice_left]
            alice_left += 1
        else:
            bob_candies += candies[bob_right]
            bob_right -= 1
    
    candies_eaten = len(candies)
    alice_left -= 1
    bob_right += 1

    while alice_candies != bob_candies and alice_left > 0 and bob_right < len(candies):
        if alice_candies > bob_candies:
            alice_candies -= candies[alice_left]
            alice_left -= 1
        else:
            bob_candies -= candies[bob_right]
            bob_right += 1
        candies_eaten -= 1
    
    return candies_eaten


print(maxCandiesCount([10,10,10,1]))


