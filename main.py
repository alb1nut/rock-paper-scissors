import random


while True:
    # try:
        options=['R','P','S']
        player_choice= input('Please pick an option between "R", "P" or "S": ').upper()
        computer_choice = random.choice(options)

        if player_choice in options:
            if player_choice == computer_choice:
                print('Player ' +player_choice +' : CPU ' +computer_choice)
                print('Its a tie Both players selected ' + player_choice )
            elif player_choice == 'R':
                if computer_choice == "S":
                    print('Player ' +player_choice +' : CPU ' +computer_choice)
                    print('Rock smashes scissors! You win!')
                else:
                    print('Player ' +player_choice +' : CPU ' +computer_choice)
                    print("Paper covers rock! You lose.")  
            elif player_choice == 'P':
                if computer_choice == 'R':
                    print('Player ' +player_choice +' : CPU ' +computer_choice)
                    print('Paper covers rock! You Win.')  
                else:
                    print('Player ' +player_choice +' : CPU ' +computer_choice)
                    print('Scissors cuts Paper! You Lose!')
            elif player_choice == 'S':
                if computer_choice == 'P':
                    print('Player ' +player_choice +' : CPU ' +computer_choice)
                    print("Scissors cuts paper! You Win.")
                else:
                    print('Player ' +player_choice +' : CPU ' +computer_choice)
                    print('Rock smashes scissors! You Lose!')
        if not player_choice  in  options:
            print('Error Ocured, Please try again')
            print('You picked : ' +player_choice)
                
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
    # except:
    #     print('Error Ocured, Please try again')
    #     print('You picked : ' +player_choice)
    #     play_again = input("Play again? (y/n): ")
    #     if play_again.lower() != "y":
    #         break

    