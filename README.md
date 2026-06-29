🎮 Number Guess Tournament

A simple Python console-based number guessing game with multiple difficulty levels. Players choose a level, guess the randomly generated number within a limited number of attempts, and view their guess history after each round.

📌 Features
# Three difficulty levels:
-Easy (1–10, 3 attempts)
-Medium (1–50, 5 attempts)
-Hard (1–100, 7 attempts)
Random number generation
Limited attempts based on difficulty
Guess history displayed after every game
Tournament-style menu
Input validation for invalid entries
Play multiple rounds without restarting the program

🛠️ Technologies Used

Python 3
Built-in random module

🎮 Game Menu
1. Play New Tournament Round
2. View Tournament Rules
3. Exit Game

🎯 Difficulty Levels
Level	Number Range	Attempts
Easy	1 - 10	3
Medium	1 - 50	5
Hard	1 - 100	7

📋 Rules
Select a difficulty level.
Guess the randomly generated number.
You have a limited number of attempts.
The game provides hints whether your guess is too high or too low.
After the game ends, your complete guess history is displayed.
You can start a new tournament round from the main menu.

💻 Sample Output

-------------Number Guess Tournament----------------
==============Tournament Menu======================
1. Play New Tournament Round
2. View Tournament Rules
3. Exit Game

Enter Your Menu Choice: 1

Select your Level:
1. Easy
2. Medium
3. Hard

Easy Level Selected
Guess the number between 1 and 10

Round: 1
Enter your number: 5
Your Guess was Too Low

Round: 2
Enter your number: 8
---You Guessed the Right Number---

Your Previous Guess History: [5, 8]

🚀 Future Improvements

Score tracking
High score leaderboard
Multiplayer mode
Timer-based gameplay
Difficulty customization
Save game statistics to a file
🤝 Contributing

Contributions are welcome. Feel free to fork this repository, improve the project, and submit a pull request.

📄 License

This project is licensed under the MIT License. Feel free to use and modify it for learning purposes.
