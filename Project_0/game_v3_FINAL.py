# The funtion that guesses the number in less than 20 attempts 
# Developed by Gleb Khamin

import numpy as np
from game_v2 import score_game

# the function
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1

        if number > predict:
          if (number - predict) > 10:
            predict += 11
          else:
            predict += 1

        elif number < predict:
          if (predict - number) > 10:
            predict -= 11
          else:
            predict -= 1


    return count


# Checking the efficiency of the function above
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
