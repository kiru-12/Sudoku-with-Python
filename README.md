# Sudoku-with-Python
Sudoku Game &amp; Solver with Python
## Introduction
> This python program is essentially a sudoku game with a solver feature included. When executed, it allows the user to play sudoku games of their preferred difficulty. All successful solves will be recorded in the leaderboard. The solver feature allows the user to input any sudoku puzzle and the solver algorithm will reveal the solution

## The Game
> When the user opts for the game feature by clicking the 'PLAY' button in the home page, he/she will be prompted to enter his/her name and choose a difficulty level (easy, medium, hard, expert & insanely extreme). Upon selecting the difficulty, the user will be redirected to the game page where the puzzle will be displayed. There will be a stopwatch running to indicate the time elapsed. The user can take however long to solve the puzzle. The user will also have options to: 
>> i) Check his/her solution
>> 
>> ii) Reveal the solution
>> 
>> iii) Go back

## The Solver
> In the solver feature, the user will be given an empty 9x9 grid. The user can manually input an unsolved puzzle into the grid and click on **Reveal Solution** to get the solved puzzle.
> The user can also save the puzzle that he/she entered into the grid. The puzzle will be saved in a folder named **savedpuzzles** in the local directory. 
> The user can also open a puzzle which will be displayed on the empty grid. The puzzle can be opened from the **savedpuzzles** folder. To be precise, the user can open any folder that contains a puzzle **AS LONG AS** the puzzle is saved in a binary file (.dat) in the following configuration:
>> [
>> 
>> [1,0,1,1,0,1,1,1,1],
>> 
>> [1,1,0,1,1,1,1,1,1],
>> 
>> [1,1,1,1,1,1,1,1,1],
>> 
>> [1,1,1,1,0,1,0,1,1],
>> 
>> [1,1,1,1,1,1,1,1,1],
>> 
>> [1,1,0,1,1,1,1,1,1],
>> 
>> [1,1,1,1,1,1,0,1,1],
>> 
>> [1,1,1,0,1,1,1,1,1],
>> 
>> [1,1,1,1,1,1,1,1,1]
>> 
>> ]
>> 
> **not a real sudoku puzzle. just an example**
> 
> In place of the empty spaces in a real puzzle, the file must contains zeroes (0)
> 
