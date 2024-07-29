#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def match_value(A, B):
    i = j = matches = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            matches += 1
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return matches

def initialize_data():
    # Generate random PWNs and SWNs
    numbers = list(range(1, 31))
    random.shuffle(numbers)
    #WinNo = [1,2,3,4,5,6,7,8]        #for result debugging
    WinNo = numbers[:8]
    insertion_sort(WinNo[:6])
    selection_sort(WinNo[6:])

    # Generate random game numbers for 1000 players
    lotto = []
    for _ in range(1000):
        player_numbers = random.sample(range(1, 31), 6)
        merge_sort(player_numbers)
        lotto.append(player_numbers)
    
#     # for result debugging              ####################
#     player_numbers = [1,2,3,4,5,6,7,8]        
#     lotto.append(player_numbers)
#     
    return lotto, WinNo

def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

def process_winners(lotto, WinNo):
    pwns = WinNo[:6]
    swns = WinNo[6:]
    winner_stats = {'1st class': 0, '2nd class': 0, '3rd class': 0, '4th class': 0}
    
    for game_numbers in lotto:
        pwn_count = sum(1 for num in game_numbers if num in pwns)
        swn_count = sum(1 for num in game_numbers if num in swns)
        
        if pwn_count == 6:
            winner_stats['1st class'] += 1
        elif pwn_count == 5:
            winner_stats['2nd class'] += 1
        elif pwn_count == 4:
            winner_stats['3rd class'] += 1
        elif pwn_count == 3 or swn_count == 2:
            winner_stats['4th class'] += 1
    
    return winner_stats

def display_data(lotto, WinNo):
    print("Player's ID Game Numbers")
    for idx, numbers in enumerate(lotto):
        print(f"{idx+1:4d} {numbers}")
    print("\nWinning Numbers (PWNs then SWNs):", WinNo[:6], WinNo[6:])

def display_winner_statistics(winner_stats):
    print("\nWinners statistics table:")
    print("Winner class\tTotal number of winners")
    for key, value in winner_stats.items():
        print(f"{key}\t{value}")

def check_player_status(player_id, lotto, WinNo):
    game_numbers = lotto[player_id - 1]
    pwns = WinNo[:6]
    swns = WinNo[6:]
    
    pwn_matches = match_value(game_numbers, pwns)
    swn_matches = match_value(game_numbers, swns)
    
    print(f"\nPlayer’s ID: {player_id}")
    print(f"Player’s game-numbers: {game_numbers}")
    print(f"PWNs: {pwns}")
    print(f"SWNs: {swns}")
    
    if pwn_matches == 6:
        print("Player’s status: You win the game, congratulations!")
    elif pwn_matches == 5:
        print("Player’s status: You are a 2nd class winner, congratulations!")
    elif pwn_matches == 4:
        print("Player’s status: You are a 3rd class winner, congratulations!")
    elif pwn_matches == 3:
        print("Player’s status: You are a 4th class winner, congratulations!")
    elif swn_matches == 2:
        print("Player’s status: You won a 4th-class prize with SWNs, congratulations!")
    else:
        print("Player’s status: You are not a winner. Thanks for playing lotto. Good luck next time!")

def menu(lotto, WinNo):
    while True:
        print("\nMain Menu:")
        print("1. Show Initialized data")
        print("2. Display statistics of winners")
        print("3. Check my lotto status")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            display_data(lotto, WinNo)
        elif choice == '2':
            winner_stats = process_winners(lotto, WinNo)
            display_winner_statistics(winner_stats)
        elif choice == '3':
            player_id = int(input("Enter your Player ID (1-1000): "))
            check_player_status(player_id, lotto, WinNo)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

def main():
    lotto, WinNo = initialize_data()
    menu(lotto, WinNo)

if __name__ == "__main__":
    main()


# In[ ]:




