Hi! Here are my practical exercises.

# 1. Currency_Converter
   Simple Python program to convert amounts between USD, EUR, and CAD using fixed exchange rates.
   How it works:
   - User enters an amount.
   - Chooses source and target currencies.
   - Program prints the converted value.
     
Example:
   ```text
   - Enter the amount: 100
   - Source currency (USD/EUR/CAD): USD
   - Target currency (USD/EUR/CAD): EUR
   - 100.00 USD is equal to 85.00 EUR
   ```
# 2. Dice_Rolling_Game
   Simple Python program that simulates rolling two dice.
   How it works:
   - The user is asked whether they want to roll the dice.
   - If “y”, the program prints two random numbers between 1 and 6.
   - If “n”, the game ends with a goodbye message.
     
Example:
   ```text
   - Roll the dice? (y/n): y
   - (3, 6)
   - Roll the dice? (y/n): n
   - Thanks for playing!
   ```
# 3. Number_Guessing_Game
   A simple Python game where you try to guess a random number between 1 and 100.
   How it works:
   - The computer randomly chooses a number.
   - You enter your guess.
   - The program tells you if your guess is too high, too low, or correct.
     
Example:
   ```text
   - Guess the number between 1 and 100: 50
   - Too low!
   - Guess the number between 1 and 100: 75
   - Too high!
   - Guess the number between 1 and 100: 63
   - Congratulations! You guessed the number.
   ```  
# 4. QR_Code_Generator
   Simple Python program that creates a QR code from any text or URL.
   How it works:
   - The user enters text (or a link) and a filename.
   - The program generates a purple-on-black QR code.
   - The image is saved as a .png file.
     
Example:
   ```text
   - Enter the text or URL: https://github.com/MykolaPereviznyk
   - Enter the filename: my_qr
   - QR code saved as my_qr.png
   ```
# 5. Rock_Paper_Scissor
   Classic Rock–Paper–Scissors game against the computer.
   How it works:
   - You enter r (rock), p (paper), or s (scissors).
   - The computer randomly picks one of the three.
   - The game shows both choices and the result: win, lose, or tie.
   - You can continue or quit.
     
Example:
   ```text
   - Rock, paper, or scissors? (r/p/s): r
   - You chose Rock
   - Computer chose Scissors
   - You win
   - Continue? (y/n): n
   ```
# 6. Tic_Tac_Toe
   A console-based Tic Tac Toe game for two players, using colored X and O symbols.
   How it works:
   - The board is a 3×3 grid.
   - Player X goes first, then players alternate.
   - Players choose a row and column (0–2).
   - The game checks for:
   - winning rows  
   - winning columns  
   - winning diagonals  
   - a full board (draw)
     
Example:
   ```text
   - Player X's turn
   - Enter row (0-2): 1
   - Enter column (0-2): 1
      |   |
   ---+---+---
      | X |
   ---+---+---
      |   |
   - Player O's turn...
   ```
# 7. Todo_List_App
   A simple console-based Todo List application that lets you view, add, and remove tasks from a list through a text-based menu.
   How it works:
   - The program starts with a predefined list of tasks.
   - A menu is displayed with four options:
   - View Tasks
   - Add a Task
   - Remove a Task
   - Exit
   - Depending on the user’s choice:
   - View Tasks — prints all existing tasks or shows “Empty” if the list has no items.
   - Add a Task — allows the user to enter a new task, which is added to the todo list.
   - Remove a Task — displays the list and allows the user to remove a task by its number.
   - Input is validated to ensure the user enters a valid option and valid task numbers.
   - The program continues looping until the user selects “Exit”.
     
Example:
   ```text
   -------------------------------------------
   Todo List Menu:
   -------------------------------------------
   1. View Tasks
   2. Add a Task
   3. Remove a Task
   4. Exit
   -------------------------------------------
   Enter your choice: 1
   -------------------------------------------
   1. Grecery shopping
   2. Reading
   -------------------------------------------
   
   -------------------------------------------
   Todo List Menu:
   -------------------------------------------
   1. View Tasks
   2. Add a Task
   3. Remove a Task
   4. Exit
   -------------------------------------------
   Enter your choice: 2
   Enter a new task: Finish Python exercises
   -------------------------------------------
   
   -------------------------------------------
   Todo List Menu:
   -------------------------------------------
   1. View Tasks
   2. Add a Task
   3. Remove a Task
   4. Exit
   -------------------------------------------
   Enter your choice: 3
   -------------------------------------------
   1. Grecery shopping
   2. Reading
   3. Finish Python exercises
   -------------------------------------------
   Enter your task!: 1
   -------------------------------------------
   
   -------------------------------------------
   Todo List Menu:
   -------------------------------------------
   1. View Tasks
   2. Add a Task
   3. Remove a Task
   4. Exit
   -------------------------------------------
   Enter your choice: 4
   ```
