# Lotto Award Checking System

## Project Overview

This project simulates a Lotto award checking system. The system facilitates up to 1000 players to play Lotto and check their game status. The system is designed to generate random data for Lotto draws and to implement various functionalities to check the status of each player's game-numbers against winning numbers.

## Features

- **Initialization Stage:**
  - Generates random game-numbers for 1000 players.
  - Randomly generates winning numbers (8 distinct integers) where:
    - The first 6 are Primary Winning Numbers (PWNs).
    - The last 2 are Supplementary Winning Numbers (SWNs).

- **Data Pre-processing:**
  - Sorts game-numbers for all players using Merge Sort.
  - Sorts PWNs using Insertion Sort.
  - Sorts SWNs using Selection Sort.

- **Menu Options:**
  1. **Show Initialized Data:** Displays the game data and winning numbers.
  2. **Display Statistics of Winners:** Shows the number of winners in each class.
  3. **Check My Lotto Status:** Allows a player to check their Lotto status by entering their ID.

## Algorithms

### Sorting Algorithms
- **Insertion Sort:** Used to sort Primary Winning Numbers (PWNs).
- **Selection Sort:** Used to sort Supplementary Winning Numbers (SWNs).
- **Merge Sort:** Used to sort each player's game-numbers.

### Searching and Matching
- **Binary Search:** Utilized for checking the winner class based on the sorted arrays.
- **Match Value Algorithm:** Computes the matching values between two sorted integer arrays to determine the number of matching winning numbers.

## Implementation

### Initialization
- Generates random game-numbers for all players and winning numbers.
- Stores data in a two-dimensional array `lotto[0…999][0…5]` and an array `WinNo[0…7]`.

### Data Pre-processing
- Sorts the arrays as specified using the respective sorting algorithms.

### Menu Options
1. **Show Initialized Data:**
   - Prints tables of player game-numbers and winning numbers.
2. **Display Statistics of Winners:**
   - Calculates and displays the number of winners for each class.
3. **Check My Lotto Status:**
   - Displays player's game-numbers, winning numbers, and status based on matching results.

## Usage

1. **Initialization:**
   - The system automatically generates and initializes data on startup.

2. **Running the System:**
   - Execute the program and use the menu options to interact with the system:
     - **1. Show Initialized Data**
     - **2. Display Statistics of Winners**
     - **3. Check My Lotto Status**
     - **4. Exit**

## Example

To check the status of a player with ID 123, select option 3 and enter the ID when prompted. The system will display the player's game-numbers, the winning numbers, and the player's status.

## Dependencies

- Python 3.x

## Files

- `lotto_system.py`: Main Python file implementing the Lotto system.
- `README.md`: This file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

