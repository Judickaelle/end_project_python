# end_project_python

Creation of a Memory game in console with Python.

The game will include a main menu where it is possible to choose the game (in case we want to add more game in the future). Then, for the memory game, it will be possible to choose between two decks of cards: The Letters (A, B, …) or the real card game (1♥, 1♠ …). It will also be possible to select the number of pairs to play with.

Two levels of difficulty will be available: Normal and Hard. For the normal one, the player has to find pairs. For the hard one, he must find quadruple.

At the end of each game, the number of try will be printed. Each game will also be saved in an external .txt file. For each line of this file will be written:
    The name of the player
    the date the game was played
    The difficulty
    The number of try

The player will be able to read this file from the main menu. From the main menu, it will also be possible to access to the statistic lobby. Here several statistics will be printed:
    The name of the player
    The number of games played
    The average of try per difficulty
    The best score per difficulty
    
Finally, it will be possible to print the global ranking of the Memory game from the main menu. Sort by the number of try.