# 8. Simple_Text_Editor
   A basic console-based text editor that allows you to open, create, modify, and save text files.
   The program reads the contents of a file (if it exists), lets the user enter new text, and saves the updated content when the user types SAVE.
   How it works:
   - The user enters a filename to open or create.
   - If the file exists:
     - Its contents are displayed.
   - If the file does not exist:
     - A new empty file is created.
   - The user can then type any number of lines.
   - When the user types SAVE on a new line:
     - All the entered text is saved to the file.
     - A confirmation message appears.
   - If the file cannot be accessed, an error message is shown.

Example:
```text
Enter the filename to open or create: notes.txt
Shopping list:
- Milk
- Bread

Enter your text (type SAVE on a new line to save and exist):
Add eggs
Add apples
SAVE
notes.txt saved.

Enter the filename to open or create: todo.txt

Enter your text (type SAVE on a new line to save and exist):
Write documentation
Review Python code
SAVE
todo.txt saved.
```
# 9. Dice_Game
   A simple two-player dice game where each player tries to reach 100 points.
   Players can roll the die up to three times per turn and decide whether to roll again after each roll.
   If the player rolls a 1, their turn score becomes 0 and the turn ends immediately.

   How it works:
   - Two players start with a score of 0.
   - On each player's turn:
     - The player rolls the die.
     - The result is printed.
     - If the roll is 1:
       - The player's turn score becomes 0.
       - The turn ends right away.
     - Otherwise:
       - The rolled number is added to the player's score.
       - The player may choose to roll again (maximum three rolls per turn).
   - After both players finish their turns, the current total scores are displayed.
   - The first player to reach 100 points or more wins the game.

Example:
```text
Player 1's turn
You rolled a 4
Roll again? (y/n): y
You rolled a 6
Roll again? (y/n): n

Current: Player 1: 10, Player 2: 0

Player 2's turn
You rolled a 1
Player 2 scored 0 points this turn.

Current: Player 1: 10, Player 2: 0

Player 1's turn
You rolled a 5
Roll again? (y/n): y
You rolled a 3
Roll again? (y/n): n

Current: Player 1: 18, Player 2: 0

Player 1's turn
You rolled a 6
Roll again? (y/n): n
player 1 wins!
```
# 10. Cows_and_Bulls  
   A logic-based number-guessing game where you try to guess a 4-digit number with unique digits.

   How it works:
   - The computer generates a random 4-digit number (all digits are different).
   - You enter your guess (must also contain 4 unique digits).
   - The program returns:
     * Bulls — correct digit in the correct position
     * Cows — correct digit but in the wrong position
   - Goal: guess the number and get 4 bulls.

Example:
```text
   I have generated a 4-digit number with unique digits. Try to guess it!
   Guess: 1234
   1 cows, 0 bulls
   Guess: 4271
   2 cows, 1 bulls
   Guess: 4721
   0 cows, 4 bulls
   Congratulations! You guessed the correct number
```
# 11. Password_Strength_Checker  
   Simple Python program that checks how strong a password is.

   How it works:
   - You enter a password.
   - The program evaluates length, upper/lowercase letters, digits, and special symbols.
   - It prints the strength level: Very Weak, Weak, Medium, Hard, or Very Hard.

Example:
```text
   - Enter a password: Abc123!
   - Password strength: Hard
```

# 14. Slot_Machine_Game  
Simple Python slot machine game where you place bets and spin the reels.

How it works:
- You enter your starting balance.
- Place a bet for each round.
- The slot machine spins three symbols.
- If two symbols match — you win 2x your bet.
- If three symbols match — you win 3x your bet.
- If no symbols match — you lose your bet.
- The game continues until you quit or run out of money.

Example:
```text
   Enter your starting balance: $100
   Welcome to the slot Machine Game!
   You start with a balance of $100

   Current balance: $100
   Enter your bet amount: $10
   🍒|🍒|⭐
   You won $20

   Do you want to play again? (y/n): n
   You walk away with $110.
```

