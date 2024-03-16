# Treasure Hunt

This Python script implements a simple text-based adventure game where the player navigates through a grid, encountering various elements such as treasures, monsters, potions, swords, and venom. The goal is to accumulate points by collecting treasures while managing resources like swords and potions to survive encounters with monsters and venom.

## How to Play

1. The game starts with a grid containing treasures, monsters, potions, swords, and venom randomly placed.
2. The player begins at a random starting position on the grid.
3. The player can move left (L), up (U), right (R), or down (D) to navigate the grid.
4. Each move may reveal the contents of the current cell on the grid.
5. Points are earned by collecting treasures.
6. Swords and potions help the player survive encounters with monsters and venom, respectively.
7. Running out of resources or encountering certain dangers results in the end of the game.

## Script Overview

- `dateTimePlayed`: Timestamp indicating when the game was played.
- `playDictionary`: Dictionary to store game logs.
- `userPlayDictionary`: Dictionary to store individual user's game logs.
- Constants representing grid elements: `EX`, `REALEMPTY`, `EMPTY`, `TREASURE`, `MONSTER`, `VENOM`, `SWORD`, `POTION`.
- `whatToAddInGrid`: List of elements to be randomly added to the grid.
- `NROWS_IN_GRID`, `NCOLS_IN_GRID`: Number of rows and columns in the grid.
- `grid`: 2D list representing the game grid.
- `emptyGrid`: 2D list used for displaying the game grid to the player.
- Functions to find an empty cell on the grid and move the player.

## Usage

1. Run the script.
2. Follow the prompts to move the player around the grid and interact with elements.
3. Collect treasures, manage resources, and survive encounters to earn points.
