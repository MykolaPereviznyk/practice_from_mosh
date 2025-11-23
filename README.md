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
