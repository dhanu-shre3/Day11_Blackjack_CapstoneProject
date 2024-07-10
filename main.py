############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo

import random

#1. Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

def play_game():
    print(logo)
    def calculate_score(cards):
        """Takes a list of card and returns a score calculated from the cards"""
        #Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        if sum(cards) ==21 and len(cards) == 2:
            return 0
        
    #Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

        elif 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    #13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif computer_score == 0:
            return "lose, oponnent has Blackjack"
        elif user_score == 0:
            return "Won, user has Blackjack"
        elif user_score > 21:
            return "You went over, you lose"
        elif computer_score >21:
            return "Oponnent went over, you won"
        elif user_score > computer_score:
            return "You win"
        else:
            return "you lose"
    #2. Deal the user and computer 2 cards each using deal_card() and append().
    user_card = []
    computer_card = []

    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    #11.The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

    while not is_game_over:

        #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card} and Current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        #If the game has not ended, ask the user if they want to draw another card. 
        # If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            user_should_deal = input("Type 'y' to add another card or 'n' to pass: ")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True    


    # 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

    while computer_score != 0 and computer_score > 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f" Your final hand is: {user_card} Final score: {user_score}")
    print(f"Computer's final cards are: {computer_card} Final score: {computer_score}")
    print(compare(user_score, computer_score))    

#14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you wanna play a game of blackjack? Type 'yes' or 'no'") == "yes":
    play_game()
