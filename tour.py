"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "main":'
import time
from toah_model import TOAHModel


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """
    play_game((model, animate, delay_btw_moves, model.get_number_of_cheeses()),
              0, 1, 2, 3)

def play_game(t, first_stool, second_stool, third_stool,
              fourth_stool):
    """ ((TOAHModel, int, bool, int), int, int, int, int) -> None

    Automate the Anne Hoy game. 
    """
    model = t[0]
    animate = t[1]
    delay_btw_moves = t[2]
    cheeses = t[3]
    
    if cheeses == 1:
        model.move(first_stool, fourth_stool)
        if animate:
            print(model)
            time.sleep(delay_btw_moves)
    else:
        if cheeses == 2:
            i = 1
        else:
            i = 2
        
        play_game((model, animate, delay_btw_moves, cheeses - i), first_stool,
                  third_stool, fourth_stool, second_stool)
        play_game((model, animate, delay_btw_moves, 1), first_stool,
                  third_stool, second_stool, fourth_stool)
        play_game((model, animate, delay_btw_moves, cheeses - i), second_stool,
                  third_stool, first_stool, fourth_stool)

if __name__ == '__main__':
    num_cheeses = 5
    delay_between_moves = 0.5
    animation = input('Type "yes" if you would you like to animate the game?')
    console_animate = (animation == "yes")

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())
    # Leave files below to see what python_ta checks.
    # File tour_pyta.txt must be in same folder
    import python_ta
    python_ta.check_all(config="tour_pyta.txt")
